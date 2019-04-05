'''
Question: 
  338. Counting Bits

Descrition: 
   Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's 
   in their binary representation and return them as an array.

Example:

  1.Input: 2
  	Output: [0,1,1]

  2.Input: 5
	Output: [0,1,1,2,1,2]
'''

#Python code

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        #Solution 2
        #用动态规划做：
        # 如果i是偶数，那么i中1的个数和i//2中1的个数是一样的
        # 如果i是奇数，那么i中1的个数和i//2中1的个数+1。
        # 所以主要问题就是判断i的奇偶性，可以用i&1来判断
        dp = [None] * (num + 1)
        dp[0] = 0
        for i in range(1, num + 1):
            if i % 2 == 0:
                dp[i] = dp[i // 2]
            else:
                dp[i] = 1 + dp[i // 2]
        return dp
        
        
        #Solution
        ans = [0] * (num + 1)
        count = 0
        for i in range(num + 1):
            ch = bin(i)[2:]
            for j in ch:
                if j == '1':
                    count += 1
            ans[i] = count
            count = 0
        return ans

        