#
# @lc app=leetcode id=3344 lang=python3
#
# [3344] Maximum Sized Array
#

# @lc code=start
from bisect import bisect_left, bisect_right
from collections import Counter

class Solution:

    def maxSizedArray(self, s: int) -> int:

        def check(n: int) -> int:
            res = 0
            for bit in range(n.bit_length()):
                cnt = n >> bit + 1 << bit
                if n & 1 << bit:
                    cnt += n & (1 << bit) - 1
                res += (n ** 2 - (n - cnt) ** 2) << bit
            res *= n * (n - 1) // 2
            return res

        return bisect_right(range(s + 1), s, key=check) - 1 if s else 1

        # l, r = 1, 1196
        # cac = {}

        # while l < r:
        #     mid = (l + r + 1) // 2

        #     if mid not in cac:
        #         ct = Counter()
        #         for j in range(1, mid):
        #             while j:
        #                 vb = j & -j
        #                 ct[vb] += 1
        #                 j -= vb

        #         cac[mid] = 0
        #         for vb in ct:
        #             cac[mid] += vb * (mid ** 2 - (mid - ct[vb]) ** 2)
                
        #         cac[mid] *= mid * (mid - 1) // 2

        #     if cac[mid] <= s:
        #         l = mid
        #     else:
        #         r = mid - 1

        # return l

        
# @lc code=end

