#
# @lc app=leetcode id=2875 lang=python3
#
# [2875] Minimum Size Subarray in Infinite Array
#

# @lc code=start
class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:

        # n, s = len(nums), sum(nums)
        # k = target // s
        # target %= s
        # if target % s == 0: return k * n

        # dp = {0: -1}
        # su, res = 0, float("inf")
        # for i, num in enumerate(nums * 2):
        #     su += num
        #     if su - target in dp:
        #         res = min(res, i - dp.get(su - target))
        #     dp[su] = i

        # return res + n * k if res < float("inf") else -1


        n, s = len(nums), sum(nums)
        num_cycles, target = target // s, target % s

        seen, curr, res = {0: -1}, 0, float("inf")
        for i in range(n * 2):
            curr += nums[i % n]
            seen[curr] = i
            if curr - target in seen:
                res = min(res, i - seen[curr - target])

        res += num_cycles * n
        return -1 if res == float("inf") else res
        
# @lc code=end

