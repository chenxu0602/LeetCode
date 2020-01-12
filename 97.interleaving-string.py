#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Hard (28.61%)
# Likes:    948
# Dislikes: 53
# Total Accepted:    124.9K
# Total Submissions: 428.1K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
# 
# Example 1:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
# 
# 
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l:
            return False

        dp = [[True for _ in range(c+1)] for _ in range(r+1)]

        for i in range(1, r+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        for j in range(1, c+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, r+1):
            for j in range(1, c+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i-1+j]) or \
                    (dp[i][j-1] and s2[j-1] == s3[i-1+j])

        return dp[r][c]

        """
        l1, l2, l3 = len(s1)+1, len(s2)+1, len(s3)+1
        if l1 + l2 != l3+1:
            return False

        pre = [True for _ in range(l2)]

        for j in range(1, l2):
            pre[j] = pre[j-1] and s2[j-1] == s3[j-1]

        for i in range(1, l1):
            cur = [pre[0] and s1[i-1] == s3[i-1]] * l2
            for j in range(1, l2):
                cur[j] = (cur[j-1] and s2[j-1] == s3[i+j-1]) or \
                    (pre[j] and s1[i-1] == s3[i+j-1])
            pre = cur[:]
        return pre[-1]
        """

        



        
# @lc code=end

