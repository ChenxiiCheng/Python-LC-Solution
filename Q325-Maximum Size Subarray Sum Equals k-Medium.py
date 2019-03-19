'''
Question: 
  325. Maximum Size Subarray Sum Equals k

Descrition: 
  Given an array nums and a target value k, find the maximum length of a subarray that sums to k. 
  If there isn't one, return 0 instead.

  Note:
  The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

Examples:
  1.Input: nums = [1, -1, 5, -2, 3], k = 3
    Output: 4 
    Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest.

  2.Input: nums = [-2, -1, 2, 1], k = 1
    Output: 2 
    Explanation: The subarray [-1, 2] sums to 1 and is the longest.
'''

#Python3 Code:

class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #Solution
        #初始化dic是为了避免0的情况
        #eg:[1,-1,5,-2,3] k=3
        #若没初始化dic={1:0,0:1,5:2} 当i=3,curSum=5-2=3,3-3=0
        #则ans=max(0, 3-1)=2而不是4
        #若初始化dic={0:-1,1:0,5:2} 当i=3，curSum=5-2=3,3-3=0
        #则ans=max(0, 3-(-1))=4
        if not nums or k is None:
            return 0
        ans = curSum = 0
        dic = {0:-1}
        for i in range(len(nums)):
            curSum += nums[i]
            if curSum - k in dic:
                ans = max(ans, i - dic[curSum - k])
            if curSum not in dic:
                dic[curSum] = i
        return ans

        