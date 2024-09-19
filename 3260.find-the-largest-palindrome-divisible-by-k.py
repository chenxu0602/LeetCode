#
# @lc app=leetcode id=3260 lang=python3
#
# [3260] Find the Largest Palindrome Divisible by K
#

# @lc code=start
from functools import lru_cache

class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:

        # Let dp(i, r) be whether we can solve filling in ans[i:-i] with a prior digit sum of r mod K

        pow10 = [1] * n
        for i in range(1, n):
            pow10[i] = pow10[i - 1] * 10 % k

        ans = [9] * n

        @lru_cache(None)
        def dp(i, r):
            if i == (n + 1) // 2:
                return r == 0

            for d in range(9, -1, -1):
                ans[i] = ans[~i] = d
                coeff = sum(pow10[j] for j in {i, n - 1 - i})
                r2 = (r + coeff * d) % k
                if dp(i + 1, r2):
                    return True

            return False

        dp(0, 0)
        return ''.join(map(str, ans))
        
# @lc code=end

