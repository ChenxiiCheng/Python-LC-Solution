'''
Question: 
  12. Integer to Roman

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

	For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

	Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

	I can be placed before V (5) and X (10) to make 4 and 9. 
	X can be placed before L (50) and C (100) to make 40 and 90. 
	C can be placed before D (500) and M (1000) to make 400 and 900.
	Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.
Examples:
	1.Input: 3
	  Output: "III"

	2.Input: 9
      Output: "IX"

    3.Input: 58
	  Output: "LVIII"
      Explanation: L = 50, V = 5, III = 3.
'''

#Python3 Code:

class Solution:
    def intToRoman(self, num: int) -> str:
        #Solution 2
        lis = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        ans = ''
        for i, j in enumerate(nums):
            while num >= j:
                ans += lis[i]
                num -= j
            if num == 0:
                return ans
        
        
        #Solution
        lis = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
        nums = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        result = ''
        for letter, n in zip(lis, nums):
            result += letter * (num // n)
            num %= n
        return result

        