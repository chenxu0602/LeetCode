#
# @lc app=leetcode id=3269 lang=python3
#
# [3269] Constructing Two Increasing Arrays
#

# @lc code=start
from itertools import product

class Solution:
    def minLargest(self, nums1: List[int], nums2: List[int]) -> int:

        increment = lambda x, y: x + 1 + (x % 2 == y % 2)

        n1, n2 = map(len, (nums1, nums2))
        dp = [[float('inf')] * (n2 + 1) for _ in range(n1 + 1)]

        dp[0][0] = 0
        for  i in range(n1):
            dp[i + 1][0] = increment(dp[i][0], nums1[i])

        for j in range(n2):
            dp[0][j + 1] = increment(dp[0][j], nums2[j])

        for i, j in product(range(n1), range(n2)):
            dp[i + 1][j + 1] = min(increment(dp[i][j + 1], nums1[i]), increment(dp[i + 1][j], nums2[j]))

        
        return dp[n1][n2]

        
# @lc code=end

