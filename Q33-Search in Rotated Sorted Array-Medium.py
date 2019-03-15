'''
Question: 
  33. Search in Rotated Sorted Array

Descrition: 
  Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
  (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
  
  You are given a target value to search. If found in the array return its index, otherwise return -1.

  You may assume no duplicate exists in the array.

  Your algorithm's runtime complexity must be in the order of O(log n).

Examples:

  1.Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

  2.Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1
'''

#Python3 Code:

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #Solution
        #二分法，先判断中值是属于哪边的升序序列，再根据端点值继续判断 target 该落在左边还是右边区域
        if not nums or target is None:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            if nums[mid] <= nums[right]:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

        