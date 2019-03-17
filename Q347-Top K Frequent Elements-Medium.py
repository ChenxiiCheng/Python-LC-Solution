'''
Question: 
  347. Top K Frequent Elements

Descrition: 
  Given a non-empty array of integers, return the k most frequent elements.

Examples:

  1.Input: nums = [1,1,1,2,2,3], k = 2
    Output: [1,2]

  2.Input: nums = [1], k = 1
    Output: [1]
'''

#Python3 Code:

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #Solution 3
        count = collections.Counter(nums)
        return [item[0] for item in count.most_common(k)]
        
        
        #Solution 2
        count = collections.Counter(nums)
        return heapq.nlargest(k, count, key=lambda x:count[x])
        
        
        #Solution
        ans = []
        count = collections.Counter(nums)
        output = sorted(count.items(), key=lambda x:x[1], reverse=True)
        for i in range(k):
            ans.append(output[i][0])
        return ans

        