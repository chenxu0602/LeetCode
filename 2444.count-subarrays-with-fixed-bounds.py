#
# @lc app=leetcode id=2444 lang=python3
#
# [2444] Count Subarrays With Fixed Bounds
#

# @lc code=start
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:

        res = 0
        jmin = jmax = jbad = -1

        for i, v in enumerate(nums):
            if not minK <= v <= maxK:
                jbad = i

            if v == minK: jmin = i

            if v == maxK: jmax = i

            res += max(0, min(jmin, jmax) - jbad)

        return res
        
# @lc code=end

