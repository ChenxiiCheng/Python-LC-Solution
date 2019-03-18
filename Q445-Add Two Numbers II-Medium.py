'''
Question: 
  445. Add Two Numbers II

Descrition: 
  You are given two non-empty linked lists representing two non-negative integers. 
  The most significant digit comes first and each of their nodes contain a single digit. 
  Add the two numbers and return it as a linked list.

  You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Examples:
	Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 8 -> 0 -> 7
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
        #Solution
        #注意这里先生成的节点是最后面的
        #所以这里是每次把cur加入到链表里
        #dummy -> cur ->
        #所以是cur.next = dummy.next
        #dummy.next = cur 
        s1, s2 = [], []
        while l1:
            s1.append(l1)
            l1 = l1.next
        while l2:
            s2.append(l2)
            l2 = l2.next
        s = 0
        dummy = ListNode(0)
        while s1 or s2 or s:
            if s1:
                s += s1.pop().val
            if s2:
                s += s2.pop().val
            cur = ListNode(s % 10)
            cur.next = dummy.next
            dummy.next = cur
            s //= 10
        return dummy.next

