'''
Question: 
  13. Roman to Integer

Descrition: 
  Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol       Value
	I             1
	V             5
	X             10
	L             50
	C             100
	D             500
	M             1000

  For example, two is written as II in Roman numeral, just two one's added together. 
  Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

  Roman numerals are usually written largest to smallest from left to right. 
  However, the numeral for four is not IIII. Instead, the number four is written as IV. 
  Because the one is before the five we subtract it making four. The same principle applies to the number nine, 
  which is written as IX. There are six instances where subtraction is used:

  I can be placed before V (5) and X (10) to make 4 and 9. 
  X can be placed before L (50) and C (100) to make 40 and 90. 
  C can be placed before D (500) and M (1000) to make 400 and 900.
  Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Examples:
  1.Input: "III"
    Output: 3

  2.Input: "IV"
    Output: 4

  3.Input: "IX"
    Output: 9

  4.Input: "LVIII"
    Output: 58
    Explanation: L = 50, V= 5, III = 3.
'''

#Python3 Code:

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Solution 3
        roman = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        ans = 0
        for i in range(len(s) - 1):
            if roman[s[i]] < roman[s[i + 1]]:
                ans -= roman[s[i]]
            else:
                ans += roman[s[i]]
        return ans + roman[s[-1]]
        
        
        #Solution 2
        #仅考虑相邻的罗马数字的大小情况。对于输入的罗马数字字符串，从后向前扫描，
        #遇到前面数大于等于后面数的时候，相加；
        #遇到前面数小于后面数的时候，相减。（该思路也可以从前向后扫描）
        #因为前面的数索引是i-1，所以range里是(, 0, -1)
        dic = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = dic[s[-1]]  #dic[s[len(s) - 1]]都行
        for i in range(len(s) -1, 0, -1):
            cur = dic[s[i]]
            pre = dic[s[i - 1]]
            ans += pre if pre >= cur else -pre
        return ans
        
        
        #Solution
        #罗马数字采用七个罗马字母作数字： 
        #I（1）、X（10）、C（100）、M（1000）、V（5）、L（50）、D（500）。
        # 记数的方法： 
        # 1. 相同的数字连写，所表示的数等于这些数字相加得到的数，如 III=3； 
        # 2. 小的数字在大的数字的右边，所表示的数等于这些数字相加得到的数，如 VIII=8、XIII=12； 
        # 3. 小的数字（限于 I、X 和 C）在大的数字的左边，所表示的数等于大数减小数得到的数，如 IV=4、IX=9； 
        # 4. 在一个数的上面画一条横线，表示这个数增值 1,000 倍。
        
        #根据上面说的计数方法的前三条。对于输入的罗马数字字符串，从后向前扫描，
        #遇到前面数大于等于后面的最大数的时候，相加；遇到前面数小于后面的最大数的时候，相减。
        digits = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        ans = 0
        maxDigit = 1
        for i in range(len(s) - 1, -1, -1):
            if digits[s[i]] >= maxDigit:
                maxDigit = digits[s[i]]
                ans += digits[s[i]]
            else:
                ans -= digits[s[i]]
        return ans

        