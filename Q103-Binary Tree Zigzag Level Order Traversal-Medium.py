'''
Question: 
  103. Binary Tree Zigzag Level Order Traversal
  website: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

Descrition: 
  Given a binary tree, return the zigzag level order traversal of its nodes' values. 
  (ie, from left to right, then right to left for the next level and alternate between).

Examples:

  Given binary tree [3,9,20,null,null,15,7],
  output => [[3],[20,9],[15,7]]
'''

#Python3 Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #Solution
        if not root:
            return []
        reverse = False
        stack = [root]
        ans = []
        while stack:
            vals = [node.val for node in stack]
            if reverse:
                vals = vals[::-1]
            ans.append(vals)
            stack = [kid for node in stack for kid in (node.left, node.right) if kid]
            reverse = not reverse
        return ans

