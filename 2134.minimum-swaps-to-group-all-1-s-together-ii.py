#
# @lc app=leetcode id=2134 lang=python3
#
# [2134] Minimum Swaps to Group All 1's Together II
#

# @lc code=start
class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        # Count number of ones in nums, let the number of ones be stored in the variable ones
        # Append nums to nums because we have to look at it as a circular array
        # Find the maximum number of ones in a window of size ones in the new array
        # Number of swaps = ones - maximum number of ones in a window of size ones

        ones, n = nums.count(1), len(nums)
        x, onesInWindow = 0, 0
        for i in range(n * 2):
            if i >= ones and nums[i % n - ones]:
                x -= 1
            if nums[i % n] == 1:
                x += 1
            onesInWindow = max(x, onesInWindow)

        return ones - onesInWindow
        
# @lc code=end

