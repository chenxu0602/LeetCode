#
# @lc app=leetcode id=3221 lang=python3
#
# [3221] Maximum Array Hopping Score II
#

# @lc code=start
class Solution:
    def maxScore(self, nums: List[int]) -> int:

        ans, max_ = 0, 0
        for num in reversed(nums[1:]):
            max_ = max(max_, num)
            ans += max_

        return ans
        
# @lc code=end

