'''
Question: 
  406. Queue Reconstruction by Height

Descrition: 
   Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), 
   where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. 
   Write an algorithm to reconstruct the queue.

Example:

  Input:
    [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

  Output:
    [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''

#Python code

class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        #Solution
        #(-x[0], x[1]) 先按x[0]大小排，若出现相同的x[0],再按照x[1]大小排
        people = sorted(people, key=lambda x:(-x[0], x[1]))
        ans = []
        for x in people:
            ans.insert(x[1], x)
        return ans

        