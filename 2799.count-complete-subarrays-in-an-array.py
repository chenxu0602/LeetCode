#
# @lc app=leetcode id=2799 lang=python3
#
# [2799] Count Complete Subarrays in an Array
#

# @lc code=start
from collections import Counter

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:

        complete = 0
        n = len(nums)
        k = len(set(nums))
        count = Counter()
        i = 0

        for j in range(n):
            count[nums[j]] += 1

            while len(count) == k:
                complete += n - j
                count[nums[i]] -= 1

                if not count[nums[i]]:
                    count.pop(nums[i])

                i += 1

        return complete
        
# @lc code=end

