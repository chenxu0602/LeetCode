#
# @lc app=leetcode id=821 lang=python3
#
# [821] Shortest Distance to a Character
#
# https://leetcode.com/problems/shortest-distance-to-a-character/description/
#
# algorithms
# Easy (64.02%)
# Likes:    680
# Dislikes: 59
# Total Accepted:    43.8K
# Total Submissions: 68.2K
# Testcase Example:  '"loveleetcode"\n"e"'
#
# Given a string S and a character C, return an array of integers representing
# the shortest distance from the character C in the string.
# 
# Example 1:
# 
# 
# Input: S = "loveleetcode", C = 'e'
# Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
# 
# 
# 
# 
# Note:
# 
# 
# S string length is in [1, 10000].
# C is a single character, and guaranteed to be in string S.
# All letters in S and C are lowercase.
# 
# 
#
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        # O(N)
        prev = float("-inf")
        ans = []
        for i, x in enumerate(S):
            if x == C:
                prev = i
            ans.append(i - prev)

        prev = float("inf")
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            ans[i] = min(ans[i], prev - i)

        return ans
        

