'''
Question: 
  543. Diameter of Binary Tree

Descrition: 
  Given a binary tree, you need to compute the length of the diameter of the tree. 
  The diameter of a binary tree is the length of the longest path between any two nodes in a tree. 
  This path may or may not pass through the root.

Examples:
  Input:[1,2,3,4,5]
  Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
'''

#Python3 Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Solution
        self.ans = 0
        
        def depth(p):
            if not p: return 0
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left + right)
            return 1 + max(left, right)
        
        depth(root)
        return self.ans

        