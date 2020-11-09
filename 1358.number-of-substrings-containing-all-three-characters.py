#
# @lc app=leetcode id=1358 lang=python3
#
# [1358] Number of Substrings Containing All Three Characters
#
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/
#
# algorithms
# Medium (59.95%)
# Likes:    521
# Dislikes: 11
# Total Accepted:    16.5K
# Total Submissions: 27.6K
# Testcase Example:  '"abcabc"'
#
# Given a string s consisting only of characters a, b and c.
# 
# Return the number of substrings containing at least one occurrence of all
# these characters a, b and c.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the
# characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab",
# "bcabc", "cab", "cabc" and "abc" (again). 
# 
# 
# Example 2:
# 
# 
# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the
# characters a, b and c are "aaacb", "aacb" and "acb". 
# 
# 
# Example 3:
# 
# 
# Input: s = "abc"
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 3 <= s.length <= 5 x 10^4
# s only consists of a, b or c characters.
# 
# 
#

# @lc code=start
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        x = [0, 0, 0]
        i, res = 0, 0
        for j in range(len(s)):
            x[ord(s[j]) - ord('a')] += 1
            while all(x):
                x[ord(s[i]) - ord('a')] -= 1
                i += 1
            res += i
        return res
        
# @lc code=end

