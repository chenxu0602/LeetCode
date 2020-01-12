#
# @lc app=leetcode id=1155 lang=python3
#
# [1155] Number of Dice Rolls With Target Sum
#
# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
#
# algorithms
# Medium (50.18%)
# Likes:    180
# Dislikes: 14
# Total Accepted:    10.9K
# Total Submissions: 22.4K
# Testcase Example:  '1\n6\n3'
#
# You have d dice, and each die has f faces numbered 1, 2, ..., f.
# 
# Return the number of possible ways (out of f^d total ways) modulo 10^9 + 7 to
# roll the dice so the sum of the face up numbers equals target.
# 
# 
# Example 1:
# 
# 
# Input: d = 1, f = 6, target = 3
# Output: 1
# Explanation: 
# You throw one die with 6 faces.  There is only one way to get a sum of 3.
# 
# 
# Example 2:
# 
# 
# Input: d = 2, f = 6, target = 7
# Output: 6
# Explanation: 
# You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
# 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
# 
# 
# Example 3:
# 
# 
# Input: d = 2, f = 5, target = 10
# Output: 1
# Explanation: 
# You throw two dice, each with 5 faces.  There is only one way to get a sum of
# 10: 5+5.
# 
# 
# Example 4:
# 
# 
# Input: d = 1, f = 2, target = 3
# Output: 0
# Explanation: 
# You throw one die with 2 faces.  There is no way to get a sum of 3.
# 
# 
# Example 5:
# 
# 
# Input: d = 30, f = 30, target = 500
# Output: 222616187
# Explanation: 
# The answer must be returned modulo 10^9 + 7.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= d, f <= 30
# 1 <= target <= 1000
# 
#

# @lc code=start
class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        """
        if target < d or target > d * f:
            return 0

        if target > d * (1 + f) // 2:
            target = d * (1 + f) - target

        dp = [0] * (target + 1)
        for i in range(1, min(f, target) + 1):
            dp[i] = 1

        for i in range(2, d+1):
            new_dp = [0] * (target + 1)
            for j in range(i, min(target, i*f)+1):
                new_dp[j] = new_dp[j-1] + dp[j-1]
                if j - 1 > f:
                    new_dp[j] -= dp[j-f-1]
            dp = new_dp

        return dp[target] % (10**9 + 7)
        """

        dp = [1] + [0] * target
        for i in range(d):
            for j in range(target, -1, -1):
#                dp[j] = sum([dp[j-k] for k in range(1, 1+min(f,j))] or [0])
                dp[j] = sum(dp[max(0, j-f):j])
        return dp[target] % (10**9+7)

        
        
# @lc code=end

