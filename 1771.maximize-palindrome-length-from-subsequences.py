#
# @lc app=leetcode id=1771 lang=python3
#
# [1771] Maximize Palindrome Length From Subsequences
#
# https://leetcode.com/problems/maximize-palindrome-length-from-subsequences/description/
#
# algorithms
# Hard (31.69%)
# Likes:    111
# Dislikes: 5
# Total Accepted:    3K
# Total Submissions: 9.3K
# Testcase Example:  '"cacb"\n"cbba"'
#
# You are given two strings, word1 and word2. You want to construct a string in
# the following manner:
# 
# 
# Choose some non-empty subsequence subsequence1 from word1.
# Choose some non-empty subsequence subsequence2 from word2.
# Concatenate the subsequences: subsequence1 + subsequence2, to make the
# string.
# 
# 
# Return the length of the longest palindrome that can be constructed in the
# described manner. If no palindromes can be constructed, return 0.
# 
# A subsequence of a string s is a string that can be made by deleting some
# (possibly none) characters from s without changing the order of the remaining
# characters.
# 
# A palindrome is a string that reads the same forward as well as backward.
# 
# 
# Example 1:
# 
# 
# Input: word1 = "cacb", word2 = "cbba"
# Output: 5
# Explanation: Choose "ab" from word1 and "cba" from word2 to make "abcba",
# which is a palindrome.
# 
# Example 2:
# 
# 
# Input: word1 = "ab", word2 = "ab"
# Output: 3
# Explanation: Choose "ab" from word1 and "a" from word2 to make "aba", which
# is a palindrome.
# 
# Example 3:
# 
# 
# Input: word1 = "aa", word2 = "bb"
# Output: 0
# Explanation: You cannot construct a palindrome from the described method, so
# return 0.
# 
# 
# Constraints:
# 
# 
# 1 <= word1.length, word2.length <= 1000
# word1 and word2 consist of lowercase English letters.
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        s = word1 + word2
        m, n = map(len, (word1, word2))
        ans = 0

        dp = [[0] * (m + n) for _ in range(m + n)]
        for i in range(m + n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, m + n):
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                    if i < m and j >= m:
                        ans = max(ans, dp[i][j])
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return ans



        
# @lc code=end

