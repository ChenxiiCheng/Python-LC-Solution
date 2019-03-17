'''
Question: 
  505. The Maze II

Descrition: 
  There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by 
  rolling up, down, left or right, but it won't stop rolling until hitting a wall. 
  When the ball stops, it could choose the next direction.

  Given the ball's start position, the destination and the maze, find the shortest distance for the ball to stop at the destination. 
  The distance is defined by the number of empty spaces traveled by the ball from the start position (excluded) to the destination (included). 
  If the ball cannot stop at the destination, return -1.

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

	Output: 12

	Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
	             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.
'''

#Python3 Code:

class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        #Solution
        m, n = len(maze), len(maze[0])
        q, visited = [(0, start[0], start[1])], {(start[0], start[1]):0}
        while q:
            dist, x, y = heapq.heappop(q)
            if [x, y] == destination:
                return dist
            for i, j in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                r, c, d = x, y, 0
                while 0 <= r + i < m and 0 <= c + j < n and maze[r + i][c + j] != 1:
                    r += i
                    c += j
                    d += 1
                if (r, c) not in visited or dist + d < visited[(r, c)]:
                    visited[(r, c)] = dist + d
                    heapq.heappush(q, (dist + d, r, c))
        return -1

        