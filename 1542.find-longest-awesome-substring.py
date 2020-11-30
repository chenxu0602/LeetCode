#
# @lc app=leetcode id=1542 lang=python3
#
# [1542] Find Longest Awesome Substring
#
# https://leetcode.com/problems/find-longest-awesome-substring/description/
#
# algorithms
# Hard (35.98%)
# Likes:    271
# Dislikes: 6
# Total Accepted:    4.7K
# Total Submissions: 13.1K
# Testcase Example:  '"3242415"'
#
# Given a string s. An awesome substring is a non-empty substring of s such
# that we can make any number of swaps in order to make it palindrome.
# 
# Return the length of the maximum length awesome substring of s.
# 
# 
# Example 1:
# 
# 
# Input: s = "3242415"
# Output: 5
# Explanation: "24241" is the longest awesome substring, we can form the
# palindrome "24142" with some swaps.
# 
# 
# Example 2:
# 
# 
# Input: s = "12345678"
# Output: 1
# 
# 
# Example 3:
# 
# 
# Input: s = "213123"
# Output: 6
# Explanation: "213123" is the longest awesome substring, we can form the
# palindrome "231132" with some swaps.
# 
# 
# Example 4:
# 
# 
# Input: s = "00"
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists only of digits.
# 
# 
#

# @lc code=start
class Solution:
    def longestAwesome(self, s: str) -> int:
        # We have 10 + 1 types of palindromes.
        # Use any number as the middle character, or don't have a middle character.

        res, cur, n = 0, 0, len(s)
        seen = [-1] + [n] * 1024

        for i, c in enumerate(s):
            cur ^= 1 << int(c)
            for j in range(10):
                res = max(res, i - seen[cur ^ (1 << j)])
            res = max(res, i - seen[cur])
            seen[cur] = min(seen[cur], i)

        return res
        
# @lc code=end

