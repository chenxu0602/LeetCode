#
# @lc app=leetcode id=3036 lang=python3
#
# [3036] Number of Subarrays That Match a Pattern II
#

# @lc code=start
class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:

        def lee_kmp(s):
            n = len(s)
            dp = [0] * n
            for i in range(1, n):
                v = dp[i - 1]
                while v and s[i] != s[v]:
                    v = dp[v - 1]
                dp[i] = v + (s[i] == s[v])
            return dp

        def cmp(a, b):
            return (a > b) - (a < b)

        A = list(map(cmp, nums[1:], nums[:-1]))
        dp = lee_kmp(pattern + [215] + A)
        return dp.count(len(pattern))
        
        
# @lc code=end

