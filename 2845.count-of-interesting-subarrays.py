#
# @lc app=leetcode id=2845 lang=python3
#
# [2845] Count of Interesting Subarrays
#

# @lc code=start
from collections import Counter

class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:

        # Time  complexity: O(n)
        # Space complexity: O(min(n, m))
        vals, res, cnt = Counter({0: 1}), 0, 0
        for v in nums:
            cnt += (v % modulo) == k
            res += vals[(cnt - k) % modulo]
            vals[cnt % modulo] += 1

        return res

        
# @lc code=end

