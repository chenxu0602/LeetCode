#
# @lc app=leetcode id=2741 lang=python3
#
# [2741] Special Permutations
#

# @lc code=start
from functools import lru_cache

class Solution:
    def specialPerm(self, nums: List[int]) -> int:

        n = len(nums)
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(prev, mask):
            if mask == (1 << n) - 1: 
                return 1

            count = 0

            for i in range(n):
                if not (mask & (1 << i)) and (nums[i] % prev == 0 or prev % nums[i] == 0):
                    count += dfs(nums[i], mask | (1 << i))

            return count % MOD

        return dfs(1, 0)
        
# @lc code=end

