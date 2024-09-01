#
# @lc app=leetcode id=3040 lang=python3
#
# [3040] Maximum Number of Operations With the Same Score II
#

# @lc code=start
from functools import cache

class Solution:
    def maxOperations(self, nums: List[int]) -> int:

        @cache
        def dfs(score, lo = 0, hi = len(nums) - 1):
            if lo >= hi: return 0
            max_ops1 = 1 + dfs(score, lo + 2, hi) if score == sum(nums[lo:lo + 2]) else 0
            max_ops2 = 1 + dfs(score, lo, hi - 2) if score == sum(nums[hi - 1:hi + 1]) else 0
            max_ops3 = 1 + dfs(score, lo + 1, hi - 1) if score == nums[lo] + nums[hi] else 0
            return max(max_ops1, max_ops2, max_ops3)

        return max(map(dfs, (nums[0] + nums[1], nums[-1] + nums[-2], nums[0] + nums[-1])))
        
# @lc code=end

