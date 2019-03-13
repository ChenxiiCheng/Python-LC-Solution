'''
Question: 
  127. Word Ladder

Descrition: 
  Given two words (beginWord and endWord), and a dictionary's word list, 
  find the length of shortest transformation sequence from beginWord to endWord, such that:

  Only one letter can be changed at a time.
  Each transformed word must exist in the word list. 
  Note that beginWord is not a transformed word.
  
  Note:
  Return 0 if there is no such transformation sequence.
  All words have the same length.
  All words contain only lowercase alphabetic characters.
  You may assume no duplicates in the word list.
  You may assume beginWord and endWord are non-empty and are not the same.

Examples:

  1.Input:
  beginWord = "hit",
  endWord = "cog",
  wordList = ["hot","dot","dog","lot","log","cog"]
  
  Output: 5

  Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
  return its length 5.

  2.Input:
  beginWord = "hit"
  endWord = "cog"
  wordList = ["hot","dot","dog","lot","log"]

  Output: 0

  Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

#Python3 Code:

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        #Solution
        wordList = set(wordList)
        visited = set()
        alpha = string.ascii_lowercase
        q = collections.deque([(beginWord, 1)])
        while q:
            word, length = q.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for ch in alpha:
                    new_word = word[:i] + ch + word[i + 1:]
                    if new_word in wordList and new_word not in visited:
                        q.append((new_word, length + 1))
                        visited.add(new_word)
        return 0

