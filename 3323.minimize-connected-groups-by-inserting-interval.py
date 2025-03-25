#
# @lc app=leetcode id=3323 lang=python3
#
# [3323] Minimize Connected Groups by Inserting Interval
#

# @lc code=start
from bisect import bisect_left

class Solution:
    def minConnectedGroups(self, intervals: List[List[int]], k: int) -> int:

        bin_search = lambda x: bisect_left(begs, x[1] + k + 1) - x[0] - 1

        intervals.sort()
        beg0, end0 = intervals.pop(0)
        begs, ends = [beg0], [end0]

        for beg, end in intervals:
            if beg > ends[-1]:
                begs += beg,
                ends += end,
            elif beg <= ends[-1] < end:
                ends[-1] = end


        return len(begs) - max(map(bin_search, enumerate(ends)))

        
# @lc code=end

