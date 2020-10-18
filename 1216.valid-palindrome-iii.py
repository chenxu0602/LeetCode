#
# @lc app=leetcode id=1216 lang=python3
#
# [1216] Valid Palindrome III
#
# https://leetcode.com/problems/valid-palindrome-iii/description/
#
# algorithms
# Hard (45.44%)
# Likes:    99
# Dislikes: 3
# Total Accepted:    4.8K
# Total Submissions: 10.6K
# Testcase Example:  '"abcdeca"\n2'
#
# Given a string s and an integer k, find out if the given string is a
# K-Palindrome or not.
# 
# A string is K-Palindrome if it can be transformed into a palindrome by
# removing at most k characters from it.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcdeca", k = 2
# Output: true
# Explanation: Remove 'b' and 'e' characters.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s has only lowercase English letters.
# 1 <= k <= s.length
# 
# 
#

# @lc code=start
class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # Longest palindromic subsequence

        # n = len(s)
        # dp = [[0] * (n + 1) for _ in range(n + 1)]

        # for i in range(1, n + 1):
        #     for j in range(1, n + 1):
        #         if s[i - 1] == s[n - j]:
        #             dp[i][j] = dp[i - 1][j - 1] + 1
        #         else:
        #             dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # return n - dp[n][n] <= k


        n = len(s)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return n - dp[0][n - 1] <= k

        
# @lc code=end

