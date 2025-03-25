#
# @lc app=leetcode id=3333 lang=python3
#
# [3333] Find the Original Typed String II
#

# @lc code=start
from functools import reduce
from itertools import accumulate

class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:

        MOD = 10**9 + 7
        consecutive, prev = [1], word[0]

        for elem in word[1:]:
            if elem == prev:
                consecutive[-1] += 1
            else:
                consecutive += 1,
                prev = elem

        n = len(consecutive)

        prod = reduce(lambda x, acc: (x * acc) % MOD, consecutive)
        k -= len(consecutive)

        if k <= 0: return prod

        dp = [0] * k
        dp[0] = 1

        for group in consecutive:
            a = [0] * k

            for i in range(k):
                a[i] += dp[i]

                if i + group < k:
                    a[i + group] -= dp[i]

            dp = list(accumulate(a))

        return (prod - sum(dp)) % MOD


        
# @lc code=end

