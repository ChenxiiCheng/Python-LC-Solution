'''
Question: 
  206. Reverse Linked List

Descrition: 
  Reverse a singly linked list.

Examples:
	Input: 1->2->3->4->5->NULL
	Output: 5->4->3->2->1->NULL
'''

#Python3 Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Solution
        if head == None:
            return None
        prev = None
        while head:
            cur = head
            head = head.next
            cur.next = prev
            prev = cur
        return prev

        