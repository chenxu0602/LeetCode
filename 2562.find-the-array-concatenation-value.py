#
# @lc app=leetcode id=2562 lang=python3
#
# [2562] Find the Array Concatenation Value
#

# @lc code=start
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:

        ans = 0
        if len(nums) % 2 == 1:
            ans = nums[len(nums) // 2]

        for i in range(len(nums) // 2):
            ans += int(str(nums[i]) + str(nums[len(nums) - 1 - i]))

        return ans
        
# @lc code=end

