'''
Question: 
  102. Binary Tree Level Order Traversal

Descrition: 
  Given a binary tree, return the level order traversal of its nodes' values. 
  (ie, from left to right, level by level).

Examples:

  1.Input: Given binary tree [3,9,20,null,null,15,7],
	    3
	   / \
	  9  20
	    /  \
	   15   7
  Output: 
	  [
	  	[3],
	  	[9,20],
	  	[15,7]
	  ]
'''

#Python3 Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        #Solution
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            vals = [node.val for node in stack]
            ans.append(vals)
            stack = [kid for node in stack for kid in (node.left, node.right) if kid]
        return ans  

        