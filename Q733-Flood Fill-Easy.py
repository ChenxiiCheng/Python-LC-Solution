'''
Question: 
  733. Flood Fill

Descrition: 
  An image is represented by a 2-D array of integers, each integer representing the pixel value of the image (from 0 to 65535).
  Given a coordinate (sr, sc) representing the starting pixel (row and column) of the flood fill, and a pixel value newColor, "flood fill" the image.
  To perform a "flood fill", consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
  plus any pixels connected 4-directionally to those pixels (also with the same color as the starting pixel), and so on. 
  Replace the color of all of the aforementioned pixels with the newColor.

  At the end, return the modified image.

Examples:

Input: 
	image = [[1,1,1],[1,1,0],[1,0,1]]
	sr = 1, sc = 1, newColor = 2
	Output: [[2,2,2],[2,2,0],[2,0,1]]
	Explanation: 
	From the center of the image (with position (sr, sc) = (1, 1)), all pixels connected 
	by a path of the same color as the starting pixel are colored with the new color.
	Note the bottom corner is not colored 2, because it is not 4-directionally connected
	to the starting pixel.
'''

#Python3 Code:

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        #Solution 3 - BFS
        old, m, n = image[sr][sc], len(image), len(image[0])
        if old != newColor: 
            q = collections.deque([(sr, sc)])
            while q:
                i, j = q.popleft()
                image[i][j] = newColor
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and image[x][y] == old: 
                        q.append((x, y))
        return image
        
        
        #Solution 2 - DFS
        #经典的dfs方法，要保存一下指定位置的颜色再对该位置染色，
        #并对其四个方向的相邻元素进行处理，如果颜色和以前的颜色相同即染色并递归调用。
        color = image[sr][sc]
        if color != newColor:
            self.dfs(image, sr, sc, color, newColor)
        return image
    def dfs(self, image, i, j, color, newColor):
        m, n = len(image), len(image[0])
        if image[i][j] == color:
            image[i][j] = newColor
            if i >= 1: 
                self.dfs(image, i - 1, j, color, newColor)
            if i + 1 < m:
                self.dfs(image, i + 1, j, color, newColor)
            if j >= 1:
                self.dfs(image, i, j - 1, color, newColor)
            if j + 1 < n:
                self.dfs(image, i, j + 1, color, newColor)
        
        
        #Solution - DFS
        SR, SC = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image
        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r - 1, c)
                if r < SR - 1: dfs(r + 1, c)
                if c >= 1: dfs(r, c - 1)
                if c < SC - 1: dfs(r, c + 1)
        dfs(sr, sc)
        return image

        