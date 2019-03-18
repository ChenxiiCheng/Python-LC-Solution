'''
Question: 
  16. 3Sum Closest

Descrition: 
  Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. 
  Return the sum of the three integers. You may assume that each input would have exactly one solution.

Examples:
  Given array nums = [-1, 2, 1, -4], and target = 1.
  The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

#Python3 Code:

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #Solution
        if not nums or target is None:
            return 0
        nums.sort()
        n = len(nums)
        ans = float('inf')
        for i in range(n - 2):
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(s - target) < abs(ans - target):
                    ans = s
                elif s > target:
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    return target
        return ans

        