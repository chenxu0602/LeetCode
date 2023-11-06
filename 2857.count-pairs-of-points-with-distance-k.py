#
# @lc app=leetcode id=2857 lang=python3
#
# [2857] Count Pairs of Points With Distance k
#

# @lc code=start
from collections import Counter

class Solution:
    def countPairs(self, coordinates: List[List[int]], k: int) -> int:

        # Given an array A, find the pair that A[i] ^ A[j] == k.
        # For each A[i], find it's pair A[i] ^ k and update res += count[A[i] ^ k]
        # then update count[A[i]] += 1
        count = Counter()
        res = 0
        for x1, y1 in coordinates:
            for x in range(k + 1):
                res += count[x1 ^ x, y1 ^ (k - x)]
            count[x1, y1] += 1

        return res
        
# @lc code=end

