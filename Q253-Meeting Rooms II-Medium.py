'''
Question: 
  253. Meeting Rooms II

Descrition: 
  Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), 
  find the minimum number of conference rooms required.

Examples:

  1.Input: [[0, 30],[5, 10],[15, 20]]
  Output: 2

  2.Input: [[7,10],[2,4]]
  Output: 1
'''

#Python3 Code:

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        #Solution
        #是用heap[0]而不是heap[-1]，因为若intervals=[[0,30],[5,10],[15,20]]
        #到i=[15,20]时，heap=[30,10]，这时候若拿的是heap[-1]=30，记住python中是最小堆
        #应该拿heap[0]=10，判断10<=15，则这个i可以和上个i共用同个房间
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        heap = []
        for i in intervals:
            if heap and heap[0] <= i.start:
                heapq.heapreplace(heap, i.end)
            else:
                heapq.heappush(heap, i.end)
        return len(heap)

        