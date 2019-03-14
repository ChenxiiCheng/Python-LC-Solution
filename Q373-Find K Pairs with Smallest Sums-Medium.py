'''
Question: 
  373. Find K Pairs with Smallest Sums

Descrition: 
  You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.
  Define a pair (u,v) which consists of one element from the first array and one element from the second array.
  Find the k pairs (u1,v1),(u2,v2) ...(uk,vk) with the smallest sums.

Examples:

  1.Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
    Output: [[1,2],[1,4],[1,6]] 
    Explanation: The first 3 pairs are returned from the sequence: 
             [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

  2.Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
    Output: [1,1],[1,1]
    Explanation: The first 2 pairs are returned from the sequence: 
             [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
'''

#Python3 Code:

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        #Solution 2
        if not nums1 or not nums2:
            return []
        if k < 1:
            return []
        if k == 1:
            return [[nums1[0], nums2[0]]]
        visited = {}
        heap = []
        output = []
        heapq.heappush(heap, (nums1[0] + nums2[0], 0, 0))
        visited[(0,0)] = 1
        
        while heap and len(output) < k:
            pair = heapq.heappop(heap)
            curSum, ptr1, ptr2 = pair[0], pair[1], pair[2]
            output.append([nums1[ptr1], nums2[ptr2]])
            if ptr1 < len(nums1) - 1 and (ptr1 + 1, ptr2) not in visited:
                heapq.heappush(heap, (nums1[ptr1 + 1] + nums2[ptr2], ptr1 + 1, ptr2))
                visited[(ptr1 + 1, ptr2)] = 1
            if ptr2 < len(nums2) - 1 and (ptr1, ptr2 + 1) not in visited:
                heapq.heappush(heap, (nums1[ptr1] + nums2[ptr2 + 1], ptr1, ptr2 + 1))
                visited[(ptr1, ptr2 + 1)] = 1
        return output
        
        
        #Solution
        if not nums1 or not nums2: return []
        h = []
        
        # pair combination
        for i in range(len(nums1)):
            heapq.heappush(h, (nums1[i] + nums2[0], i, 0))

        # return k smallest pairs
        res = []
        while h and k > 0:
            small, i, j = heapq.heappop(h)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(h, (nums1[i] + nums2[j + 1], i, j + 1))
            k -= 1
        
        return res

        