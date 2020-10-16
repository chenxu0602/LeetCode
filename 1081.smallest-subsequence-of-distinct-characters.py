#
# @lc app=leetcode id=1081 lang=python3
#
# [1081] Smallest Subsequence of Distinct Characters
#
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/description/
#
# algorithms
# Medium (50.07%)
# Likes:    510
# Dislikes: 73
# Total Accepted:    13.7K
# Total Submissions: 26.6K
# Testcase Example:  '"bcabc"'
#
# Return the lexicographically smallest subsequence of s that contains all the
# distinct characters of s exactly once.
# 
# Note: This question is the same as 316:
# https://leetcode.com/problems/remove-duplicate-letters/
# 
# 
# Example 1:
# 
# 
# Input: s = "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# 
# Input: s = "cbacdcbc"
# Output: "acdb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        last = {c: i for i, c in enumerate(s)}
        stack = []

        for i, c in enumerate(s):
            if c in stack: continue
            while stack and stack[-1] > c and i < last[stack[-1]]:
                stack.pop()
            stack.append(c)

        return "".join(stack)
        
# @lc code=end

