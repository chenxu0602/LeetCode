#
# @lc app=leetcode id=2859 lang=python3
#
# [2859] Sum of Values at Indices With K Set Bits
#

# @lc code=start
class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:

        # if k == 0: return nums[0]
        # n = len(nums)
        # d, j, res = [0] * n, 1, 0
        # for i in range(1, n):
        #     if i == j * 2: j *= 2
        #     d[i] = 1 + d[i - j]
        #     if d[i] == k:
        #         res += nums[i]

        # return res


        if k == 0: return nums[0]
        n = len(nums)
        d, res = [0] * n, 0
        for i in range(1, n):
            d[i] = 1 + d[i & (i - 1)]
            if d[i] == k:
                res += nums[i]

        return res
        
# @lc code=end

