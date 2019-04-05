'''
Question: 
  198. House Robber

Descrition: 
   You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, 
   the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and 
   it will automatically contact the police if two adjacent houses were broken into on the same night.
   Given a list of non-negative integers representing the amount of money of each house, 
   determine the maximum amount of money you can rob tonight without alerting the police.

Example:

  1.Input: [1,2,3,1]
	Output: 4
	Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3). Total amount you can rob = 1 + 3 = 4.

  2.Input: [2,7,9,3,1]
	Output: 12
	Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1). Total amount you can rob = 2 + 9 + 1 = 12.
'''

#Python code

class Solution:
    def rob(self, nums: List[int]) -> int:
        #Solution
        #经典的动态规划问题，dp[i]表示从偷到第i个房子能偷盗的最大数额（此时，i从0开始，范围内的最后一个房子可以偷也可以不             #偷,最后返回dp[n-1]，dp[0]=nums[0]，dp[1]=max(nums[0],nums[1])，对于第i个屋子（此处i从0开始，这一天的价值是           #nums[i]），这一天，小偷可以选择不偷盗，保持dp[i-1]，或者选择偷盗，但是偷盗的话，前一天必定不能偷盗，所以偷盗的价值是         #dp[i-2]+nums[i]，所以转移方程是dp[i]=max(dp[i-1],dp[i-2]+nums[i])。
        if not nums:
            return 0
        n = len(nums)
        if n < 2:
            return nums[0]
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]

        