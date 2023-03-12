#
# @lc app=leetcode id=2465 lang=python3
#
# [2465] Number of Distinct Averages
#

# @lc code=start
class Solution:
    def distinctAverages(self, nums: List[int]) -> int:

        n = len(nums)
        nums.sort()
        return len({nums[i] + nums[~i] for i in range(n // 2)})
        
# @lc code=end

