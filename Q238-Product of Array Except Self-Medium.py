'''
Question: 
  238. Product of Array Except Self

Descrition: 
  Given an array nums of n integers where n > 1, return an array output 
  such that output[i] is equal to the product of all the elements of nums except nums[i].

Examples:

  Input:  [1,2,3,4]
  Output: [24,12,8,6]
'''

#Python3 Code:

class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #Solution
        p = 1
        output = []
        for i in range(len(nums)):
            output.append(p)
            p *= nums[i]
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= p
            p *= nums[i]
        return output

        