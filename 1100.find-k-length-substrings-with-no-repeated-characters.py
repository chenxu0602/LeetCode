#
# @lc app=leetcode id=1100 lang=python3
#
# [1100] Find K-Length Substrings With No Repeated Characters
#
# https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/description/
#
# algorithms
# Medium (71.34%)
# Likes:    47
# Dislikes: 4
# Total Accepted:    3.6K
# Total Submissions: 5K
# Testcase Example:  '"havefunonleetcode"\n5'
#
# Given a string S, return the number of substrings of length K with no
# repeated characters.
# 
# 
# 
# Example 1:
# 
# 
# Input: S = "havefunonleetcode", K = 5
# Output: 6
# Explanation: 
# There are 6 substrings they are :
# 'havef','avefu','vefun','efuno','etcod','tcode'.
# 
# 
# Example 2:
# 
# 
# Input: S = "home", K = 5
# Output: 0
# Explanation: 
# Notice K can be larger than the length of S. In this case is not possible to
# find any substring.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= S.length <= 10^4
# All characters of S are lowercase English letters.
# 1 <= K <= 10^4
# 
# 
#
class Solution:
    def numKLenSubstrNoRepeats(self, S: str, K: int) -> int:
        """
        res, i = 0, 0
        cur = set()
        for j in range(len(S)):
            while S[j] in cur:
                cur.remove(S[i])
                i += 1
            cur.add(S[j])
            res += j - i + 1 >= K
        return res
        """

        return 0 if K > 26 else sum(len(set(S[i:i+K])) == K for i in range(len(S) - K + 1))
        

