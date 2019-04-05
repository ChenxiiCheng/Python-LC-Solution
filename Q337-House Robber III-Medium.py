'''
Question: 
  337. House Robber III

Descrition: 
   The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." 
   Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". 
   It will automatically contact the police if two directly-linked houses were broken into on the same night.
   Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example:

  1.Input: [3,2,3,null,3,null,1]

	     3
	    / \
	   2   3
	    \   \ 
	     3   1

	Output: 7 
	Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

  2.Input: [3,4,5,1,3,null,1]

	     3
	    / \
	   4   5
	  / \   \ 
	 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
'''

#Python code

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #Solution 3
        #Alternate between picking the children or the current node and the children's children.
        #ln = left node; lc = left children; rn = right node; rc = right children
        def dfs(node):
            ln, lc = dfs(node.left) if node.left else (0,0)
            rn, rc = dfs(node.right) if node.right else (0,0)
            return node.val + lc + rc, max(ln + rn, ln + rc, lc + rc, lc + rn)
        return max(dfs(root)) if root else 0
        
        
        #Solution 2
        #For each node, we either rob it or not. So the recursion returns two values: yes and no.
        #For parent yes, it is the sum of not robing left, not robing right, and the parent.val.
        #For parent no, it is max(left_yes, left_no) + max(right_yes, right_no) because we don't care 
        #whether to rob left or right since we are not robing the parent. 
        yes, no = self.dfs(root)
        return max(yes, no)
    
    def dfs(self, root):
        if root is None:
            return 0, 0
        left_yes, left_no = self.dfs(root.left)
        right_yes, right_no = self.dfs(root.right)
        
        root_yes = left_no + right_no + root.val
        root_no = max(left_yes, left_no) + max(right_yes, right_no)
        
        return root_yes, root_no
        
        
        #Solution
        dp = {}
        if not root:
            return 0
        def rob(root):  
            if not root:
                return 0
            if root in dp:
                return dp[root]
            gain = root.val
            child_gain = rob(root.left) + rob(root.right)
            if root.left:
                gain += rob(root.left.left) + rob(root.left.right)
            if root.right:
                gain += rob(root.right.left) + rob(root.right.right)
            dp[root] = max(gain, child_gain)
            return dp[root]
        return rob(root)

        