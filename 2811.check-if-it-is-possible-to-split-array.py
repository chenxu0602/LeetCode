#
# @lc app=leetcode id=2811 lang=python3
#
# [2811] Check if it is Possible to Split Array
#

# @lc code=start
class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:

        n = len(nums)
        if n < 3: return True 
        return any(nums[i] + nums[i + 1] >= m for i in range(n - 1))
        
# @lc code=end

