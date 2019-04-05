'''
Question: 
  96. Unique Binary Search Trees

Descrition: 
   Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

	Input: 3
	Output: 5
	Explanation:
	Given n = 3, there are a total of 5 unique BST's:

	   1         3     3      2      1
	    \       /     /      / \      \
	     3     2     1      1   3      2
	    /     /       \                 \
	   2     1         2                 3
'''

#Python code

class Solution:
    def numTrees(self, n: int) -> int:
        #Solution 2
        if num == 0 or num == 1:
            return 1
        dp = [0 for i in range(num + 1)]
        dp[0]= 1
        for i in range(num):
            for j in range(i + 1):
                dp[i + 1] += dp[j]*dp[i - j]
        return dp[num]
        
        
        #Solution
        #看到题目首先是找规律，然后得出结论。
        #以n=6为例，6-1=(0+5)=(1+4)=(2+3)=(3+2)=(4+1)=(5+0), 分别代表父节点为1、2、3、4、5、6的情况下左右子树上的元素个数。
        #建立数组res[i]，存储整数i能组成的唯一搜索二叉树个数，便由排列组合得出关系式，如(4+1)=res[4]*res[1]，即此时父节点是5，
        #左子树有4个元素，能组成res[4]个不同的树；右子树有1个元素，能组成res[1]个不同的树。
        #因此n=6且父节点是5时能组成res[4]*res[1]种树，再以此类推父节点是其他值的情况。
        dp = [1, 1]
        for i in range(2, n + 1):
            count = 0
            for j in range(i):
                count += dp[j] * dp[i - j - 1]
            dp.append(count)
        return dp.pop()

        