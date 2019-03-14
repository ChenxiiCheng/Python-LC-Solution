'''
Question: 
  658. Find K Closest Elements

Descrition: 
  Given a sorted array, two integers k and x, find the k closest elements to x in the array. 
  The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Examples:

  1.Input: [1,2,3,4,5], k=4, x=3
    Output: [1,2,3,4]

  2.Input: [1,2,3,4,5], k=4, x=-1
    Output: [1,2,3,4]
'''

#Python3 Code:

class Solution:
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        #Solution 2
        while len(arr) > k:
            if x - arr[0] <= arr[-1] - x:
                arr.pop()
            else:
                arr.pop(0)
        return arr
        
        
        #Solution
        left, right = 0, len(arr) - k
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] <= arr[mid + k] - x:
                right = mid
            else:
                left = mid + 1
        return arr[left:left + k]

        