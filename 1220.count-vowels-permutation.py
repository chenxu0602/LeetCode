#
# @lc app=leetcode id=1220 lang=python3
#
# [1220] Count Vowels Permutation
#
# https://leetcode.com/problems/count-vowels-permutation/description/
#
# algorithms
# Hard (53.70%)
# Likes:    206
# Dislikes: 44
# Total Accepted:    11.7K
# Total Submissions: 21.7K
# Testcase Example:  '1'
#
# Given an integer n, your task is to count how many strings of length n can be
# formed under the following rules:
# 
# 
# Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
# Each vowel 'a' may only be followed by an 'e'.
# Each vowel 'e' may only be followed by an 'a' or an 'i'.
# Each vowel 'i' may not be followed by another 'i'.
# Each vowel 'o' may only be followed by an 'i' or a 'u'.
# Each vowel 'u' may only be followed by an 'a'.
# 
# 
# Since the answer may be too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: 5
# Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: 10
# Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io",
# "iu", "oi", "ou" and "ua".
# 
# 
# Example 3: 
# 
# 
# Input: n = 5
# Output: 68
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2 * 10^4
# 
# 
#

# @lc code=start
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # dp = [[0] * 5 for _ in range(n + 1)]
        # dp[1] = [1] * 5

        # for i in range(2, n + 1):
        #     # a is allowed to follow e, i, or u.
        #     dp[i][0] = dp[i - 1][1] + dp[i - 1][2] + dp[i - 1][4]
        #     # e is allowed to follow a or i.
        #     dp[i][1] = dp[i - 1][0] + dp[i - 1][2]
        #     # i is allowed to follow e or o.
        #     dp[i][2] = dp[i - 1][1] + dp[i - 1][3]
        #     # o is allowed to follow i
        #     dp[i][3] = dp[i - 1][2]
        #     # u is allowed to follow i or o.
        #     dp[i][4] = dp[i - 1][2] + dp[i - 1][3]

        # return sum(dp[n]) % (10**9 + 7)


        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o

        return (a + e + i + o + u) % (10**9 + 7)
        
# @lc code=end

