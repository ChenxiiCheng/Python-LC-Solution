'''
Question: 
  215. Kth Largest Element in an Array

Descrition: 
  Find the kth largest element in an unsorted array. 
  Note that it is the kth largest element in the sorted order, not the kth distinct element.

Examples:

  1.Input: [3,2,1,5,6,4] and k = 2
    Output: 5

  2.Input: [3,2,3,1,2,4,5,5,6] and k = 4
    Output: 4
'''

#Python3 Code:

class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #Another way
        #Solution
        if not nums or k is None:
            return -1
        heap = []
        for ch in nums:
            heapq.heappush(heap, ch)
        while len(heap) > k:
            heapq.heappop(heap)
        return heapq.heappop(heap)
        
        
        #Solution 2
        heap = []
        for i in range(len(nums)):
            heapq.heappush(heap, nums[i])
        for _ in range(len(nums) - k):
            heapq.heappop(heap)
        return heapq.heappop(heap)
        
        
        #Solution
        return sorted(nums)[-k]

        
