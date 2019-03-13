'''
Question: 
  2. Add Two Numbers

Descrition: 
  You are given two non-empty linked lists representing two non-negative integers. 
  The digits are stored in reverse order and each of their nodes contain a single digit. 
  Add the two numbers and return it as a linked list.
  You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Examples:

  Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
  Output: 7 -> 0 -> 8
  Explanation: 342 + 465 = 807.
'''

#Python3 Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        #Solution 2
        if not l1 or not l2:
            return l1 or l2
        dummy = root = ListNode(0)
        add = 0
        while l1 or l2 or add:
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + add
            add = val // 10
            root.next = ListNode(val % 10)
            root = root.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next       
        
        #Solution
        if not l1 or not l2:
            return l1 or l2
        dummy = root = ListNode(0)
        add = 0
        while l1 or l2 or add:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            add, val = divmod(v1 + v2 + add, 10)
            root.next = ListNode(val)
            root = root.next
        return dummy.next

        