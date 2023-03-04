#
# @lc app=leetcode id=2426 lang=python3
#
# [2426] Number of Pairs Satisfying Inequality
#

# @lc code=start
import bisect
from sortedcontainers import SortedList

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:

        l = SortedList()
        res = 0
        for a, b in zip(nums1, nums2):
            res += l.bisect_right(a - b + diff)
            l.add(a - b)
        return res
        
# @lc code=end

