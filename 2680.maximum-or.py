#
# @lc app=leetcode id=2680 lang=python3
#
# [2680] Maximum OR
#

# @lc code=start
class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:

        """
        res, left, n = 0, 0, len(nums)
        right = [0] * n

        for i in range(n - 2, -1, -1):
            right[i]  = right[i + 1] | nums[i + 1]

        for i in range(n):
            res = max(res, left | nums[i] << k | right[i])
            left |= nums[i]

        return res
        """

        cur, saved = 0, 0
        for num in nums:
            saved |= num & cur
            cur |= num

        max_num = 0

        for num in nums:
            max_num = max(max_num, saved | (cur & ~num) | num << k)

        return max_num
        
# @lc code=end

