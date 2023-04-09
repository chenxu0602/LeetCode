#
# @lc app=leetcode id=2576 lang=python3
#
# [2576] Find the Maximum Number of Marked Indices
#

# @lc code=start
class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:

        i, n = 0, len(nums)
        nums.sort()
        for j in range(n - n // 2, n):
            i += 2 * nums[i] <= nums[j]
        return i * 2
        
# @lc code=end

