#
# @lc app=leetcode id=2251 lang=python3
#
# [2251] Number of Flowers in Full Bloom
#

# @lc code=start
import bisect, itertools
from sortedcontainers import SortedDict

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        """
        # Time  complexity: O(nlogn + mlogn)
        # Space complexity: O(n)
        start, end = sorted(start for start, end in flowers), sorted(end for start, end in flowers)
        return [bisect.bisect_right(start, t) - bisect.bisect_left(end, t) for t in persons]
        """

        diff = SortedDict({0: 0})
        for i, j in flowers:
            diff[i] = diff.get(i, 0) + 1
            diff[j + 1] = diff.get(j + 1, 0) - 1

        count = list(itertools.accumulate(diff.values()))
        return [count[diff.bisect_right(t) - 1] for t in persons]

        
# @lc code=end

