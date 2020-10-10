#
# @lc app=leetcode id=1032 lang=python3
#
# [1032] Stream of Characters
#
# https://leetcode.com/problems/stream-of-characters/description/
#
# algorithms
# Hard (46.21%)
# Likes:    242
# Dislikes: 51
# Total Accepted:    14.4K
# Total Submissions: 31.2K
# Testcase Example:  '["StreamChecker","query","query","query","query","query","query","query","query","query","query","query","query"]\n' + '[[["cd","f","kl"]],["a"],["b"],["c"],["d"],["e"],["f"],["g"],["h"],["i"],["j"],["k"],["l"]]'
#
# Implement the StreamChecker class as follows:
# 
# 
# StreamChecker(words): Constructor, init the data structure with the given
# words.
# query(letter): returns true if and only if for some k >= 1, the last k
# characters queried (in order from oldest to newest, including this letter
# just queried) spell one of the words in the given list.
# 
# 
# 
# 
# Example:
# 
# 
# StreamChecker streamChecker = new StreamChecker(["cd","f","kl"]); // init the
# dictionary.
# streamChecker.query('a');          // return false
# streamChecker.query('b');          // return false
# streamChecker.query('c');          // return false
# streamChecker.query('d');          // return true, because 'cd' is in the
# wordlist
# streamChecker.query('e');          // return false
# streamChecker.query('f');          // return true, because 'f' is in the
# wordlist
# streamChecker.query('g');          // return false
# streamChecker.query('h');          // return false
# streamChecker.query('i');          // return false
# streamChecker.query('j');          // return false
# streamChecker.query('k');          // return false
# streamChecker.query('l');          // return true, because 'kl' is in the
# wordlist
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= words.length <= 2000
# 1 <= words[i].length <= 2000
# Words will only consist of lowercase English letters.
# Queries will only consist of lowercase English letters.
# The number of queries is at most 40000.
# 
# 
#

# @lc code=start
from collections import defaultdict
from functools import reduce

class StreamChecker:

    def __init__(self, words: List[str]):
        # O(N x M)

        # self.s = ""
        # self.dic = defaultdict(set)
        # for w in words:
        #     self.dic[w[-1]].add(w)

        # Trie = lambda: defaultdict(Trie)
        # self.trie = Trie()
        # for word in words:
        #     reduce(dict.__getitem__, word, self.trie)['#'] = True
        # self.waiting = []


        Trie = lambda: defaultdict(Trie)
        self.trie = Trie()
        for word in words:
            reduce(dict.__getitem__, word[::-1], self.trie)['#'] = True
        self.S = ""
        self.W = max(map(len, words))

        

    def query(self, letter: str) -> bool:
        # O(M) where M is a max word length.

        # self.s += letter
        # return any(self.s.endswith(w) for w in self.dic[letter])

        # self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        # return any('#' in node for node in self.waiting)

        self.S = (letter + self.S)[:self.W]
        cur = self.trie
        for c in self.S:
            if c in cur:
                cur = cur[c]
                if cur['#']:
                    return True
            else:
                break
        return False
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
# @lc code=end

