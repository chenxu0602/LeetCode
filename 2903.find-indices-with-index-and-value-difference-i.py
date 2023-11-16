#
# @lc app=leetcode id=2903 lang=python3
#
# [2903] Find Indices With Index and Value Difference I
#

# @lc code=start
from itertools import combinations

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:

        if indexDifference == valueDifference == 0: return [0, 0]

        pairs = filter(lambda x: x[1] - x[0] >= indexDifference, combinations(range(len(nums)), 2))

        for i, j in pairs:
            if abs(nums[i] - nums[j]) >= valueDifference:
                return [i, j]

        return [-1, -1]
        
# @lc code=end

