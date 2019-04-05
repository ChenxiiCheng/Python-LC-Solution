'''
Question: 
  221. Maximal Square

Descrition: 
  Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

    Input: 

    1 0 1 0 0
    1 0 1 1 1
    1 1 1 1 1
    1 0 0 1 0

    Output: 4

'''

#Python code

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        #设这个DP[i][j]数组为以i, j位置为右下角顶点的能够成的最大正方形的边长。
        #数组如果是第一行或者第一列，显然dp和matrix相等。如果是其他位置，
        #当matrix[i][j] = 1时，能够成的正方形等于左边、上边、左上能够成的正方形边长的最小值+1.
        #为什么是最小值？因为只要存在一个0，那么就没法构成更大的正方形，这个是很保守的策略。

        #递推公式如下：

        #dp[0][j] = matrix[0][j] (topmost row);
        #dp[i][0] = matrix[i][0] (leftmost column);
        #For i > 0 and j > 0: if matrix[i][j] = 0, dp[i][j] = 0; 
        #if matrix[i][j] = 1, dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1.

        if not matrix:
            return 0
        ans = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
        for j in range(n):
            dp[0][j] = int(matrix[0][j])
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == '1':
                    dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1
        for row in dp:
            ans = max(ans, max(row))
        return ans ** 2

        