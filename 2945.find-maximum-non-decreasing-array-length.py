#
# @lc app=leetcode id=2945 lang=python3
#
# [2945] Find Maximum Non-decreasing Array Length
#

# @lc code=start
from itertools import accumulate
from bisect import bisect_left
from collections import deque

class Solution:
    def findMaximumLength(self, nums: List[int]) -> int:

        """
        n = len(nums)
        last = [0] + [float('inf')] * n
        acc = [0]
        dp = [0] * (n + 1)
        for j in range(n):
            a = nums[j]
            acc += a + acc[-1],
            i = j
            while last[i] > acc[-1] - acc[i]:
                i -= 1

            last[j + 1] = acc[-1] - acc[i]
            dp[j + 1] = dp[i] + 1

        return dp[-1]
        """


        """
        # The sum of last group of elements is acc[j] - acc[i] = A[i] + ... + A[j - 1].
        # We will find the next shortest group starting from A[j] to A[k - 1]
        # to make it bigger than current group.
        # acc[j] - acc[i] <= acc[k] - acc[j]
        # so that acc[j] * 2 - acc[i] <= acc[k].

        # So we can apply binary search in acc array,
        # to find the lower bound index of acc[j] * 2 - acc[i].
        # And we assign pre[k] = j, which means
        # to make the k first element non-decreasing,
        # we need to at least to sum up A[j] + A[j + 1] + .. A[k - 1] to make it big enough.

        n = len(nums)
        acc = list(accumulate(nums, initial=0))
        pre = [0] * (n + 2)
        dp = [0] * (n + 1)
        i = 0
        for j, a in enumerate(nums, 1):
            i = max(i, pre[j])
            dp[j] = dp[i] + 1
            k = bisect_left(acc, acc[j] * 2 - acc[i])
            pre[k] = j

        return dp[n]
        """

        queue, d, s, S = deque(), 0, 0, 0
        for num in nums:
            S += num
            while queue and queue[0][0] <= S:
                _, d_, s_ = queue.popleft()
                if (d_, s_) >= (d, s): 
                    d, s = d_, s_
                
            while queue and queue[-1] > (2 * S - s, d + 1, S):
                queue.pop()

            queue += (2 * S - s, d + 1, S),

        return d + 1
        
# @lc code=end

