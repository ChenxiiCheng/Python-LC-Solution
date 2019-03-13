'''
Question: 
  200. Number of Islands

Descrition: 
  Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
  An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
  You may assume all four edges of the grid are all surrounded by water.

Examples:

  Input:
  11000
  11000
  00100
  00011

  Output: 3
'''

#Python3 Code:

class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        #Solution
        if not grid:
            return 0
        count = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    count += 1
                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1 or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)

        