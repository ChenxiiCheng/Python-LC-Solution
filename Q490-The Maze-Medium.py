'''
Question: 
  490. The Maze

Descrition: 
  There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by 
  rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, it could choose the next direction.

  Given the ball's start position, the destination and the maze, determine whether the ball could stop at the destination.

  The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. 
  You may assume that the borders of the maze are all walls. The start and destination coordinates are represented by row and column indexes.

Examples:

    Input 1: a maze represented by a 2D array

	0 0 1 0 0
	0 0 0 0 0
	0 0 0 1 0
	1 1 0 1 1
	0 0 0 0 0

	Input 2: start coordinate (rowStart, colStart) = (0, 4)
	Input 3: destination coordinate (rowDest, colDest) = (4, 4)

	Output: true
	Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.
'''

#Python3 Code:

class Solution:
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        #Solution
        m, n = len(maze), len(maze[0])
        
        def dfs(x, y, visited):
            if (x, y) in visited:
                return False
            visited.add((x, y))
            if [x, y] == destination:
                return True
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                row, col = x, y
                while 0 <= row + i < m and 0 <= col + j < n and maze[row + i][col + j] != 1:
                    row += i
                    col += j
                if dfs(row, col, visited):
                    return True
            return False
        return dfs(start[0], start[1], set())

        