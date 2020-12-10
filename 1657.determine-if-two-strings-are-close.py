#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#
# https://leetcode.com/problems/determine-if-two-strings-are-close/description/
#
# algorithms
# Medium (50.67%)
# Likes:    141
# Dislikes: 11
# Total Accepted:    7.9K
# Total Submissions: 15.5K
# Testcase Example:  '"abc"\n"bca"'
#
# Two strings are considered close if you can attain one from the other using
# the following operations:
# 
# 
# Operation 1: Swap any two existing characters.
# 
# 
# For example, abcde -> aecdb
# 
# 
# Operation 2: Transform every occurrence of one existing character into
# another existing character, and do the same with the other
# character.
# 
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into
# a's)
# 
# 
# 
# 
# You can use the operations on either string as many times as necessary.
# 
# Given two strings, word1 and word2, return true if word1 and word2 are close,
# and false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: word1 = "abc", word2 = "bca"
# Output: true
# Explanation: You can attain word2 from word1 in 2 operations.
# Apply Operation 1: "abc" -> "acb"
# Apply Operation 1: "acb" -> "bca"
# 
# 
# Example 2:
# 
# 
# Input: word1 = "a", word2 = "aa"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in
# any number of operations.
# 
# 
# Example 3:
# 
# 
# Input: word1 = "cabbba", word2 = "abbccc"
# Output: true
# Explanation: You can attain word2 from word1 in 3 operations.
# Apply Operation 1: "cabbba" -> "caabbb"
# Apply Operation 2: "caabbb" -> "baaccc"
# Apply Operation 2: "baaccc" -> "abbccc"
# 
# 
# Example 4:
# 
# 
# Input: word1 = "cabbba", word2 = "aabbss"
# Output: false
# Explanation: It is impossible to attain word2 from word1, or vice versa, in
# any amount of operations.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= word1.length, word2.length <= 10^5
# word1 and word2 contain only lowercase English letters.
# 
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1, c2 = Counter(word1), Counter(word2)
        return sorted(c1.keys()) == sorted(c2.keys()) and sorted(c1.values()) == sorted(c2.values())
        
# @lc code=end

