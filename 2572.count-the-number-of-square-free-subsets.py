#
# @lc app=leetcode id=2572 lang=python3
#
# [2572] Count the Number of Square-Free Subsets
#

# @lc code=start
from collections import Counter, defaultdict
import math

class Solution:
    def squareFreeSubsets(self, nums: List[int]) -> int:

        """
        MOD = 10**9 + 7
        cnt = Counter(nums)

        def count(arr):
            if not arr: return 1
            arr1 = [x for x in arr if math.gcd(x, arr[0]) == 1]
            return (count(arr[1:]) + cnt[arr[0]] * count(arr1)) % MOD

        candidates = [2, 3, 5, 6, 7, 10, 11, 13, 14, 15, 17, 19, 21, 22, 23, 26, 29, 30]
        return (count(candidates) * pow(2, cnt[1], MOD) - 1) % MOD
        """

        """
        MOD = 10**9 + 7
        valid = {1:0, 2:1, 3:2, 5:4, 6:3, 7:8, 10:5, 11:16, 13:32, 14:9, 15:6, 17:64, 19:128, 21:10, 22:17, 23:256, 26:33, 29:512, 30:7}
        count = Counter()
        for n in nums:
            if n in valid:
                for k in count.copy():
                    if valid[n] & k == 0:
                        count[valid[n] | k] += count[k]

                count[valid[n]] += 1

        return sum(count.values()) % MOD
        """

        MOD = 10**9 + 7
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        dp = [0] * (1 << 10)
        dp[0] = 1

        for a in nums:
            mask = 0
            for i, v in enumerate(primes):
                if a % (v * v) == 0:
                    mask = -1
                    break
                if a % v == 0:
                    mask |= 1 << i

            if mask >= 0:
                for i in range(1 << 10):
                    if i & mask == 0:
                        dp[i | mask] += dp[i]

        return (sum(dp) - 1) % MOD
        
# @lc code=end

