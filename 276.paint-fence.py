#
# @lc app=leetcode id=276 lang=python3
#
# [276] Paint Fence
#
# https://leetcode.com/problems/paint-fence/description/
#
# algorithms
# Easy (36.52%)
# Likes:    425
# Dislikes: 108
# Total Accepted:    42.6K
# Total Submissions: 116.7K
# Testcase Example:  '3\n2'
#
# There is a fence with n posts, each post can be painted with one of the k
# colors.
# 
# You have to paint all the posts such that no more than two adjacent fence
# posts have the same color.
# 
# Return the total number of ways you can paint the fence.
# 
# Note:
# n and k are non-negative integers.
# 
# Example:
# 
# 
# Input: n = 3, k = 2
# Output: 6
# Explanation: Take c1 as color 1, c2 as color 2. All possible ways
# are:
# 
# post1  post2  post3      
# ⁠-----      -----  -----  -----       
# ⁠  1         c1     c1     c2 
# 2         c1     c2     c1 
# 3         c1     c2     c2 
# 4         c2     c1     c1  
# ⁠  5         c2     c1     c2
# 6         c2     c2     c1
# 
# 
#
class Solution:
    def numWays(self, n: int, k: int) -> int:

        """
        if n == 0:
            return 0
        if n == 1:
            return k
        same, diff = k, k*(k-1)
        for i in range(3, n+1):
            same, diff = diff, (same+diff) * (k-1)
        return same + diff
        """

        if n == 0: return 0
        if n == 1: return k
        if n == 2: return k*k

        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = k
        dp[2] = k * k

        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) * (k - 1)

        return dp[n]



