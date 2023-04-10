#
# @lc app=leetcode id=2593 lang=python3
#
# [2593] Find Score of an Array After Marking All Elements
#

# @lc code=start
class Solution:
    def findScore(self, nums: List[int]) -> int:

        n = len(nums)
        seen = [0] * (n + 1)
        res = 0

        for v, i in sorted([v, i] for i, v in enumerate(nums)):
            if seen[i]: continue
            res += v
            seen[i] = seen[i - 1] = seen[i + 1] = 1

        return res
        
# @lc code=end

