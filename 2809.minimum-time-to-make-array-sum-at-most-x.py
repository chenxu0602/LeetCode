#
# @lc app=leetcode id=2809 lang=python3
#
# [2809] Minimum Time to Make Array Sum At Most x
#

# @lc code=start
class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:

        # Create a matrix with n rows and n columns. (To make it simpler, let indices start from 1 here).
        # The ith row and jth column is nums1[i] + nums2[i] * j, which is the value each number will be after j seconds.

        # The question changes into select j rows from the first j columns (one row per column), let the sum be s, we want sum(matrix[.][j]) - s <= x.
        # Here sum(matrix[.][j]) is the sum of all the values in jth column which is a constant = nums1[0..n - 1] + nums2[0..n - 1] * j and x is also a constant. So our goal is to make s as large as possible.

        # In general to select one column in each row can be solved by graph matching, but this question's constraints are too large to a graph matching algorithm.

        # We can use dyanmaic programming.

        # dp[i][j] means the maximum sum to select j columns from the first i rows (note j <= i).
        # dp[i][j] = max(dp[i - 1][j], dp[i][j - 1] + nums1[i] + j * nums2[i])
        # which is basically select the jth column or not.

        n = len(nums1)
        indices = list(range(n))
        s, d = 0, 0
        for i in range(n):
            s += nums1[i]
            d += nums2[i]

        if s <= x: return 0

        indices.sort(key=lambda i: nums2[i])

        dp = [0] * (n + 1)
        r = n + 1
        for i in range(1, n + 1):
            for j in range(min(i, r - 1), 0, -1):
                dp[j] = max(dp[j], dp[j - 1] + nums2[indices[i - 1]] * j + nums1[indices[i - 1]])
                if s + j * d - dp[j] <= x:
                    r = j

        return r if r <= n else -1

        
# @lc code=end

