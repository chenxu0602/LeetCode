#
# @lc app=leetcode id=2848 lang=python3
#
# [2848] Points That Intersect With Cars
#

# @lc code=start
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        s = set()
        for start, end in nums:
            s |= set(range(start, end + 1))
        return len(s)
        
# @lc code=end

