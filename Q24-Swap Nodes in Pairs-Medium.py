'''
Question: 
  24. Swap Nodes in Pairs

Descrition: 
  Given a linked list, swap every two adjacent nodes and return its head.

  You may not modify the values in the list's nodes, only nodes itself may be changed.

Examples:
  Given 1->2->3->4, you should return the list as 2->1->4->3.
'''

#Python3 Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Solution
        dummy = root = ListNode(0)
        dummy.next = head
        while root.next and root.next.next:
            p1, p2 = root.next, root.next.next
            root.next, p1.next, p2.next = p2, p2.next, p1
            root = root.next.next
        return dummy.next

        