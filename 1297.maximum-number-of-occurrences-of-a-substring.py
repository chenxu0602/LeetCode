#
# @lc app=leetcode id=1297 lang=python3
#
# [1297] Maximum Number of Occurrences of a Substring
#
# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/description/
#
# algorithms
# Medium (43.83%)
# Likes:    72
# Dislikes: 82
# Total Accepted:    5.7K
# Total Submissions: 13K
# Testcase Example:  '"aababcaab"\n2\n3\n4'
#
# Given a string s, return the maximum number of ocurrences of any substring
# under the following rules:
# 
# 
# The number of unique characters in the substring must be less than or equal
# to maxLetters.
# The substring size must be between minSize and maxSize inclusive.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
# Output: 2
# Explanation: Substring "aab" has 2 ocurrences in the original string.
# It satisfies the conditions, 2 unique letters and size 3 (between minSize and
# maxSize).
# 
# 
# Example 2:
# 
# 
# Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
# Output: 2
# Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
# 
# 
# Example 3:
# 
# 
# Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
# Output: 3
# 
# 
# Example 4:
# 
# 
# Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# 1 <= maxLetters <= 26
# 1 <= minSize <= maxSize <= min(26, s.length)
# s only contains lowercase English letters.
# 
#

# @lc code=start
from collections import Counter 

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        return next((i for x, i in Counter(s[i:j] for i, j in zip(range(len(s)), range(minSize, len(s)+1))).most_common() if len(set(x)) <= maxLetters), 0)
        
# @lc code=end

