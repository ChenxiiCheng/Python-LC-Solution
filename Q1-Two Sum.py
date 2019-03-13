'''
Question: 
  1. Two Sum

Descrition: 
  Given an array of integers, return indices of the two numbers such that they add up to a specific target.
  You may assume that each input would have exactly one solution, and you may not use the same element twice.

Examples:
  Given nums = [2, 7, 11, 15], target = 9,
  Because nums[0] + nums[1] = 2 + 7 = 9,
  return [0, 1].
'''

#Python3 Code:

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Solution 2
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i
        return [-1, -1]
        
        
        #Solution 1
        for i in range(len(nums)):
            #因为如果是j从i开始，则[3,2,4]会直接返回[0,0]
            #因为3+3=6，而题目说不能重复使用元素
            for j in range(i + 1, len(nums)):
                if target == nums[i] + nums[j]:
                    return [i, j]
        return [-1, -1]

