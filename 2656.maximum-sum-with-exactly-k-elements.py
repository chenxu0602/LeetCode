#
# @lc app=leetcode id=2656 lang=python3
#
# [2656] Maximum Sum With Exactly K Elements 
#

# @lc code=start
class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:

        return k * max(nums) + k * (k - 1) // 2
        
# @lc code=end

