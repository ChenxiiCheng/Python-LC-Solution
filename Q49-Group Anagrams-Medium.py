'''
Question: 
  49. Group Anagrams

Descrition: 
  Given an array of strings, group anagrams together.

Examples:

  Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
  Output:
		[
		  ["ate","eat","tea"],
		  ["nat","tan"],
		  ["bat"]
		]
'''

#Python3 Code:

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #Solution
        if not strs:
            return []
        dic = {}
        for ch in strs:
            c = ''.join(sorted(ch))
            if c not in dic:
                dic[c] = [ch]
            else:
                dic[c].append(ch)
        return [val for val in dic.values()]

        