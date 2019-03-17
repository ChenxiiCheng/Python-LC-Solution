'''
Question: 
  286. Walls and Gates

Descrition: 
  You are given a m x n 2D grid initialized with these three possible values.

  -1 - A wall or an obstacle.
  0 - A gate.
  INF - Infinity means an empty room. We use the value 231 - 1 = 2147483647 to 
  represent INF as you may assume that the distance to a gate is less than 2147483647.
  Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, 
  it should be filled with INF.

Examples:

	Given the 2D grid:
	INF  -1  0  INF
	INF INF INF  -1
	INF  -1 INF  -1
	  0  -1 INF INF

	After running your function, the 2D grid should be:
	  3  -1   0   1
	  2   2   1  -1
	  1  -1   2  -1
	  0  -1   3   4

'''

#Python3 Code:

class Solution:
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        #Solution
        if not rooms:
            return None
        m, n = len(rooms), len(rooms[0])
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    self.helper(rooms, i, j, 0)
    def helper(self, rooms, i, j, dist):
        if i < 0 or j < 0 or i >= len(rooms) or j >= len(rooms[0]) or rooms[i][j] < dist:
            return
        rooms[i][j] = dist
        self.helper(rooms, i + 1, j, dist + 1)
        self.helper(rooms, i - 1, j, dist + 1)
        self.helper(rooms, i, j + 1, dist + 1)
        self.helper(rooms, i, j - 1, dist + 1)

        