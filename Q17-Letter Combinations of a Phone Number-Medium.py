'''
Question: 
  17. Letter Combinations of a Phone Number

Descrition: 
  Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

  A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Examples:
  Input: "23"
  Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
'''

#Python3 Code:

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #Solution
        if not digits:
            return []
        dic = {'1':'','2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        ans = ['']
        for digit in digits:
            tmp = []
            lis = dic[digit]
            for st in ans:
                for ch in lis:
                    tmp.append(st + ch)
            ans = tmp
        return ans

        