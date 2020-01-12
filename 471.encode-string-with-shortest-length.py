#
# @lc app=leetcode id=471 lang=python3
#
# [471] Encode String with Shortest Length
#
# https://leetcode.com/problems/encode-string-with-shortest-length/description/
#
# algorithms
# Hard (45.29%)
# Likes:    245
# Dislikes: 17
# Total Accepted:    12.7K
# Total Submissions: 28K
# Testcase Example:  '"aaa"'
#
# Given a non-empty string, encode the string such that its encoded length is
# the shortest.
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times.
# 
# Note:
# 
# 
# k will be a positive integer and encoded string will not be empty or have
# extra space.
# You may assume that the input string contains only lowercase English letters.
# The string's length is at most 160.
# If an encoding process does not make the string shorter, then do not encode
# it. If there are several solutions, return any of them is fine.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "aaa"
# Output: "aaa"
# Explanation: There is no way to encode it such that it is shorter than the
# input string, so we do not encode it.
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: "aaaaa"
# Output: "5[a]"
# Explanation: "5[a]" is shorter than "aaaaa" by 1 character.
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: "aaaaaaaaaa"
# Output: "10[a]"
# Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have
# the same length = 5, which is the same as "10[a]".
# 
# 
# 
# 
# Example 4:
# 
# 
# Input: "aabcaabcd"
# Output: "2[aabc]d"
# Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".
# 
# 
# 
# 
# Example 5:
# 
# 
# Input: "abbbabbbcabbbabbbc"
# Output: "2[2[abbb]c]"
# Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to
# "2[abbb]c", so one answer can be "2[2[abbb]c]".
# 
# 
# 
# 
#

from functools import lru_cache

class Solution:
    def encode2(self, s, memo={}):
        if s not in memo:
            n = len(s)
            i = (s + s).find(s, 1)
            one = f"{n//i}[{self.encode2(s[:i])}]" if i < n else s
            multi = [self.encode2(s[:i]) + self.encode2(s[i:]) for i in range(1 ,n)]
            memo[s] = min([s, one] + multi, key=len)

        return memo[s]

    def encode(self, s: str) -> str:
#        return self.encode2(s)

        @lru_cache(None)
        def dfs(s):
            n = len(s)
            i = (s + s).find(s, 1)
            one = f"{n//i}[{dfs(s[:i])}]" if i < n else s
            multi = [dfs(s[:i]) + dfs(s[i:]) for i in range(1, n)]
            return min([s, one] + multi, key=len)

        return dfs(s)
        

