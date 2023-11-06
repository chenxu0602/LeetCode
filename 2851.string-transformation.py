#
# @lc app=leetcode id=2851 lang=python3
#
# [2851] String Transformation
#

# @lc code=start
class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:

        n = len(s)
        ss = s + s
        first = ss.find(t)
        if first == -1: return 0
        elif first == 0:
            zero_targets = 1
        else:
            zero_targets = 0

        period = ss.find(s, 1)
        frequency = len(s) // period
        nonzero_targets = frequency - zero_targets

        MOD = 10**9 + 7
        ways_0 = (pow(n - 1, k, MOD * n) + (n - 1) * ((-1) ** k)) // n
        ways_1 = (pow(n - 1, k, MOD * n) - ((-1) ** k)) // n

        return (zero_targets * ways_0 + nonzero_targets * ways_1) % MOD
        
# @lc code=end

