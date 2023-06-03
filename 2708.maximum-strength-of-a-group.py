#
# @lc app=leetcode id=2708 lang=python3
#
# [2708] Maximum Strength of a Group
#

# @lc code=start
class Solution:
    def maxStrength(self, nums: List[int]) -> int:

        max_strength = min_strength = nums[0]
        for num in nums[1:]:
            max_strength, min_strength = max(max_strength, num, num * max_strength, num * min_strength), min(min_strength, num, num * min_strength, num * max_strength)
        return max_strength
        
# @lc code=end

