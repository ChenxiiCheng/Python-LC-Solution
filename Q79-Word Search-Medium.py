'''
Question: 
  79. Word Search

Descrition: 
  Given a 2D board and a word, find if the word exists in the grid.

  The word can be constructed from letters of sequentially adjacent cell, 
  where "adjacent" cells are those horizontally or vertically neighboring. 
  same letter cell may not be used more than once.

Examples:
  board =
	[
	  ['A','B','C','E'],
	  ['S','F','C','S'],
	  ['A','D','E','E']
	]

  Given word = "ABCCED", return true.
  Given word = "SEE", return true.
  Given word = "ABCB", return false.
'''

#Python3 Code:

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        #Solution
        #先考虑只能从某个固定位置起始的组合，如果说没有“数组中每个字符只能使用一次”的限制的话，
        #我们只需要递归的对这个位置的四个方向探索word[1:]即可，
        #加上这个限制后我们每次探索前要把这个位置先修改成非字符元素(如None)，
        #但是注意因为是递归算法所以每次修改之后都要改回原来的值。
        if not board or word is None:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False
    def dfs(self, board, i, j, word):
        if not word:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]
        board[i][j] = '#'
        res = self.dfs(board, i + 1, j, word[1:]) or self.dfs(board, i - 1, j, word[1:]) or \
                self.dfs(board, i, j + 1, word[1:]) or self.dfs(board, i, j - 1, word[1:])
        board[i][j] = tmp
        return res

        