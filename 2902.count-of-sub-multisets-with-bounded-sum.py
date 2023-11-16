#
# @lc app=leetcode id=2902 lang=python3
#
# [2902] Count of Sub-Multisets With Bounded Sum
#

# @lc code=start
from collections import Counter

class Solution:
    def countSubMultisets(self, nums: List[int], l: int, r: int) -> int:

        # In this Knapsack DP problem,
        # dp[i] is the ways to sum up i.
        # dp[0] = 1 for empty set,
        # and we want to find sum(dp[l] + ... + dp[r]).

        # Iterate all items,
        # assume we have c item of size a,
        # iterate i from r to 1,
        # update dp[i] += dp[i - a] + dp[i - a * 2] + ...+ dp[i - a * c].

        # Improve the process of calculation,
        # with idea of sliding window by keep the sum of
        # dp[i - a] + ... + dp[i - a * c]

        # Time  complexity: O(rm)
        # Space complexity: O(r)
        # where m is the number of different nums[i],
        # sum >= (1 + m) * m / 2 so O(m) = O(sqrt(sum))

        MOD = 10**9 + 7
        dp = [1] + [0] * r
        count = Counter(nums)

        for a, c in count.items():
            for i in range(r, max(r - a, 0), -1):
                v = sum(dp[i - a * k] for k in range(c) if i >= a * k)
                for j in range(i, 0, -a):
                    v -= dp[j]
                    if j >= a * c: v += dp[j - a * c]
                    dp[j] = (dp[j] + v) % MOD

        return (count[0] + 1) * sum(dp[l:]) % MOD


        
# @lc code=end

