#
# @lc app=leetcode id=1230 lang=python3
#
# [1230] Toss Strange Coins
#
# https://leetcode.com/problems/toss-strange-coins/description/
#
# algorithms
# Medium (45.62%)
# Likes:    73
# Dislikes: 3
# Total Accepted:    3K
# Total Submissions: 6.6K
# Testcase Example:  '[0.4]\n1'
#
# You have some coins.  The i-th coin has a probability prob[i] of facing heads
# when tossed.
# 
# Return the probability that the number of coins facing heads equals target if
# you toss every coin exactly once.
# 
# 
# Example 1:
# Input: prob = [0.4], target = 1
# Output: 0.40000
# Example 2:
# Input: prob = [0.5,0.5,0.5,0.5,0.5], target = 0
# Output: 0.03125
# 
# 
# Constraints:
# 
# 
# 1 <= prob.length <= 1000
# 0 <= prob[i] <= 1
# 0 <= target <= prob.length
# Answers will be accepted as correct if they are within 10^-5 of the correct
# answer.
# 
# 
#

# @lc code=start
class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:

        # dp[c][k] is the prob of tossing c first coins and get k faced up.
        # dp[c][k] = dp[c - 1][k] * (1 - p) + dp[c - 1][k - 1] * p)

        dp = [1] + [0] * target
        for p in prob:
            for k in range(target, -1, -1):
                dp[k] = (dp[k-1] if k else 0) * p + dp[k] * (1-p)
        return dp[target]
        
# @lc code=end

