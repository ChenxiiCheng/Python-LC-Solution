'''
Question: 
  3. Longest Substring Without Repeating Characters

Descrition: 
  Given a string, find the length of the longest substring without repeating characters.

Examples:
  1.Input: "abcabcbb"
    Output: 3 
    Explanation: The answer is "abc", with the length of 3.

  2.Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

  3.Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
'''

#Python3 Code:

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        #Soltuion 2
        dic, start, ans = {}, 0, 0
        for i in range(len(s)):
            if s[i] not in dic or dic[s[i]] < start:
                ans = max(ans, i - start + 1)
            else:
                start = dic[s[i]] + 1
            dic[s[i]] = i
        return ans
        
        
        #Solution
        dic, start, ans = {}, 0, 0
        for i, v in enumerate(s):
            if v in dic and start <= dic[v]:
                start = dic[v] + 1
            else:
                ans = max(ans, i - start + 1)
            dic[v] = i
        return ans

        