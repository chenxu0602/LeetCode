#
# @lc app=leetcode id=2968 lang=python3
#
# [2968] Apply Operations to Maximize Frequency Score
#

# @lc code=start
from itertools import accumulate

class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:

        """
        n = len(nums)
        acc = list(accumulate(sorted(nums), initial=0))
        l, r = 1, n
        while l < r:
            m = (l + r + 1) // 2
            for i in range(n - m + 1):
                if (acc[i + m] - acc[i + (m + 1) // 2]) - (acc[i + m // 2] - acc[i]) <= k:
                    l = m
                    break
            else:
                r = m - 1

        return l
        """

        i = 0
        nums.sort()
        for j in range(len(nums)):
            k -= nums[j] - nums[(i + j) // 2]
            if k < 0:
                k += nums[(i + j + 1) // 2] - nums[i]
                i += 1

        return j - i + 1
        
# @lc code=end

