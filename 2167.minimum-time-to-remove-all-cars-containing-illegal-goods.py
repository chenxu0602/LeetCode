#
# @lc app=leetcode id=2167 lang=python3
#
# [2167] Minimum Time to Remove All Cars Containing Illegal Goods
#

# @lc code=start
class Solution:
    def minimumTime(self, s: str) -> int:
        # |..left..|..middle..|..right..|
        # len(left) + 2* count(middle, 1) + len(right) = len(left) + len(middle) + len(right) + 2*count(middle, 1) - len(middle) = n + count(middle, 1) - count(middle, 0)
        # def minSum(nums):
        #     dp = [0] * len(nums)
        #     dp[0] = nums[0]
        #     for i in range(1, len(nums)):
        #         dp[i] = min(nums[i], nums[i] + dp[i - 1])
        #     return min(0, min(dp))

        # s1 = [1 if i == '1' else -1 for i in s]
        # score = minSum(s1)
        # return len(s) + score

        res, curr = len(s), 0
        s1 = [1 if int(x) else -1 for x in s]
        for x in s1:
            curr = min(x, curr + x)
            res = min(res, curr)
        return len(s) + min(res, 0)


        # left, res, n = 0, len(s), len(s)
        # for i, c in enumerate(s):
        #     left = min(left + (c == '1') * 2, i + 1)
        #     res = min(res, left + n - 1 - i)
        # return res
        
# @lc code=end

