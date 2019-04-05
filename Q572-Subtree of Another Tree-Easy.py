'''
Question: 
  572. Subtree of Another Tree

Descrition: 
   Given two non-empty binary trees s and t, check whether tree t has exactly the same structure and node values with a subtree of s. 
   A subtree of s is a tree consists of a node in s and all of this node's descendants. The tree s could also be considered as a subtree of itself.

Example:

    Example1:
		Given tree s:

		     3
		    / \
		   4   5
		  / \
		 1   2

		Given tree t:
		   4 
		  / \
		 1   2
		Return true, because t has the same structure and node values with a subtree of s.

	Example 2:
		Given tree s:

		     3
		    / \
		   4   5
		  / \
		 1   2
		    /
		   0
		Given tree t:
		   4
		  / \
		 1   2
		Return false.
'''

#Python code

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        #Solutionn
        if not s: 
            return False
        if self.isSameTree(s, t): 
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

        