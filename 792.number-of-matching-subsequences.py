#
# @lc app=leetcode id=792 lang=python3
#
# [792] Number of Matching Subsequences
#
# https://leetcode.com/problems/number-of-matching-subsequences/description/
#
# algorithms
# Medium (44.20%)
# Likes:    536
# Dislikes: 42
# Total Accepted:    24.2K
# Total Submissions: 54.5K
# Testcase Example:  '"abcde"\n["a","bb","acd","ace"]'
#
# Given string S and a dictionary of words words, find the number of words[i]
# that is a subsequence of S.
# 
# 
# Example :
# Input: 
# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
# Output: 3
# Explanation: There are three words in words that are a subsequence of S: "a",
# "acd", "ace".
# 
# 
# Note:
# 
# 
# All words in words and S will only consists of lowercase letters.
# The length of S will be in the range of [1, 50000].
# The length of words will be in the range of [1, 5000].
# The length of words[i] will be in the range of [1, 50].
# 
# 
#
from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        # Brute Force
        # Time  complexity: O(words.length x S.length + sum(words[i].length))
        # For each word, our subseq check on word words[i] may take time compolexity
        # O(S.length + words[i].length)
        # Space complexity: O(1)
        # def subseq(word):
        #     it = iter(S)
        #     return all(x in it for x in word)

        # return sum(subseq(word) for word in words)


        # Next Letter Pointers
        # Time  complexity: O(S.length + sum(words[i].length))
        # Space complexity: O(words.length)
        # ans, heads = 0, [[] for _ in range(26)]
        # for word in words:
        #     it = iter(word)
        #     heads[ord(next(it)) - ord('a')].append(it)

        # for letter in S:
        #     letter_index = ord(letter) - ord('a')
        #     old_bucket = heads[letter_index]
        #     heads[letter_index] = []

        #     while old_bucket:
        #         it = old_bucket.pop()
        #         nxt = next(it, None)
        #         if nxt:
        #             heads[ord(nxt) - ord('a')].append(it)
        #         else:
        #             ans += 1

        # return ans

        
        waiting = defaultdict(list)

        # for word in words:
        #     waiting[word[0]].append(iter(word[1:]))

        for it in map(iter, words):
            waiting[next(it)].append(it)

        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)

        return len(waiting[None])

