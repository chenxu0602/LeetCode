#
# @lc app=leetcode id=1163 lang=python3
#
# [1163] Last Substring in Lexicographical Order
#
# https://leetcode.com/problems/last-substring-in-lexicographical-order/description/
#
# algorithms
# Hard (33.58%)
# Likes:    230
# Dislikes: 300
# Total Accepted:    17.9K
# Total Submissions: 50.6K
# Testcase Example:  '"abab"\r'
#
# Given a string s, return the last substring of s in lexicographical
# order.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abab"
# Output: "bab"
# Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"].
# The lexicographically maximum substring is "bab".
# 
# 
# Example 2:
# 
# 
# Input: "leetcode"
# Output: "tcode"
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= s.length <= 4 * 10^5
# s contains only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def lastSubstring(self, s: str) -> str:
        # Time  complexity: O(N)
        # Space complexity: O(1)
        i, j, offset = 0, 1, 0
        while j + offset < len(s):
            if s[i + offset] == s[j + offset]:
                offset += 1
                continue
            elif s[i + offset] > s[j + offset]:
                j = j + offset + 1
            else:
                i = max(i + offset + 1, j)
                j = i + 1

            offset = 0

        return s[i:]

                
        
# @lc code=end

