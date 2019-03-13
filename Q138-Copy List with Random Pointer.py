'''
Question: 
  138. Copy List with Random Pointer

Descrition: 
  A linked list is given such that each node contains an additional random pointer 
  which could point to any node in the list or null. Return a deep copy of the list.

Examples:
  Input:
  {"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},"random":{"$ref":"2"},"val":1}

Explanation:
  Node 1's value is 1, both of its next and random pointer points to Node 2.
  Node 2's value is 2, its next pointer points to null and its random pointer points to itself.
'''

#Python3 Code:

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        #Solution
        if not head:
            return
        cur, dic = head, {}
        while cur:
            dic[cur] = Node(cur.val, None, None)
            cur = cur.next
        cur = head
        while cur:
            if cur.random:
                dic[cur].random = dic[cur.random]
            if cur.next:
                dic[cur].next = dic[cur.next]
            cur = cur.next
        return dic[head]

