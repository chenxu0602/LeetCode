#
# @lc app=leetcode id=3046 lang=python3
#
# [3046] Split the Array
#

# @lc code=start
from collections import Counter

class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:

        return all(val <= 2 for val in Counter(nums).values())
        
# @lc code=end

