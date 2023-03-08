#
# @lc app=leetcode id=2439 lang=python3
#
# [2439] Minimize Maximum of Array
#

# @lc code=start
import itertools

class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        return max((a + i) // (i + 1) for i, a in enumerate(itertools.accumulate(nums)))
        
# @lc code=end

