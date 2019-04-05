'''
Question: 
  70. Climbing Stairs

Descrition: 
   You are climbing a stair case. It takes n steps to reach to the top. Each time you can either climb 1 or 2 steps. 
   In how many distinct ways can you climb to the top? Note: Given n will be a positive integer.

Example:

  1.Input: 2
	Output: 2
	Explanation: There are two ways to climb to the top.
	1. 1 step + 1 step
	2. 2 steps

  2.Input: 3
	Output: 3
	Explanation: There are three ways to climb to the top.
	1. 1 step + 1 step + 1 step
	2. 1 step + 2 steps
	3. 2 steps + 1 step
'''

#Python code
class Solution:
    def climbStairs(self, n: int) -> int:
        #Solution 2
        #当输入为1, 2, 3, 4, 5, 6, 7, 8, 9, 10时，
        #观察输出为1, 2, 3, 5, 8, 13, 21, 34, 55, 89，
        #是斐波那契数列！好了，我们找到了规律，写代码吧。
        pre = cur = 1
        for i in range(1, n):
            pre, cur = cur, pre + cur
        return cur
        
        
        #Solution
        #当n = 1时，有一种路径；当n=2时，有两种路径；当n=3时，有三种路径。
        #当n=4时，有五种，n=5时有八种。可见，n的当前项等于前两项相加之和。
        #应该把每项的值存放在list集合中，首先先对list集合的数值进行初始化，
        #对第一项和第二项赋值为1，从第三项开始的每一项都等于前两项相加之和。
        #最后，返回list集合中的最后一项。
        res = [0] * (n + 1)
        res[0], res[1] = 1, 1
        i = 2
        while i <= n:
            res[i] = res[i - 1] + res[i - 2]
            i += 1
        return res[-1]