'''
Question: 
  21. Merge Two Sorted Lists

Descrition: 
  Merge two sorted linked lists and return it as a new list. 
  The new list should be made by splicing together the nodes of the first two lists.

Examples:
  Input: 1->2->4, 1->3->4
  Output: 1->1->2->3->4->4
'''

#Python3 Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        #Solution
        dummy = root = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                root.next = l1
                l1 = l1.next
            else:
                root.next = l2
                l2 = l2.next
            root = root.next
        root.next = l1 or l2
        return dummy.next

        