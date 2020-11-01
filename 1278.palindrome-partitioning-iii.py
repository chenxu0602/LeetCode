#
# @lc app=leetcode id=1278 lang=python3
#
# [1278] Palindrome Partitioning III
#
# https://leetcode.com/problems/palindrome-partitioning-iii/description/
#
# algorithms
# Hard (57.54%)
# Likes:    146
# Dislikes: 2
# Total Accepted:    4.6K
# Total Submissions: 8.1K
# Testcase Example:  '"abc"\n2'
#
# You are given a string s containing lowercase letters and an integer k. You
# need to :
# 
# 
# First, change some characters of s to other lowercase English letters.
# Then divide s into k non-empty disjoint substrings such that each substring
# is palindrome.
# 
# 
# Return the minimal number of characters that you need to change to divide the
# string.
# 
# 
# Example 1:
# 
# 
# Input: s = "abc", k = 2
# Output: 1
# Explanation: You can split the string into "ab" and "c", and change 1
# character in "ab" to make it palindrome.
# 
# 
# Example 2:
# 
# 
# Input: s = "aabbc", k = 3
# Output: 0
# Explanation: You can split the string into "aa", "bb" and "c", all of them
# are palindrome.
# 
# Example 3:
# 
# 
# Input: s = "leetcode", k = 8
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= s.length <= 100.
# s only contains lowercase English letters.
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def num_change(w):
            return sum(a != b for a, b in zip(w, w[::-1])) // 2

        @lru_cache(None)
        def dp(i, k):
            if k == 1:
                return num_change(s[:i + 1])
            else:
                return min(dp(j, k - 1) + num_change(s[j + 1:i + 1]) for j in range(k - 2, i))

        return dp(len(s) - 1, k)
        
# @lc code=end

