#
# @lc app=leetcode id=2740 lang=python3
#
# [2740] Find the Value of the Partition
#

# @lc code=start
class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:

        nums.sort()
        return min(nums[i] - nums[i - 1] for i in range(1, len(nums)))
        
# @lc code=end

