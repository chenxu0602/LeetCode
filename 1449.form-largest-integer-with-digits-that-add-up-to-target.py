#
# @lc app=leetcode id=1449 lang=python3
#
# [1449] Form Largest Integer With Digits That Add up to Target
#
# https://leetcode.com/problems/form-largest-integer-with-digits-that-add-up-to-target/description/
#
# algorithms
# Hard (43.00%)
# Likes:    293
# Dislikes: 5
# Total Accepted:    7.7K
# Total Submissions: 17.9K
# Testcase Example:  '[4,3,2,5,6,7,2,5,5]\n9'
#
# Given an array of integers cost and an integer target. Return the maximum
# integer you can paint under the following rules:
# 
# 
# The cost of painting a digit (i+1) is given by cost[i] (0 indexed).
# The total cost used must be equal to target.
# Integer does not have digits 0.
# 
# 
# Since the answer may be too large, return it as string.
# 
# If there is no way to paint any integer given the condition, return "0".
# 
# 
# Example 1:
# 
# 
# Input: cost = [4,3,2,5,6,7,2,5,5], target = 9
# Output: "7772"
# Explanation:  The cost to paint the digit '7' is 2, and the digit '2' is 3.
# Then cost("7772") = 2*3+ 3*1 = 9. You could also paint "977", but "7772" is
# the largest number.
# Digit    cost
# ⁠ 1  ->   4
# ⁠ 2  ->   3
# ⁠ 3  ->   2
# ⁠ 4  ->   5
# ⁠ 5  ->   6
# ⁠ 6  ->   7
# ⁠ 7  ->   2
# ⁠ 8  ->   5
# ⁠ 9  ->   5
# 
# 
# Example 2:
# 
# 
# Input: cost = [7,6,5,5,5,6,8,7,8], target = 12
# Output: "85"
# Explanation: The cost to paint the digit '8' is 7, and the digit '5' is 5.
# Then cost("85") = 7 + 5 = 12.
# 
# 
# Example 3:
# 
# 
# Input: cost = [2,4,6,2,4,6,4,4,4], target = 5
# Output: "0"
# Explanation: It's not possible to paint any integer with total cost equal to
# target.
# 
# 
# Example 4:
# 
# 
# Input: cost = [6,10,15,40,40,40,40,40,40], target = 47
# Output: "32211"
# 
# 
# 
# Constraints:
# 
# 
# cost.length == 9
# 1 <= cost[i] <= 5000
# 1 <= target <= 5000
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0] + [-1] * (target + 5000)
        for t in range(1, target + 1):
            dp[t] = max(dp[t - c] * 10 + i + 1 for i, c in enumerate(cost))
        return str(max(dp[t], 0))


        # @lru_cache(None)
        # def max_sum(i, target):
        #     if i == len(cost) or target < 0:
        #         return float("-inf")

        #     if target == 0:
        #         return 0

        #     # the two scenarios, 1 is take the current digit, the other one is not taking the current digit
        #     c1 = max_sum(i, target - cost[i]) * 10 + i + 1
        #     c2 = max_sum(i + 1, target)
        #     res = max(c1, c2)
        #     return res

        # res = max_sum(0, target)
        # if res > 0:
        #     return str(res)
        # else:
        #     return '0'


        # def getBigger(num1, num2):
        #     if '0' in num2:
        #         return num1
        #     elif '0' in num1:
        #         return num2
        #     elif int(num1) > int(num2):
        #         return num1
        #     else:
        #         return num2

        # def dfs(cost, index, remain):
        #     if remain == 0:
        #         return ""
        #     elif remain < 0 or index == len(cost) + 1:
        #         return "0"

        #     take = str(index) + dfs(cost, 1, remain - cost[index - 1])
        #     skip = dfs(cost, index + 1, remain)

        #     return getBigger(take, skip)

        # ans = dfs(cost, 1, target)
        # return ans if '0' not in ans else '0'
        
# @lc code=end

