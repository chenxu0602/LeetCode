#
# @lc app=leetcode id=472 lang=python3
#
# [472] Concatenated Words
#
# https://leetcode.com/problems/concatenated-words/description/
#
# algorithms
# Hard (35.27%)
# Likes:    266
# Dislikes: 67
# Total Accepted:    23.1K
# Total Submissions: 65.4K
# Testcase Example:  '["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]'
#
# Given a list of words (without duplicates), please write a program that
# returns all concatenated words in the given list of words.
# A concatenated word is defined as a string that is comprised entirely of at
# least two shorter words in the given array.
# 
# Example:
# 
# Input:
# ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]
# 
# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]
# 
# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats";
# "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; "ratcatdogcat"
# can be concatenated by "rat", "cat", "dog" and "cat".
# 
# 
# 
# Note:
# 
# The number of elements of the given array will not exceed 10,000 
# The length sum of elements in the given array will not exceed 600,000. 
# All the input string will only include lower case letters.
# The returned elements order does not matter. 
# 
# 
#
class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
#        s = {w for w in words if w}
#        f = lambda w: not w or any(w[:i+1] in s and f(w[i+1:]) for i in range(len(w), -1, -1)) 
#        return [w for w in sorted(s, key=len)[::-1] if s.discard(w) or f(w)]

        ret, s = [], {w for w in words if w}
        f = lambda w: not w or any(w[:i+1] in s and f(w[i+1:]) for i in range(len(w), -1, -1)) 
        for w in sorted(s, key=len, reverse=True):
            s.discard(w)
            if f(w):
                ret.append(w)

        return ret



