#
# @lc app=leetcode id=1593 lang=python3
#
# [1593] Split a String Into the Max Number of Unique Substrings
#
# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/
#
# algorithms
# Medium (46.86%)
# Likes:    229
# Dislikes: 11
# Total Accepted:    9.6K
# Total Submissions: 20.4K
# Testcase Example:  '"ababccc"'
#
# Given a string s, return the maximum number of unique substrings that the
# given string can be split into.
# 
# You can split string s into any list of non-empty substrings, where the
# concatenation of the substrings forms the original string. However, you must
# split the substrings such that all of them are unique.
# 
# A substring is a contiguous sequence of characters within a string.
# 
# 
# Example 1:
# 
# 
# Input: s = "ababccc"
# Output: 5
# Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc'].
# Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a'
# and 'b' multiple times.
# 
# 
# Example 2:
# 
# 
# Input: s = "aba"
# Output: 2
# Explanation: One way to split maximally is ['a', 'ba'].
# 
# 
# Example 3:
# 
# 
# Input: s = "aa"
# Output: 1
# Explanation: It is impossible to split the string any further.
# 
# 
# 
# Constraints:
# 
# 
# 
# 1 <= s.length <= 16
# 
# 
# s contains only lower case English letters.
# 
# 
# 
#

# @lc code=start
class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        def dfs(s, seen):
            ans = 0
            if s:
                for i in range(1, len(s) + 1):
                    candidate = s[:i]
                    if candidate not in seen:
                        seen.add(candidate)
                        ans = max(ans, 1 + dfs(s[i:], seen))
                        seen.remove(candidate)

            return ans

        seen = set()
        return dfs(s, seen)
        
# @lc code=end

