#
# @lc app=leetcode id=2389 lang=python3
#
# [2389] Longest Subsequence With Limited Sum
#

# @lc code=start
from itertools import accumulate
from bisect import bisect_right

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        acc = list(accumulate(sorted(nums)))
        return [bisect_right(acc, q) for q in queries]
        
# @lc code=end

