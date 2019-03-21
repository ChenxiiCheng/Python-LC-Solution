'''
Question: 
  328. Odd Even Linked List

Descrition: 
  Given a singly linked list, group all odd nodes together followed by the even nodes. 
  Please note here we are talking about the node number and not the value in the nodes.

  You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Examples:
  1.Input: 1->2->3->4->5->NULL
    Output: 1->3->5->2->4->NULL

  2.Input: 2->1->3->5->6->4->7->NULL
    Output: 2->3->6->7->1->5->4->NULL
'''

#Python3 Code:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        #Solution 2
        #1->2->3->4->5->6->Null
        #1->3->5 odd.next=odd.next.next 就是5->Null
        #但是因为if odd.next!=None才改变odd，所以这里odd还是在5
        #2->4->6,这里判断if even and even.next 存在
        #才会even向后走，6后面是null,所以不会再往后走了
        if not head:
            return head
        
        odd = head
        even = even_head = head.next
        
        while odd.next:
            odd.next = odd.next.next
            if odd.next != None:
                odd = odd.next
            if even and even.next:
                even.next = even.next.next
                even = even.next
        odd.next = even_head
        return head
        
        
        #Solution 1
        if not head:
            return None
        dummy1 = root1 = ListNode(0)
        dummy2 = root2 = ListNode(0)
        count = 1
        while head:
            if count % 2 == 1:
                root1.next = head
                root1 = root1.next
            if count % 2 == 0:
                root2.next = head
                root2 = root2.next
            count += 1
            head = head.next
        root2.next = None
        root1.next = dummy2.next
        return dummy1.next

        