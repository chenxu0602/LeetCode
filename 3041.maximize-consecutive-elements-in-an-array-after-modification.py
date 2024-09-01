#
# @lc app=leetcode id=3041 lang=python3
#
# [3041] Maximize Consecutive Elements in an Array After Modification
#

# @lc code=start
from collections import defaultdict

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:

        dp = defaultdict(int)
        nums.sort()
        for num in nums:
            dp[num + 1] = dp[num] + 1
            dp[num] = dp[num - 1] + 1
        return max(dp.values())
        
# @lc code=end

