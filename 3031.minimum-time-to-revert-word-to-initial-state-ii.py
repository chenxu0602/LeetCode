#
# @lc app=leetcode id=3031 lang=python3
#
# [3031] Minimum Time to Revert Word to Initial State II
#

# @lc code=start
from itertools import count

class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:

        # return next(i for i in count(1) if word.startswith(word[i * k:]))

        # KMP
        n = len(word)
        dp = [0] * n
        v = 0

        for i in range(1, n):
            while v and word[i] != word[v]:
                v = dp[v - 1]

            v = dp[i] = v + (word[i] == word[v])

        while v and (n - v) % k > 0:
            v = dp[v - 1]

        return (n - v + k - 1) // k



        
# @lc code=end

