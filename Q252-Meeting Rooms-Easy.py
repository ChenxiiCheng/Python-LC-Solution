'''
Question: 
  252. Meeting Rooms

Descrition: 
  Given an array of meeting time intervals consisting of start and end times 
  [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Examples:

  1.Input: [[0,30],[5,10],[15,20]]
    Output: false

  2.Input: [[7,10],[2,4]]
    Output: true
'''

#Python3 Code:

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        #Solution
        if not intervals:
            return True
        intervals.sort(key=lambda x:x.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True

        