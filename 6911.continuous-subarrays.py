#
# @lc app=leetcode id=6911 lang=python3
#
# [6911] Continuous Subarrays
#

# @lc code=start
from collections import defaultdict, Counter

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:

        cnt = Counter()
        i = res = 0

        for j, num in enumerate(nums):
            cnt[num] += 1
            while max(cnt) - min(cnt) > 2:
                cnt[nums[i]] -= 1
                if cnt[nums[i]] == 0:
                    del cnt[nums[i]]

                i += 1

            res += j - i + 1

        return res
        
# @lc code=end

