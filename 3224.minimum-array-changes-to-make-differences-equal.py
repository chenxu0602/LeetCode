#
# @lc app=leetcode id=3224 lang=python3
#
# [3224] Minimum Array Changes to Make Differences Equal
#

# @lc code=start
from collections import Counter
from bisect import bisect_left

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:

        n = len(nums) // 2
        pairs = list(map(sorted, zip(nums[:n], nums[-1:n-1:-1])))

        differences = sorted(max(k - x, y) for x, y in pairs)  # max possible difference obtainable by changing 1 number
        ctr = Counter(map(lambda x: x[1] - x[0], pairs))

        # The left side (with small difference) need to change 2 numbers
        return min(bisect_left(differences, key) + n - ctr[key] for key in ctr)

        
# @lc code=end

