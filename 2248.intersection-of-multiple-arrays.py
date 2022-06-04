#
# @lc app=leetcode id=2248 lang=python3
#
# [2248] Intersection of Multiple Arrays
#

# @lc code=start
from collections import Counter

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return sorted([k for k, v in Counter([x for l in nums for x in l]).items() if v == len(nums)])
        
# @lc code=end

