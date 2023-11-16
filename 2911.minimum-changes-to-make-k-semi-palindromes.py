#
# @lc app=leetcode id=2911 lang=python3
#
# [2911] Minimum Changes to Make K Semi-palindromes
#

# @lc code=start
from functools import cache
from collections import defaultdict

class Solution:
    def minimumChanges(self, s: str, k: int) -> int:

        # div[len] is a list of all factors d of len,
        # where 1 <= d < len and len % d == 0.

        # dp(i, k) means the cost to split s[:i] (i first characters of s)
        # into k semi-palindromes.
        # We will try to split out all the suffixes of s[:i].

        # change(i, j) means the cost to make substring s[i:j] semi-palindrome.
        # semi(i, j, d) means the cost to make substring s[i:j] semi-palindrome with module by d.

        # Finally we return dp(n, k)

        div = defaultdict(lambda: [1])
        n = len(s)
        for d in range(2, n):
            for v in range(d + d, n + 1, d):
                div[v] += d,

        def change(i, j):
            return min(semi(i, j, d) for d in div[j - i])

        @cache
        def semi(i, j, d):
            if i >= j: return 0
            return semi(i + d, j - d, d) + sum(s[i + k] != s[j - d + k] for k in range(d))

        @cache
        def dp(i, k):
            if k == 1:
                return change(0, i)
            return min(dp(j, k - 1) + change(j, i) for j in range((k - 1) * 2, i - 1))

        return dp(n, k)
        
# @lc code=end

