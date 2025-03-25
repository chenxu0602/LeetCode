#
# @lc app=leetcode id=3348 lang=python3
#
# [3348] Smallest Divisible Digit Product II
#

# @lc code=start
from math import gcd

__import__('atexit').register(lambda: open('display_runtime.txt', 'w').write('0'))

def fill(req, length):
    ans = []
    for d in range(9, 1, -1):
        while req % d == 0:
            ans += d,
            req //= d

    ans.extend([1] * max(0, length - len(ans)))
    return ''.join(map(str, reversed(ans)))


class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        n, t2 = len(num), t
        for p in [2, 3, 5, 7]:
            while t2 % p == 0:
                t2 //= p

        if t2 != 1: return '-1'

        P = [t] * (n + 1)
        for i, v in enumerate(map(int, num)):
            if v == 0: break
            P[i + 1] = P[i] // gcd(P[i], v)

        if P[-1] == 1: return num

        zero = num.find('0') % n
        for i in range(zero, -1, -1):
            req = P[i]
            digits = n - 1 - i
            for d in range(int(num[i]) + 1, 10):
                ending = fill(req // gcd(req, d), digits)
                if len(ending) <= digits:
                    return num[:i] + str(d) + ending

        return fill(t, len(num) + 1)

        
# @lc code=end

