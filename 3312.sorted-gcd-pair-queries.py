#
# @lc app=leetcode id=3312 lang=python3
#
# [3312] Sorted GCD Pair Queries
#

# @lc code=start
from math import gcd
from itertools import combinations, chain, accumulate
from collections import Counter, defaultdict
from bisect import bisect_right

N = 50001
divs = [[] for _ in range(N)]
for i in range(1, N):
    for j in range(i, N, i):
        divs[j] += i,

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:

        c = Counter(chain.from_iterable(divs[num] for num in nums))
        gcds = defaultdict(int)

        for f in sorted(c.keys(), reverse=True):
            nf = gcds[f] + c[f] * (c[f] - 1) // 2
            if not nf:
                del gcds[f]
                continue
            for ff in divs[f]:
                gcds[ff] -= nf
            gcds[f] = nf

        gcd_i = sorted(gcds.keys())
        gcd_ac = list(accumulate(gcds[i] for i in gcd_i))

        res = [gcd_i[bisect_right(gcd_ac, q)] for q in queries]

        return res



        
# @lc code=end

