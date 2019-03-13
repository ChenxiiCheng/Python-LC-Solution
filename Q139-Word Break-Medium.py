'''
Question: 
  139. Word Break

Descrition: 
  Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, 
  determine if s can be segmented into a space-separated sequence of one or more dictionary words.

  Note:
  The same word in the dictionary may be reused multiple times in the segmentation.
  You may assume the dictionary does not contain duplicate words.

Examples:

  1.Input: s = "leetcode", wordDict = ["leet", "code"]
  Output: true
  Explanation: Return true because "leetcode" can be segmented as "leet code".

  2.Input: s = "applepenapple", wordDict = ["apple", "pen"]
  Output: true
  Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
'''

#Python3 Code:

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        #Solution
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(n):
            if dp[i]:
                for j in wordDict:
                    l = len(j)
                    if i + l <= n and s[i:i + l] == j:
                        dp[i + l] = True
        return dp[n]

