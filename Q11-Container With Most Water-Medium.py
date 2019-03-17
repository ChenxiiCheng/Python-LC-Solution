'''
Question: 
  11. Container With Most Water

Descrition: 
  Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
  n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, 
  which together with x-axis forms a container, such that the container contains the most water.

  Note: You may not slant the container and n is at least 2.

Examples:
	Input: [1,8,6,2,5,4,8,3,7]
	Output: 49
'''

#Python3 Code:

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #Solution
        if not height:
            return 0
        left, right = 0, len(height) - 1
        max_area = area = 0
        while left < right:
            l, r = height[left], height[right]
            if l < r:
                area = (right - left) * l
                while height[left] <= l:
                    left += 1
            else:
                area = (right - left) * r
                while height[right] <= r and right:
                    right -= 1
            max_area = max(max_area, area)
        return max_area

        