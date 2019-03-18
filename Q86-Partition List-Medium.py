'''
Question: 
  86. Partition List

Descrition: 
  Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

  You should preserve the original relative order of the nodes in each of the two partitions.

Examples:
  Input: head = 1->4->3->2->5->2, x = 3
  Output: 1->2->2->4->3->5
'''

#Python3 Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        #Solution
        if not head:
            return None
        dummy1 = root1 = ListNode(0) 
        dummy2 = root2 = ListNode(0)
        while head:
            if head.val < x:
                root1.next = head
                root1 = root1.next
            else:
                root2.next = head
                root2 = root2.next
            head = head.next
        root2.next = None
        root1.next = dummy2.next
        return dummy1.next

        