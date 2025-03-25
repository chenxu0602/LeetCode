#
# @lc app=leetcode id=3334 lang=python3
#
# [3334] Find the Maximum Factor Score of Array
#

# @lc code=start
from collections import Counter
from math import gcd, lcm
from itertools import accumulate

class Solution:
    def maxScore(self, nums: List[int]) -> int:

        """
        n, ctr = len(nums), Counter(nums)
        mx = gcd(*nums) * lcm(*nums)

        if n > 1:
            for i in range(n):
                if ctr[nums[i]] > 1:
                    continue

                arr = nums[:i] + nums[i + 1:]
                mx = max(mx, gcd(*arr) * lcm(*arr))

        return mx
        """

        n, lcm_, gcd_ = len(nums), 1, 0
        ans = gcd(*nums) * lcm(*nums)

        pref_lcm = list(accumulate(nums[n - 1:0:-1], lcm, initial=1))[::-1]
        pref_gcd = list(accumulate(nums[n - 1:0:-1], gcd, initial=0))[::-1]

        for pref_lcm, pref_gcd, num in zip(pref_lcm, pref_gcd, nums):
            ans = max(ans, lcm(lcm_, pref_lcm) * gcd(gcd_, pref_gcd))
            lcm_, gcd_ = lcm(lcm_, num), gcd(gcd_, num)

        return ans



        
# @lc code=end

