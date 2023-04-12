#
# @lc app=leetcode id=2610 lang=python3
#
# [2610] Convert an Array Into a 2D Array With Conditions
#

# @lc code=start
from collections import Counter

class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:

        count = Counter(nums)
        k = max(count.values())
        A = list(count.elements())
        return [A[i::k] for i in range(k)]
        
# @lc code=end

