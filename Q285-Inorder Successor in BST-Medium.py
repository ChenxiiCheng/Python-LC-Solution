'''
Question: 
  285. Inorder Successor in BST

Descrition: 
  Given a binary search tree and a node in it, find the in-order successor of that node in the BST.

  The successor of a node p is the node with the smallest key greater than p.val.

Examples:
  1.Input: root = [2,1,3], p = 1
    Output: 2
    Explanation: 1's in-order successor node is 2. Note that both p and the return value is of TreeNode type.

  2.Input: root = [5,3,6,2,4,null,null,1], p = 6
    Output: null
    Explanation: There is no in-order successor of the current node, so the answer is null.
'''

#Python3 Code:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """  
        #Solution 2
        if not root: 
            return None
        if p.val < root.val: 
            return self.inorderSuccessor(root.left, p) or root 
        return self.inorderSuccessor(root.right, p)
        
        
        #Solution
        #The inorder traversal of a BST is the nodes in ascending order. 
        #To find a successor, you just need to find the 
        #smallest one that is larger than the given value 
        #since there are no duplicate values in a BST.
        succ = None
        while root:
            if p.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ

        