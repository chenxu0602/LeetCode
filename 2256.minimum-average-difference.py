#
# @lc app=leetcode id=2256 lang=python3
#
# [2256] Minimum Average Difference
#

# @lc code=start
class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        front, back = 0, sum(nums)
        minn, min_idx = float("inf"), -1

        for i in range(n):
            front += nums[i]
            back -= nums[i]

            if i < n - 1:
                x = front // (i + 1)
                y = back // (n - i - 1)
                val = x - y
            else:
                val = front // (i + 1)

            val = abs(val)

            if val < minn:
                minn = val
                min_idx = i

        return min_idx
        
# @lc code=end

