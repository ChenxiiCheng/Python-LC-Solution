'''
Question: 
  5. Longest Palindromic Substring

Descrition: 
  Given a string s, find the longest palindromic substring in s. 
  You may assume that the maximum length of s is 1000.

Examples:
  Input: "babad"
  Output: "bab"
  Note: "aba" is also a valid answer.
'''

#Python3 Code:

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Solution
        if not s:
            return ''
        ans = ''
        for i in range(len(s)):
            tmp = self.helper(s, i, i)
            if len(tmp) > len(ans):
                ans = tmp
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(ans):
                ans = tmp
        return ans
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

        