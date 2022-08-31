#
# @lc app=leetcode id=2376 lang=python3
#
# [2376] Count Special Integers
#

# @lc code=start
class Solution:
    def countSpecialNumbers(self, n: int) -> int:

        L = list(map(int, str(n + 1)))
        res, n = 0, len(L)

        def A(m, n):
            return 1 if n == 0 else A(m, n - 1) * (m - n + 1)

        for i in range(1, n):
            res += 9 * A(9, i - 1)

        s = set()
        for i, x in enumerate(L):
            for y in range(0 if i else 1, x):
                if y not in s:
                    res += A(9 - i, n - i - 1)
            if x in s: break
            s.add(x)

        return res
        
# @lc code=end

