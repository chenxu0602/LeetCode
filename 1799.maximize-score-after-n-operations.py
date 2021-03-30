#
# @lc app=leetcode id=1799 lang=python3
#
# [1799] Maximize Score After N Operations
#
# https://leetcode.com/problems/maximize-score-after-n-operations/description/
#
# algorithms
# Hard (52.06%)
# Likes:    117
# Dislikes: 7
# Total Accepted:    3.6K
# Total Submissions: 6.8K
# Testcase Example:  '[1,2]'
#
# You are given nums, an array of positive integers of size 2 * n. You must
# perform n operations on this array.
# 
# In the i^th operation (1-indexed), you will:
# 
# 
# Choose two elements, x and y.
# Receive a score of i * gcd(x, y).
# Remove x and y from nums.
# 
# 
# Return the maximum score you can receive after performing n operations.
# 
# The function gcd(x, y) is the greatest common divisor of x and y.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2]
# Output: 1
# Explanation: The optimal choice of operations is:
# (1 * gcd(1, 2)) = 1
# 
# 
# Example 2:
# 
# 
# Input: nums = [3,4,6,8]
# Output: 11
# Explanation: The optimal choice of operations is:
# (1 * gcd(3, 6)) + (2 * gcd(4, 8)) = 3 + 8 = 11
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,4,5,6]
# Output: 14
# Explanation: The optimal choice of operations is:
# (1 * gcd(1, 5)) + (2 * gcd(2, 4)) + (3 * gcd(3, 6)) = 1 + 4 + 9 = 14
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 7
# nums.length == 2 * n
# 1 <= nums[i] <= 10^6
# 
# 
#

# @lc code=start
from functools import lru_cache
import math
from itertools import combinations

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        # @lru_cache(None)
        # def dfs(i, mask):
        #     if i > len(nums) // 2:
        #         return 0
        #     res = 0
        #     for j in range(len(nums)):
        #         for k in range(j + 1, len(nums)):
        #             new_mask = (1 << j) + (1 << k)
        #             if not mask & new_mask:
        #                 res = max(res, i * math.gcd(nums[j], nums[k]) + dfs(i + 1, mask + new_mask))

        #     return res

        # return dfs(1, 0)


        gcds = {(j, k): math.gcd(nums[j], nums[k]) for j, k in combinations(range(len(nums)), 2)}

        @lru_cache(None)
        def dfs(bitmask):
            if bitmask == 0:
                return 0

            cand = 0
            n_z_bits = [j for j in range(len(nums)) if bitmask & (1 << j)]
            for j, k in combinations(n_z_bits, 2):
                q = bitmask ^ (1 << j) ^ (1 << k)
                cand = max(cand, dfs(q) + (len(nums) + 2 - len(n_z_bits)) / 2 * gcds[j, k])

            return int(cand)

        return dfs((1 << len(nums)) - 1)
        
# @lc code=end

