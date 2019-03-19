'''
Question: 
  694. Number of Distinct Islands

Descrition: 
  Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) 
  connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

  Count the number of distinct islands. An island is considered to be the same as another if and only if one island 
  can be translated (and not rotated or reflected) to equal the other.

Examples:
  1.Input
	11000
	11000
	00011
	00011
    Given the above grid map, return 1.

  2.Input
    11011
	10000
	00001
	11011
	Given the above grid map, return 3.

	Notice that:
	11
	1
	and
	 1
	11
	are considered different island shapes, because we do not consider reflection / rotation.
'''

#Python3 Code:

class Solution:
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #Solution
        m, n = len(grid), len(grid[0])
        self.steps = ''
        dist = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.dfs(grid, i, j, 'o')
                    dist.add(self.steps)
                    self.steps = ''
        return len(dist)
    def dfs(self, grid, i, j, direction):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
            return
        self.steps += direction
        grid[i][j] = '#'
        self.dfs(grid, i + 1, j, 'd')
        self.dfs(grid, i - 1, j, 'u')
        self.dfs(grid, i, j + 1, 'r')
        self.dfs(grid, i, j - 1, 'l')
        self.steps += 'b'

        