'''
Question: 
  105. Construct Binary Tree from Preorder and Inorder Traversal

Descrition: 
  Given preorder and inorder traversal of a tree, construct the binary tree.

  Note:
  You may assume that duplicates do not exist in the tree.

Examples:
  preorder = [3,9,20,15,7]
  inorder = [9,3,15,20,7]

    3
   / \
  9  20
    /  \
   15   7
'''

#Python3 Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        #Solution
        if not preorder or not inorder:
            return None
        rootVal = preorder.pop(0)
        root = TreeNode(rootVal)
        inorderIndex = inorder.index(rootVal)
        root.left = self.buildTree(preorder, inorder[:inorderIndex])
        root.right = self.buildTree(preorder, inorder[inorderIndex + 1:])
        return root

        