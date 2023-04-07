#
# @lc app=leetcode id=2555 lang=python3
#
# [2555] Maximize Win From Two Segments
#

# @lc code=start
class Solution:
    def maximizeWin(self, prizePositions: List[int], k: int) -> int:

        # Maintain a sliding segment(sliding window),
        # where A[i] - A[j] <= k.

        # dp[k] means the the maximum number
        # we can cover if you choose the one segments optimally
        # in the first k elements.

        # When we slide a segment from left to right,
        # the number of elements that we cover is i - j + 1
        # and in the first j elements,
        # we can cover at most dp[j] elements,
        # so we can cover i - j + 1 + dp[j] in total.
        # Update the result res and finally return it.k

        dp = [0] * (len(prizePositions) + 1)
        res = j = 0
        for i, a in enumerate(prizePositions):
            while prizePositions[j] < prizePositions[i] - k:
                j += 1

            dp[i + 1] = max(dp[i], i - j + 1)
            res = max(res, i - j + 1 + dp[j])

        return res
        
# @lc code=end

