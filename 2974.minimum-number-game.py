#
# @lc app=leetcode id=2974 lang=python3
#
# [2974] Minimum Number Game
#

# @lc code=start
class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

        nums.sort()

        for i in range(0, len(nums), 2):
            if i + 1 < len(nums):
                nums[i], nums[i + 1] = nums[i + 1], nums[i]

        return nums
        
# @lc code=end

