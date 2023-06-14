#
# @lc app=leetcode id=2733 lang=python3
#
# [2733] Neither Minimum nor Maximum
#

# @lc code=start
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:

        min_, max_ = min(nums), max(nums)
        for n in nums:
            if n != min_ and n != max_:
                return n
        return -1
        
# @lc code=end

