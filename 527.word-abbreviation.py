#
# @lc app=leetcode id=527 lang=python3
#
# [527] Word Abbreviation
#
# https://leetcode.com/problems/word-abbreviation/description/
#
# algorithms
# Hard (50.56%)
# Likes:    149
# Dislikes: 95
# Total Accepted:    12K
# Total Submissions: 23.6K
# Testcase Example:  '["like","god","internal","me","internet","interval","intension","face","intrusion"]'
#
# Given an array of n distinct non-empty strings, you need to generate minimal
# possible abbreviations for every word following rules below.
# 
# 
# Begin with the first character and then the number of characters abbreviated,
# which followed by the last character.
# If there are any conflict, that is more than one words share the same
# abbreviation, a longer prefix is used instead of only the first character
# until making the map from word to abbreviation become unique. In other words,
# a final abbreviation cannot map to more than one original words.
# ⁠If the abbreviation doesn't make the word shorter, then keep it as
# original.
# 
# 
# Example:
# 
# Input: ["like", "god", "internal", "me", "internet", "interval", "intension",
# "face", "intrusion"]
# Output:
# ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
# 
# 
# 
# 
# Note: 
# 
# ⁠Both n and the length of each word will not exceed 400.
# ⁠The length of each word is greater than 1.
# ⁠The words consist of lowercase English letters only.
# ⁠The return answers should be in the same order as the original array.
# 
#
from collections import defaultdict

class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        """
        def abbrev(word, i = 0):
            if (len(word) - i <= 3):
                return word
            return word[:i+1] + str(len(word) - i -2) + word[-1]

        N = len(dict)
        ans = list(map(abbrev, dict))
        prefix = [0] * N

        for i in range(N):
            while True:
                dupes = set()
                for j in range(i+1, N):
                    if ans[i] == ans[j]:
                        dupes.add(j)

                if not dupes: break
                dupes.add(i)
                for k in dupes:
                    prefix[k] += 1
                    ans[k] = abbrev(dict[k], prefix[k])

        return ans
        """

        """
        def longest_common_prefix(a, b):
            i = 0
            while i < len(a) and i < len(b) and a[i] == b[i]:
                i += 1
            return i

        ans = [None for _ in dict]

        groups = defaultdict(list)

        for index, word in enumerate(dict):
            groups[len(word), word[0], word[-1]].append((word, index))

        for (size, first, last), enum_words in groups.items():
            enum_words.sort()
            lcp = [0] * len(enum_words)
            for i, (word, _) in enumerate(enum_words):
                if i:
                    word2 = enum_words[i-1][0]
                    lcp[i] = longest_common_prefix(word, word2)
                    lcp[i-1] = max(lcp[i-1], lcp[i])

            for (word, index), p in zip(enum_words, lcp):
                delta = size - 2 - p
                if delta <= 1:
                    ans[index] = word
                else:
                    ans[index] = word[:p+1] + str(delta) + last

        return ans
        """

        groups = defaultdict(list)
        for index, word in enumerate(dict):
            groups[len(word), word[0], word[-1]].append((word, index))

        ans = [None] * len(dict)
        Trie = lambda: defaultdict(Trie)
        COUNT = False
        for group in groups.values():
            trie = Trie()
            for word, _ in group:
                cur = trie
                for letter in word[1:]:
                    cur[COUNT] = cur.get(COUNT, 0) + 1
                    cur = cur[letter]

            for word, index in group:
                cur = trie
                for i, letter in enumerate(word[1:], 1):
                    if cur[COUNT] == 1: break
                    cur = cur[letter]
                if len(word) - i - 1 > 1:
                    ans[index] = word[:i] + str(len(word)-i-1) + word[-1]
                else:
                    ans[index] = word
        return ans
        

