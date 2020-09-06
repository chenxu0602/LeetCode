#
# @lc app=leetcode id=809 lang=python3
#
# [809] Expressive Words
#
# https://leetcode.com/problems/expressive-words/description/
#
# algorithms
# Medium (44.16%)
# Likes:    126
# Dislikes: 394
# Total Accepted:    16.8K
# Total Submissions: 37.9K
# Testcase Example:  '"heeellooo"\n["hello", "hi", "helo"]'
#
# Sometimes people repeat letters to represent extra feeling, such as "hello"
# -> "heeellooo", "hi" -> "hiiii".  In these strings like "heeellooo", we have
# groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".
# 
# For some given string S, a query word is stretchy if it can be made to be
# equal to S by any number of applications of the following extension
# operation: choose a group consisting of characters c, and add some number of
# characters c to the group so that the size of the group is 3 or more.
# 
# For example, starting with "hello", we could do an extension on the group "o"
# to get "hellooo", but we cannot get "helloo" since the group "oo" has size
# less than 3.  Also, we could do another extension like "ll" -> "lllll" to get
# "helllllooo".  If S = "helllllooo", then the query word "hello" would be
# stretchy because of these two extension operations: query = "hello" ->
# "hellooo" -> "helllllooo" = S.
# 
# Given a list of query words, return the number of words that are
# stretchy. 
# 
# 
# 
# 
# Example:
# Input: 
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1
# Explanation: 
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size
# 3 or more.
# 
# 
# 
# 
# Notes: 
# 
# 
# 0 <= len(S) <= 100.
# 0 <= len(words) <= 100.
# 0 <= len(words[i]) <= 100.
# S and all words in words consist only of lowercase letters
# 
# 
# 
# 
#
import itertools

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        # Time  complexity: O(QK), where Q is the length of words and K is the maximum length of a word.
        # Space complexity: O(K)
        if not S: return 0

        def RLE(S):
            return zip(*([(k, len(list(grp))) for k, grp in itertools.groupby(S)]))

        R, count = RLE(S) 
        ans = 0
        for word in words:
            R2, count2 = RLE(word)
            if R2 != R: continue
            ans += all(c1 >= max(c2, 3) or c1 == c2 for c1, c2 in zip(count, count2))

        return ans
        

