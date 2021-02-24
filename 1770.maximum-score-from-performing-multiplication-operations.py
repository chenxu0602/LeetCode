#
# @lc app=leetcode id=1770 lang=python3
#
# [1770] Maximum Score from Performing Multiplication Operations
#
# https://leetcode.com/problems/maximum-score-from-performing-multiplication-operations/description/
#
# algorithms
# Medium (26.60%)
# Likes:    171
# Dislikes: 71
# Total Accepted:    5.7K
# Total Submissions: 21.1K
# Testcase Example:  '[1,2,3]\n[3,2,1]'
#
# You are given two integer arrays nums and multipliers of size n and m
# respectively, where n >= m. The arrays are 1-indexed.
# 
# You begin with a score of 0. You want to perform exactly m operations. On the
# i^th operation (1-indexed), you will:
# 
# 
# Choose one integer x from either the start or the end of the array nums.
# Add multipliers[i] * x to your score.
# Remove x from the array nums.
# 
# 
# Return the maximum score after performing m operations.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3], multipliers = [3,2,1]
# Output: 14
# Explanation: An optimal solution is as follows:
# - Choose from the end, [1,2,3], adding 3 * 3 = 9 to the score.
# - Choose from the end, [1,2], adding 2 * 2 = 4 to the score.
# - Choose from the end, [1], adding 1 * 1 = 1 to the score.
# The total score is 9 + 4 + 1 = 14.
# 
# Example 2:
# 
# 
# Input: nums = [-5,-3,-3,-2,7,1], multipliers = [-10,-5,3,4,6]
# Output: 102
# Explanation: An optimal solution is as follows:
# - Choose from the start, [-5,-3,-3,-2,7,1], adding -5 * -10 = 50 to the
# score.
# - Choose from the start, [-3,-3,-2,7,1], adding -3 * -5 = 15 to the score.
# - Choose from the start, [-3,-2,7,1], adding -3 * 3 = -9 to the score.
# - Choose from the end, [-2,7,1], adding 1 * 4 = 4 to the score.
# - Choose from the end, [-2,7], adding 7 * 6 = 42 to the score. 
# The total score is 50 + 15 - 9 + 4 + 42 = 102.
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# m == multipliers.length
# 1 <= m <= 10^3
# m <= n <= 10^5 
# -1000 <= nums[i], multipliers[i] <= 1000
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # n, m = map(len, (nums, multipliers))
        # dp = [[0] * m for _ in range(m + 1)]

        # for i in reversed(range(m)):
        #     for j in range(i, m):
        #         k = i + m - j - 1
        #         dp[i][j] = max(nums[i] * multipliers[k] + dp[i + 1][j],
        #                 nums[j - m + n] * multipliers[k] + dp[i][j - 1])

        # return dp[0][-1]



        @lru_cache(2000)
        def dp(lo, hi, k):
            if k == len(multipliers):
                return 0

            return max(nums[lo] * multipliers[k] + dp(lo + 1, hi, k + 1),
                    nums[hi] * multipliers[k] + dp(lo, hi - 1, k + 1))

        return dp(0, len(nums) - 1, 0)


        
# @lc code=end

