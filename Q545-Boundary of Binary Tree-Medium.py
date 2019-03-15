'''
Question: 
  545. Boundary of Binary Tree

Descrition: 
  Given a binary tree, return the values of its boundary in anti-clockwise direction starting from root. 
  Boundary includes left boundary, leaves, and right boundary in order without duplicate nodes.
  Left boundary is defined as the path from root to the left-most node. 
  Right boundary is defined as the path from root to the right-most node. 
  If the root doesn't have left subtree or right subtree, then the root itself is left boundary or right boundary. 
  Note this definition only applies to the input binary tree, and not applies to any subtrees.

  The left-most node is defined as a leaf node you could reach when you always firstly travel to the left subtree if exists. 
  If not, travel to the right subtree. Repeat until you reach a leaf node.

  The right-most node is also defined by the same way with left and right exchanged.

Examples:

	1.output:[1, 3, 4, 2]

	Explanation:
	The root doesn't have left subtree, so the root itself is left boundary.
	The leaves are node 3 and 4.
	The right boundary are node 1,2,4. Note the anti-clockwise direction means you should output reversed right boundary.
	So order them in anti-clockwise without duplicates and we have [1,3,4,2].
'''

#Python3 Code:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        # in the dfs steps to help decide when to add node
        # values to the boundary array.
        if not root: return []
        boundary = [root.val]
        def dfs(root, isleft, isright):
            if root:
                # append when going down from the left or at leaf node
                if (not root.left and not root.right) or isleft:
                    boundary.append(root.val)

                if root.left and root.right:
                    dfs(root.left, isleft, False)
                    dfs(root.right, False, isright)
                else:
                    dfs(root.left,  isleft, isright)
                    dfs(root.right, isleft, isright)

                # append to boundary when coming up from the right
                if (root.left or root.right) and isright:
                    boundary.append(root.val)

        dfs(root.left, True, False)
        dfs(root.right, False, True)
        return boundary

        