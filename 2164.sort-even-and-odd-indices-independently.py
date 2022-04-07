#
# @lc app=leetcode id=2164 lang=python3
#
# [2164] Sort Even and Odd Indices Independently
#

# @lc code=start
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        nums[::2], nums[1::2] = sorted(nums[::2]), sorted(nums[1::2])[::-1]
        return nums
        
# @lc code=end

