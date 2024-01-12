#
# @lc app=leetcode id=2965 lang=python3
#
# [2965] Find Missing and Repeated Values
#

# @lc code=start
from itertools import chain
from collections import Counter

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(ctr := Counter(chain(*grid))) + 1
        ans = [0, 0]

        for num in range(1, n + 1):
            if ctr[num] == 1: continue
            ans[1 - ctr[num] // 2] = num

        return ans
        
# @lc code=end

