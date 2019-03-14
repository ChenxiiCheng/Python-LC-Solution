'''
Question: 
  322. Coin Change

Descrition: 
  You are given coins of different denominations and a total amount of money amount. 
  Write a function to compute the fewest number of coins that you need to make up that amount. 
  If that amount of money cannot be made up by any combination of the coins, return -1.

Examples:

  1.Input: coins = [1, 2, 5], amount = 11
    Output: 3 
    Explanation: 11 = 5 + 5 + 1

  2.Input: coins = [2], amount = 3
    Output: -1
'''

#Python3 Code:

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Solution 2
        #题目比较重要的是硬币无限数量。我们的做法是使用动态规划，
        #需要构建一个长度是amount + 1的dp数组，其含义是能够成面额从0到amount + 1需要使用的最少硬币数量。
        #所以我们对每一种面额的硬币，都去计算并更新新添了这种面额的情况下，
        #构成的所有面额需要的最少硬币数量。注意，变量是不同面额的硬币。
        #dp更新的策略是从coin面额到amount+1的面额依次向后查找，
        #看这个位置能不能用更少的硬币组成（即使用面额是i - coin的需要硬币数量+1).
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, amount + 1):
                if dp[i - coin] != float('inf'):
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]
        
        
        #Solution 1
        dp = [float('inf') for i in range(amount + 1)]
        dp[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

        