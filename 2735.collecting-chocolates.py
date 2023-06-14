#
# @lc app=leetcode id=2735 lang=python3
#
# [2735] Collecting Chocolates
#

# @lc code=start
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:

        n = len(nums)
        res = [x * k for k in range(n)]
        for i in range(n):
            cur = nums[i]
            for k in range(n):
                cur = min(cur, nums[i - k])
                res[k] += cur

        return min(res)
        
# @lc code=end

