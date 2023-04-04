#
# @lc app=leetcode id=2537 lang=python3
#
# [2537] Count the Number of Good Subarrays
#

# @lc code=start
from collections import Counter 

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:

        res = cur = i = 0
        count = Counter()

        for j in range(len(nums)):
            k -= count[nums[j]]
            count[nums[j]] += 1

            while k <= 0:
                count[nums[i]] -= 1
                k += count[nums[i]]
                i += 1

            res += i

        return res
        
# @lc code=end

