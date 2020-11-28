#
# @lc app=leetcode id=1531 lang=python3
#
# [1531] String Compression II
#
# https://leetcode.com/problems/string-compression-ii/description/
#
# algorithms
# Hard (32.30%)
# Likes:    230
# Dislikes: 18
# Total Accepted:    4.7K
# Total Submissions: 14.7K
# Testcase Example:  '"aaabcccd"\n2'
#
# Run-length encoding is a string compression method that works by replacing
# consecutive identical characters (repeated 2 or more times) with the
# concatenation of the character and the number marking the count of the
# characters (length of the run). For example, to compress the string "aabccc"
# we replace "aa" by "a2" and replace "ccc" by "c3". Thus the compressed string
# becomes "a2bc3".
# 
# Notice that in this problem, we are not adding '1' after single characters.
# 
# Given a string s and an integer k. You need to delete at most k characters
# from s such that the run-length encoded version of s has minimum length.
# 
# Find the minimum length of the run-length encoded version of s after deleting
# at most k characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "aaabcccd", k = 2
# Output: 4
# Explanation: Compressing s without deleting anything will give us "a3bc3d" of
# length 6. Deleting any of the characters 'a' or 'c' would at most decrease
# the length of the compressed string to 5, for instance delete 2 'a' then we
# will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way
# is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of
# length 4.
# 
# Example 2:
# 
# 
# Input: s = "aabbaa", k = 2
# Output: 2
# Explanation: If we delete both 'b' characters, the resulting compressed
# string would be "a4" of length 2.
# 
# 
# Example 3:
# 
# 
# Input: s = "aaaaaaaaaaa", k = 0
# Output: 3
# Explanation: Since k is zero, we cannot delete anything. The compressed
# string is "a11" of length 3.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 100
# 0 <= k <= s.length
# s contains only lowercase English letters.
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def counter(start, last, last_count, remain):
            if remain < 0: return float("inf")
            if start >= len(s): return 0
            if s[start] == last:
                incr = 1 if last_count == 1 or last_count == 9 or last_count == 99 else 0
                # no need to delete here, if we have a stretch of chars like 'aaaaa' - we delete it from the beginning in the else delete section
                return incr + counter(start + 1, last, last_count + 1, remain)
            else:
                keep_counter = 1 + counter(start + 1, s[start], 1, remain)
                del_counter = counter(start + 1, last, last_count, remain - 1)
                return min(keep_counter, del_counter)

        return counter(0, "", 0, k)
        
# @lc code=end

