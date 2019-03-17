'''
Question: 
  56. Merge Intervals

Descrition: 
  Given a collection of intervals, merge all overlapping intervals.

Examples:

  1.Input: [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]
    Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

  2.Input: [[1,4],[4,5]]
    Output: [[1,5]]
    Explanation: Intervals [1,4] and [4,5] are considered overlapping.
'''

#Python3 Code:

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        #Solution
        if not intervals:
            return []
        intervals.sort(key=lambda x:x.start)
        stack = [intervals[0]]
        for i in intervals[1:]:
            if i.start <= stack[-1].end:
                stack[-1].end = max(stack[-1].end, i.end)
            else:
                stack.append(i)
        return stack

        