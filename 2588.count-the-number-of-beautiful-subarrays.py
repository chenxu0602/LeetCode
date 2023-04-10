#
# @lc app=leetcode id=2588 lang=python3
#
# [2588] Count the Number of Beautiful Subarrays
#

# @lc code=start
from collections import Counter
from itertools import accumulate
from operator import xor

class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:

        # Prefix XOR
        # pre records the prefix xor, where pre[i] = pre[i - 1] ^ nums[i]
        # dp counts the frequency for prefix different value.
        # At first pre = 0, so we initialize dp[0] = 1.

        # dp = Counter({0: 1})
        # res = pre = 0
        # for x in nums:
        #     pre ^= x
        #     res += dp[pre]
        #     dp[pre] += 1
        # return res

        count = Counter(accumulate(nums, xor, initial=0))
        return sum(n * (n - 1) for n in count.values()) // 2
        
# @lc code=end

