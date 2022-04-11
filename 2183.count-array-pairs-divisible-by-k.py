#
# @lc app=leetcode id=2183 lang=python3
#
# [2183] Count Array Pairs Divisible by K
#

# @lc code=start
from collections import Counter
import math

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # It can be shown that if n1 * n2 % k == 0, then gcd(n1, k) * gcd(n2, k) % k == 0.
        # res = 0
        # gcds = Counter()

        # for n in nums:
        #     gcd_i = math.gcd(n, k)
        #     for gcd_j, cnt in gcds.items():
        #         if gcd_i * gcd_j % k == 0:
        #             res += cnt
        #     gcds[gcd_i] += 1

        # return res


        cnt = Counter(math.gcd(n, k) for n in nums)
        res = 0
        for a in cnt:
            for b in cnt:
                if a <= b and a * b % k == 0:
                    res += cnt[a] * cnt[b] if a < b else cnt[a] * (cnt[b] - 1) // 2
        return res



        
# @lc code=end

