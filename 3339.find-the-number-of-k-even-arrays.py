#
# @lc app=leetcode id=3339 lang=python3
#
# [3339] Find the Number of K-Even Arrays
#

# @lc code=start
from math import comb

class Solution:
    def countOfArrays(self, n: int, m: int, k: int) -> int:

        """
        o, e, MOD = (m + 1) // 2, m // 2, 10**9 + 7
        res = 0

        # corner case: when there's no even sections (x == 0), all numbers are odd
        if k == 0: res += pow(o, n, MOD)

        # Number of ways to arrange even sections   *
        # Number of ways to arrange odd sections    *
        # Number of ways to choose even numbers     *
        # Number of ways to choose odd numbers  % mod
        for i in range(1, (n + 1 - k) // 2 + 1):
            res += comb(i + k - 1, i - 1) * comb(n - i - k + 1, i) \
                * pow(e, i + k, MOD) * pow(o, n - i - k, MOD) % MOD

        return res % MOD
        """

        """
        o, e, MOD = (m + 1) // 2, m // 2, 10**9 + 7
        op, ep, fac = [1], [1], [1]
        for i in range(n):
            op  += op[-1] * o % MOD,
            ep  += ep[-1] * e % MOD,
            fac += fac[-1] * (i + 1) % MOD,

        res = 0
        if k == 0: res += op[n]

        for i in range(1, (n + 1 - k) // 2 + 1):
            res += ep[i + k] * op[n - i - k] \
                * fac[i + k - 1] * pow(fac[i - 1] * fac[k], MOD - 2, MOD) \
                * fac[n - i - k + 1] * pow(fac[i] * fac[n - k + 1 - 2 * i], MOD - 2, MOD) % MOD

        return res % MOD
        """

        o, e, MOD = (m + 1) // 2, m // 2, 10**9 + 7
        dpOdd, dpEvn = [o] + [0] * k, [e] + [0] * (k + 1)

        for _ in range(n - 1):
            for i in range(k, -1, -1):
                dpOdd[i], dpEvn[i] = \
                    (dpOdd[i] + dpEvn[i]) * o % MOD, \
                    (dpOdd[i] + dpEvn[i - 1]) * e % MOD

        return (dpOdd[k] + dpEvn[k]) % MOD

        
# @lc code=end

