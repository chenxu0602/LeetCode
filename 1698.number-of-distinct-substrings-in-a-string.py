#
# @lc app=leetcode id=1698 lang=python3
#
# [1698] Number of Distinct Substrings in a String
#
# https://leetcode.com/problems/number-of-distinct-substrings-in-a-string/description/
#
# algorithms
# Medium (52.25%)
# Likes:    6
# Dislikes: 1
# Total Accepted:    190
# Total Submissions: 363
# Testcase Example:  '"aabbaba"'
#
# Given a string s, return the number of distinct substrings of s.
# 
# A substring of a string is obtained by deleting any number of characters
# (possibly zero) from the front of the string and any number (possibly zero)
# from the back of the string.
# 
# 
# Example 1:
# 
# 
# Input: s = "aabbaba"
# Output: 21
# Explanation: The set of distinct strings is
# ["a","b","aa","bb","ab","ba","aab","abb","bba","aba","aabb","abba","bbab","baba","aabba","abbab","bbaba","aabbab","abbaba","aabbaba"]
# 
# 
# Example 2:
# 
# 
# Input: s = "abcdefg"
# Output: 28
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 500
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def countDistinct(self, s: str) -> int:
        # O(N^2)
        trie = {}
        res = 0
        for i in range(len(s)):
            curr = trie
            for j in range(i, len(s)):
                if s[j] not in curr:
                    curr[s[j]] = {'$': True}
                curr = curr[s[j]]
                if curr['$']:
                    res += 1
                    curr['$'] = False

        return res
        
# @lc code=end

