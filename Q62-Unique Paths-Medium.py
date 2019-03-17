'''
Question: 
  62. Unique Paths

Descrition: 
  A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

  The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

  How many possible unique paths are there?

Examples:

  1.Input: m = 3, n = 2
    Output: 3
    Explanation:
      From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
      1. Right -> Right -> Down
      2. Right -> Down -> Right
      3. Down -> Right -> Right

  2.Input: m = 7, n = 3
    Output: 28
'''

#Python3 Code:

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #Solution
        if not m or not n:
            return 0
        dp = [[1 for _ in range(n)] for __ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

        
