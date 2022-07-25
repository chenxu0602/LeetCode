#
# @lc app=leetcode id=2338 lang=python3
#
# [2338] Count the Number of Ideal Arrays
#

# @lc code=start
from collections import Counter
from math import comb

class Solution:
    def idealArrays(self, n: int, maxValue: int) -> int:

        ans = maxValue
        freq = {x: 1 for x in range(1, maxValue + 1)}
        for k in range(1, n):
            temp = Counter()
            for x in freq:
                for m in range(2, maxValue // x + 1):
                    ans += comb(n - 1, k) * freq[x]
                    temp[m * x] += freq[x]

            freq = temp
            ans %= (10**9 + 7)

        return ans

        
# @lc code=end

