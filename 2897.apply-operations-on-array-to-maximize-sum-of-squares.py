#
# @lc app=leetcode id=2897 lang=python3
#
# [2897] Apply Operations on Array to Maximize Sum of Squares
#

# @lc code=start
from collections import Counter

class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:

        # Observe the effect of an operation on one bit:
        # (1, 1) -> (1 & 1, 1 | 1) -> (1, 1)
        # (0, 0) -> (0 & 0, 0 | 0) -> (0, 0)
        # (0, 1) -> (0 & 1, 0 | 1) -> (0, 1)
        # (1, 0) -> (1 & 0, 1 | 0) -> (0, 1)

        # The first three cases won't change anything,
        # the last case will move the bit from A[i] to A[j].

        # So apply operation as many as possible,
        # it will sort the array on each bit,
        # from random array [1,0,1,0,1,0,0],
        # to a sorted array [0,0,0,0,1,1,1].
        # Time  complexity: O(32n)
        # Space complexity: O(32)

        """
        count = [0] * 32
        for num in nums:
            for i in range(32):
                if num & ( 1 << i):
                    count[i] += 1

        res, MOD = 0, 10**9 + 7
        for j in range(k):
            cur = 0
            for i in range(32):
                if count[i]:
                    count[i] -= 1
                    cur += 1 << i

            res += cur * cur % MOD

        return res % MOD
        """

        MOD = 10**9 + 7
        count = Counter(i for num in nums for i in range(32) if num & (1 << i))
        return sum(sum((count[i] > j) << i for i in range(32)) ** 2 for j in range(k)) % MOD

        
# @lc code=end

