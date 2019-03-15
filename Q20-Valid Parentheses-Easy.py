'''
Question: 
  20. Valid Parentheses

Descrition: 
  Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
  determine if the input string is valid.

  An input string is valid if:

  Open brackets must be closed by the same type of brackets.
  Open brackets must be closed in the correct order.
  Note that an empty string is also considered valid.

Examples:

  1.Input: "()[]{}"
    Output: true

  2.Input: "([)]"
    Output: false
'''

#Python3 Code:

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #Solution 2
        if not s:
            return True
        dic = {')':'(', ']':'[', '}':'{'}
        stack = []
        for ch in s:
            if ch in dic.values():
                stack.append(ch)
            elif ch in dic.keys():
                if stack == [] or dic[ch] != stack.pop():
                    return False
            else:
                return 0
        return stack == []
        
        
        #Solution
        if not s:
            return True
        while '()' in s or '[]' in s or '{}' in s:
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        if s == '':
            return True
        return False

        