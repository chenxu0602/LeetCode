#
# @lc app=leetcode id=1119 lang=python3
#
# [1119] Remove Vowels from a String
#
# https://leetcode.com/problems/remove-vowels-from-a-string/description/
#
# algorithms
# Easy (87.99%)
# Likes:    29
# Dislikes: 45
# Total Accepted:    11.7K
# Total Submissions: 13.4K
# Testcase Example:  '"leetcodeisacommunityforcoders"'
#
# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and
# return the new string.
# 
# 
# 
# Example 1:
# 
# 
# Input: "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"
# 
# 
# Example 2:
# 
# 
# Input: "aeiou"
# Output: ""
# 
# 
# 
# 
# Note:
# 
# 
# S consists of lowercase English letters only.
# 1 <= S.length <= 1000
# 
# 
#

# @lc code=start
import re

class Solution:
    def removeVowels(self, S: str) -> str:
        
        return re.sub('a|e|i|o|u', '', S)

# @lc code=end

