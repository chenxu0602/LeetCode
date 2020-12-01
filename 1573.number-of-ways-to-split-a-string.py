#
# @lc app=leetcode id=1573 lang=python3
#
# [1573] Number of Ways to Split a String
#
# https://leetcode.com/problems/number-of-ways-to-split-a-string/description/
#
# algorithms
# Medium (30.44%)
# Likes:    186
# Dislikes: 26
# Total Accepted:    9K
# Total Submissions: 29.7K
# Testcase Example:  '"10101"'
#
# Given a binary string s (a string consisting only of '0's and '1's), we can
# split s into 3 non-empty strings s1, s2, s3 (s1+ s2+ s3 = s).
# 
# Return the number of ways s can be split such that the number of characters
# '1' is the same in s1, s2, and s3.
# 
# Since the answer may be too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: s = "10101"
# Output: 4
# Explanation: There are four ways to split s in 3 parts where each part
# contain the same number of letters '1'.
# "1|010|1"
# "1|01|01"
# "10|10|1"
# "10|1|01"
# 
# 
# Example 2:
# 
# 
# Input: s = "1001"
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: s = "0000"
# Output: 3
# Explanation: There are three ways to split s in 3 parts.
# "0|0|00"
# "0|00|0"
# "00|0|0"
# 
# 
# Example 4:
# 
# 
# Input: s = "100100010100110"
# Output: 12
# 
# 
# 
# Constraints:
# 
# 
# 3 <= s.length <= 10^5
# s[i] is '0' or '1'.
# 
# 
#

# @lc code=start
class Solution:
    def numWays(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)
        cnt = s.count('1')
        if cnt == 0:
            return (n - 1) * (n - 2) // 2 % MOD
        if cnt % 3: return 0

        ones = []
        for i, x in enumerate(s):
            if x == '1':
                ones.append(i)

        return (ones[cnt//3] - ones[cnt//3 - 1]) * (ones[2*cnt//3] - ones[2*cnt//3 - 1]) % MOD
        
# @lc code=end

