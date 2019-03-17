'''
Question: 
  71. Simplify Path

Descrition: 
  Given an absolute path for a file (Unix-style), simplify it. Or in other words, convert it to the canonical path.

  In a UNIX-style file system, a period . refers to the current directory. Furthermore, a double period .. moves the directory up a level. 
  For more information, see: Absolute path vs relative path in Linux/Unix

  Note that the returned canonical path must always begin with a slash /, and there must be only a single slash / between two directory names. 
  The last directory name (if it exists) must not end with a trailing /. Also, the canonical path must be the shortest string representing the absolute path.

Examples:

  1.Input: "/home//foo/"
    Output: "/home/foo"
    Explanation: In the canonical path, multiple consecutive slashes are replaced by a single one.

  2.Input: "/a/./b/../../c/"
    Output: "/c"

  3.Input: "/a//b////c/d//././/.."
    Output: "/a/b/c"
'''

#Python3 Code:

class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        #Solution
        if not path:
            return ''
        stack = []
        for token in path.split('/'):
            if token in ('', '.'):
                pass
            elif token == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(token)
        return '/' + '/'.join(stack)

        