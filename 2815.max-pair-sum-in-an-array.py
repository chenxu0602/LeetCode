#
# @lc app=leetcode id=2815 lang=python3
#
# [2815] Max Pair Sum in an Array
#

# @lc code=start
from collections import defaultdict

class Solution:
    def maxSum(self, nums: List[int]) -> int:

        d, ans = defaultdict(list), -1

        for num in nums:
            d[max(str(num))] += num,

        for i in d:
            if len(d[i]) < 2: continue

            ans = max(ans, sum(sorted(d[i])[-2:]))

        return ans
        
# @lc code=end

