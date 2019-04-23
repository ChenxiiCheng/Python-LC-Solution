**Question**

102. Binary Tree Level Order Traversal

Given a binary tree, return the *level order* traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree `[3,9,20,null,null,15,7]`,

```
    3
   / \
  9  20
    /  \
   15   7
```



return its level order traversal as:

```
[
  [3],
  [9,20],
  [15,7]
]
```



**Solution**

```javascript
levelOrder = (root) => {
    let ans = [];
    helper(root, 0, ans);
    return ans;
};

helper = (node, level, res) => {
    if (!node) return;
    if (!res[level]) res[level] = [];
    res[level].push(node.val);
    helper(node.left, level + 1, res);
    helper(node.right, level + 1, res);
};
```

