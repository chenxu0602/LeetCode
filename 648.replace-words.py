#
# @lc app=leetcode id=648 lang=python3
#
# [648] Replace Words
#
# https://leetcode.com/problems/replace-words/description/
#
# algorithms
# Medium (52.39%)
# Likes:    469
# Dislikes: 112
# Total Accepted:    37.1K
# Total Submissions: 70.4K
# Testcase Example:  '["cat", "bat", "rat"]\n"the cattle was rattled by the battery"'
#
# In English, we have a concept called root, which can be followed by some
# other words to form another longer word - let's call this word successor. For
# example, the root an, followed by other, which can form another word
# another.
# 
# Now, given a dictionary consisting of many roots and a sentence. You need to
# replace all the successor in the sentence with the root forming it. If a
# successor has many roots can form it, replace it with the root with the
# shortest length.
# 
# You need to output the sentence after the replacement.
# 
# Example 1:
# 
# 
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"
# 
# 
# 
# 
# Note:
# 
# 
# The input will only have lower-case letters.
# 1 <= dict words number <= 1000
# 1 <= sentence words number <= 1000
# 1 <= root length <= 100
# 1 <= sentence words length <= 1000
# 
# 
# 
# 
#
from collections import defaultdict
from functools import reduce

class Solution:
    def replaceWords(self, roots: List[str], sentence: str) -> str:
        # Prefix Hash
        # Time  complexity: O(sum(w_i ^ 2)), where w_i is the length of the i-th word.
        # Space complexity: O(N)
        # rootset = set(roots)

        # def replace(word):
        #     for i in range(1, len(word)):
        #         if word[:i] in rootset:
        #             return word[:i]
        #     return word
        
        # return " ".join(map(replace, sentence.split()))


        # sentenceAsList = sentence.split(" ")
        # for i in range(len(sentenceAsList)):
        #     for j in roots:
        #         if sentenceAsList[i].startswith(j):
        #             sentenceAsList[i] = j
        # return " ".join(sentenceAsList)

        # Trie
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # suppose root = 'abc'
        # trie['a']['b']['c'][END] = 'abc'
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = True

        for root in roots:
            reduce(dict.__getitem__, root, trie)[END] = root

        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur:
                    break
                cur = cur[letter]
            return cur.get(END, word)

        return " ".join(map(replace, sentence.split()))



