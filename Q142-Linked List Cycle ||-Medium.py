'''
Question: 
  142. Linked List Cycle II

Descrition: 
   Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
   To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. 
   If pos is -1, then there is no cycle in the linked list. Note: Do not modify the linked list.

Example:

  1.Input: head = [3,2,0,-4], pos = 1
	Output: tail connects to node index 1
	Explanation: There is a cycle in the linked list, where tail connects to the second node.

  2.Input: head = [1,2], pos = 0
	Output: tail connects to node index 0
	Explanation: There is a cycle in the linked list, where tail connects to the first node.

  3.Input: head = [1], pos = -1
	Output: no cycle
	Explanation: There is no cycle in the linked list.
'''

#Python code

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #Solution
        #https://www.cnblogs.com/zuoyuan/p/3701877.html
        #解题思路：这道题有点意思。首先使用快慢指针技巧，如果fast指针和slow指针相遇，则说明链表存在环路。
        #在fast指针和slow指针相遇后，fast指针不动，slow指针回到head，然后slow指针和fast指针同时向前走，
        #只不过这一次两个指针都是一步一步向前走。两个指针相遇的节点就是环路的起点。
        #原理说明：图中，head到环路起点的距离为K，起点到fast和slow的相遇点的距离为M，环路周长为L。
        #假设，在fast和slow相遇时，fast走过了Lfast，slow走过了Lslow。根据题意：
        #Lslow = K + M；Lfast = K + M + n * L（n为正整数）Lfast = 2 * Lslow
        #可以推出：Lslow=n*L；K=n*L-M，则当slow重新回到head，而fast还在相遇点，slow和fast都向前走，且每次走一个节点。
        #则slow从head走到起点走了K，而fast从相遇点出发也走了K，而fast向前走了距离K后到了哪里呢？由于K=（n-1）*L+（L-M），         #所以fast转了n-1圈，再走L-M，也到了起点。这样起点就找到了。
        if head == None or head.next == None:
            return None
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                break
        if slow == fast:
            slow = head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
        return None

        