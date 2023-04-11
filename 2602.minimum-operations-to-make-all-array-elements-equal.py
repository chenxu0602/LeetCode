#
# @lc app=leetcode id=2602 lang=python3
#
# [2602] Minimum Operations to Make All Array Elements Equal
#

# @lc code=start
from itertools import accumulate
import bisect

class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:

        nums.sort()
        ans, n, prefix = [], len(nums), [0] + list(accumulate(nums))
        for q in queries:
            i = bisect.bisect_left(nums, q)
            ans.append(q * (2 * i - n) + prefix[n] - 2 * prefix[i])
        return ans
        
# @lc code=end

