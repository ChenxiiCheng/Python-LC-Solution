'''
Question: 
  387. First Unique Character in a String

Descrition: 
  Given a string, find the first non-repeating character in it and return it's index. 
  If it doesn't exist, return -1.

Examples:

  1.s = "leetcode"
    return 0.

  1.s = "loveleetcode",
    return 2.
'''

#Python3 Code:

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Solution
        if not s:
            return -1
        dic = {}
        for i in s:
            dic[i] = dic.get(i, 0) + 1
        for i in range(len(s)):
            ch = s[i]
            if dic[ch] == 1:
                return i
        return -1

        