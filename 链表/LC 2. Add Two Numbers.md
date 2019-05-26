## LC 2. Add Two Numbers

![image-20190526223529142](/Users/chenxi/Library/Application Support/typora-user-images/image-20190526223529142.png)



**Python3 Code**

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        #Solution
        if not l1 or not l2:
            return l1 or l2
        dummy = root = ListNode(0)
        add = 0
        while l1 or l2 or add:
            vals = (l1.val if l1 else 0) + (l2.val if l2 else 0) + add
            root.next = ListNode(vals % 10)
            add = vals // 10
            root = root.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
```

