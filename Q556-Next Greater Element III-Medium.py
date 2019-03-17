'''
Question: 
  556. Next Greater Element III

Descrition: 
  Given a positive 32-bit integer n, you need to find the smallest 32-bit integer 
  which has exactly the same digits existing in the integer n and is greater in value than n. 
  If no such positive 32-bit integer exists, you need to return -1.

Examples:

  1.Input: 12
    Output: 21

  2.Input: 21
    Output: -1
'''

#Python3 Code:

class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Solution
        # nums = [int(i) for i in str(n)]
        nums = list(str(n))
        i = len(nums) - 1
        j = -1
        while i:
            if nums[i - 1] < nums[i]:
                j = i - 1
                break
            i -= 1
        if j == -1:
            return -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                nums[j + 1:] = sorted(nums[j + 1:])
                # nums = int(''.join([str(i) for i in nums]))
                ans = int(''.join(nums))
                return ans if -2**31 <= ans <= 2**31 - 1 else -1

