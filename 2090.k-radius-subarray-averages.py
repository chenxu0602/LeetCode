#
# @lc app=leetcode id=2090 lang=python3
#
# [2090] K Radius Subarray Averages
#

# @lc code=start
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        res = [-1] * len(nums)
        left, curWindowSum, radius = 0, 0, 2 * k + 1
        for right in range(len(nums)):
            curWindowSum += nums[right]
            if (right - left + 1 >= radius):
                res[left + k] = curWindowSum // radius
                curWindowSum -= nums[left]
                left += 1
        return res
        
# @lc code=end

