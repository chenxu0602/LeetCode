#
# @lc app=leetcode id=3026 lang=python3
#
# [3026] Maximum Good Subarray Sum
#

# @lc code=start
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:

        pre = defaultdict(lambda: float('inf'))
        cur, res = 0, float('-inf')
        for num in nums:
            pre[num] = min(pre[num], cur)
            cur += num
            res = max(res, cur - pre[num - k], cur - pre[num + k])

        return res if res > float('-inf') else 0
        
# @lc code=end

