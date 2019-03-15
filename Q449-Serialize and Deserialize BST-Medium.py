'''
Question: 
  449. Serialize and Deserialize BST

Descrition: 
  Serialization is the process of converting a data structure or object into a sequence of bits 
  so that it can be stored in a file or memory buffer, or transmitted across a network connection 
  link to be reconstructed later in the same or another computer environment.
  Design an algorithm to serialize and deserialize a binary search tree. 
  There is no restriction on how your serialization/deserialization algorithm should work. 
  You just need to ensure that a binary search tree can be serialized to a string and 
  this string can be deserialized to the original tree structure.

  The encoded string should be as compact as possible.

  Note: Do not use class member/global/static variables to store states. 
  Your serialize and deserialize algorithms should be stateless.

'''

#Python Code:

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        #Solution
        stack = []
        ans = []
        while stack or root:
            if root:
                ans.append(str(root.val))
                stack.append(root)
                root = root.left
            else:
                node = stack.pop()
                root = node.right
        return ' '.join(ans) 
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = map(int, data.split(' '))
        dummy = root = TreeNode(data[0])
        stack = []
        for n in data[1:]:
            if n < root.val:
                root.left = TreeNode(n)
                stack.append(root)
                root = root.left
            else:
                while stack and stack[-1].val < n:
                    root = stack.pop()
                root.right = TreeNode(n)
                root = root.right
        return dummy
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))