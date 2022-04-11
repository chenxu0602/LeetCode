#
# @lc app=leetcode id=2206 lang=python3
#
# [2206] Divide Array Into Equal Pairs
#

# @lc code=start
from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        return all(v % 2 == 0 for v in Counter(nums).values())
        
# @lc code=end

