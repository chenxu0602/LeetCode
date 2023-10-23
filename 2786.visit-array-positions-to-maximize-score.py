#
# @lc app=leetcode id=2786 lang=python3
#
# [2786] Visit Array Positions to Maximize Score
#

# @lc code=start
from functools import lru_cache

class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:

        # @lru_cache(None)
        # def dfs(i, oldPar):
        #     if i >= len(nums):
        #         return 0
            
        #     newPar = nums[i] % 2

        #     return max(dfs(i + 1, oldPar),
        #                nums[i] + dfs(i + 1, newPar) - x * (newPar != oldPar))

        # return dfs(0, nums[0] % 2)


        even_score = nums[0] - (x if nums[0] % 2 else 0)
        odd_score  = nums[0] - (0 if nums[0] % 2 else x)

        n = len(nums)
        for i in range(1, n):
            if nums[i] % 2:
                odd_score  = nums[i] + max(odd_score, even_score - x)
                even_score = even_score
            else:
                even_score = nums[i] + max(even_score, odd_score - x)
                odd_score = odd_score

        return max(even_score, odd_score)
        
        
# @lc code=end

