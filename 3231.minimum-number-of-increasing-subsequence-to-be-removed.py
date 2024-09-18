#
# @lc app=leetcode id=3231 lang=python3
#
# [3231] Minimum Number of Increasing Subsequence to Be Removed
#

# @lc code=start
from bisect import bisect_right

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        n = len(nums)
        ans = []

        for num in reversed(nums):
            idx = bisect_right(ans, num)

            if idx == len(ans):
                ans += num,
            else:
                ans[idx] = num

        return len(ans)
        
# @lc code=end

