#
# @lc app=leetcode id=2145 lang=python3
#
# [2145] Count the Hidden Sequences
#

# @lc code=start
import itertools

class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        A = list(itertools.accumulate(differences, initial=0))
        return max(0, (upper - lower) - (max(A) - min(A)) + 1)
        
# @lc code=end

