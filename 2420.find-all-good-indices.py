#
# @lc app=leetcode id=2420 lang=python3
#
# [2420] Find All Good Indices
#

# @lc code=start
class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:

        n, ans = len(nums), []
        dp1, dp2 = [1] * (n + 1), [1] * (n + 1)

        for i in range(1, n):
            if nums[i - 1] >= nums[i]:
                dp1[i] = dp1[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                dp2[i] = dp2[i + 1] + 1

        for i in range(k, n - k):
            if dp1[i - 1] >= k and dp2[i + 1] >= k:
                ans += i,

        return ans
        
# @lc code=end

