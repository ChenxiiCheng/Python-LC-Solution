'''
Question: 
  211. Add and Search Word - Data structure design

Descrition: 
  Design a data structure that supports the following two operations:

  void addWord(word)
  bool search(word)
  search(word) can search a literal word or a regular expression string containing only letters 
  a-z or .. A . means it can represent any one letter.

Examples:
  addWord("bad")
  addWord("dad")
  addWord("mad")
  search("pad") -> false
  search("bad") -> true
  search(".ad") -> true
  search("b..") -> true
'''

#Python3 Code:

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        #Solution
        self.wordDict = collections.defaultdict(list)
        

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        if len(word) in self.wordDict:
            self.wordDict[len(word)].append(word)
        else:
            self.wordDict[len(word)] = [word]
        

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if word == None:
            return False
        if '.' not in word:
            return word in self.wordDict[len(word)]
        for v in self.wordDict[len(word)]:
            for i, ch in enumerate(word):
                if v[i] != ch and ch != '.':
                    break
            else:
                return True
        return False
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)