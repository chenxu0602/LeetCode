#
# @lc app=leetcode id=1638 lang=python3
#
# [1638] Count Substrings That Differ by One Character
#
# https://leetcode.com/problems/count-substrings-that-differ-by-one-character/description/
#
# algorithms
# Medium (66.99%)
# Likes:    96
# Dislikes: 71
# Total Accepted:    4.8K
# Total Submissions: 7.2K
# Testcase Example:  '"aba"\n"baba"'
#
# Given two strings s and t, find the number of ways you can choose a non-empty
# substring of s and replace a single character by a different character such
# that the resulting substring is a substring of t. In other words, find the
# number of substrings in s that differ from some substring in t by exactly one
# character.
# 
# For example, the underlined substrings in "computer" and "computation" only
# differ by the 'e'/'a', so this is a valid way.
# 
# Return the number of substrings that satisfy the condition above.
# 
# A substring is a contiguous sequence of characters within a string.
# 
# 
# Example 1:
# 
# 
# Input: s = "aba", t = "baba"
# Output: 6
# Explanation: The following are the pairs of substrings from s and t that
# differ by exactly 1 character:
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# ("aba", "baba")
# The underlined portions are the substrings that are chosen from s and t.
# 
# ​​Example 2:
# 
# 
# Input: s = "ab", t = "bb"
# Output: 3
# Explanation: The following are the pairs of substrings from s and t that
# differ by 1 character:
# ("ab", "bb")
# ("ab", "bb")
# ("ab", "bb")
# ​​​​The underlined portions are the substrings that are chosen from s and t.
# 
# Example 3:
# 
# 
# Input: s = "a", t = "a"
# Output: 0
# 
# 
# Example 4:
# 
# 
# Input: s = "abe", t = "bbc"
# Output: 10
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 100
# s and t consist of lowercase English letters only.
# 
# 
#

# @lc code=start
class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        # Time  complexity: O(n^3)
        # Space complexity: O(1)
        # res = 0
        # for i in range(len(s)):
        #     for j in range(len(t)):
        #         miss = pos = 0
        #         while i + pos < len(s) and j + pos < len(t) and miss < 2:
        #             miss += s[i + pos] != t[j + pos]
        #             res += miss == 1
        #             pos += 1
        # return res


        # Time  complexity: O(mn)
        # Space complexity: O(1)
        def test(i, j):
            res = pre = cur = 0
            for k in range(min(m - i, n - j)):
                cur += 1
                if s[i + k] != t[j + k]:
                    pre, cur = cur, 0
                res += pre
            return res

        m, n = map(len, (s, t))
        return sum(test(i, 0) for i in range(m)) + sum(test(0, j) for j in range(1, m))
        
# @lc code=end

