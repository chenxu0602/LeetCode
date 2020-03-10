#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#
# https://leetcode.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (40.07%)
# Likes:    1024
# Dislikes: 52
# Total Accepted:    77.7K
# Total Submissions: 193.4K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# Given two strings s1 and s2, write a function to return true if s2 contains
# the permutation of s1. In other words, one of the first string's permutations
# is the substring of the second string.
# 
# 
# 
# Example 1:
# 
# 
# Input: s1 = "ab" s2 = "eidbaooo"
# Output: True
# Explanation: s2 contains one permutation of s1 ("ba").
# 
# 
# Example 2:
# 
# 
# Input:s1= "ab" s2 = "eidboaoo"
# Output: False
# 
# 
# 
# 
# Note:
# 
# 
# The input strings only contain lower case letters.
# The length of both given strings is in range [1, 10,000].
# 
# 
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2): return False

        map1, map2 = [0] * 26, [0] * 26

        i = 0
        while i < len(s1):
            map1[ord(s1[i]) - ord('a')] += 1
            map2[ord(s2[i]) - ord('a')] += 1
            i += 1

        if map1 == map2: return True

        left, right = 0, i
        while right < len(s2):
            map2[ord(s2[right]) - ord('a')] += 1
            map2[ord(s2[left]) - ord('a')] -= 1

            if map1 == map2: return True
            left += 1; right += 1

        return False
        
# @lc code=end

