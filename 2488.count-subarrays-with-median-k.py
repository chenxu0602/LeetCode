#
# @lc app=leetcode id=2488 lang=python3
#
# [2488] Count Subarrays With Median K
#

# @lc code=start
from collections import defaultdict

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:

        d, iMed = defaultdict(int), nums.index(k)
        ans, diff, d[0] = 0, 0, 1

        for i, n in enumerate(nums):
            diff += (n > k) - (n < k)

            if i < iMed: 
                d[diff] += 1
            else:
                ans += d[diff] + d[diff - 1]

        return ans
        
# @lc code=end

