#
# @lc app=leetcode id=3034 lang=python3
#
# [3034] Number of Subarrays That Match a Pattern I
#

# @lc code=start
from itertools import pairwise

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:

        n, p, ans = len(nums), len(pattern), 0
        f = lambda x: 2 * (x[1] >= x[0]) - (x[1] == x[0]) - 1

        arr = list(map(f, pairwise(nums)))

        for i in range(n - p):
            if arr[i:i + p] == pattern:
                ans += 1

        return ans
        
# @lc code=end

