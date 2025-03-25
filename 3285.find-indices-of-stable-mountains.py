#
# @lc app=leetcode id=3285 lang=python3
#
# [3285] Find Indices of Stable Mountains
#

# @lc code=start
from itertools import pairwise

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:

        # ans = []
        # for i, (prev, h) in enumerate(pairwise(height)):
        #     if prev > threshold: ans += i + 1,

        # return ans

        return [i for i in range(1, len(height)) if height[i - 1] > threshold]

        
# @lc code=end

