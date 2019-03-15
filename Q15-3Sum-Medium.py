'''
Question: 
  15. 3Sum

Descrition: 
  Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? 
  Find all unique triplets in the array which gives the sum of zero.

  Note:
    The solution set must not contain duplicate triplets.

Examples:

	Given array nums = [-1, 0, 1, 2, -1, -4],

	A solution set is:
	[
	  [-1, 0, 1],
	  [-1, -1, 2]
	]
'''

#Python3 Code:

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #Solution 2
        if len(nums) < 3:
            return []
        nums.sort()
        ans = set()
        for i, v in enumerate(nums[:-2]):
            if v != 0 and nums[i] == nums[i - 1]:
                continue
            dic = {}
            for x in nums[i + 1:]:
                if x not in dic:
                    dic[-v-x] = 1
                else:
                    ans.add((v, -v-x, x))
        return [list(x) for x in ans]
        
        
        #Solution
        if len(nums) < 3:
            return []
        n = len(nums)
        ans = []
        nums.sort()
        for i in range(n - 2):
            if i != 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1; right -= 1
        return ans

        