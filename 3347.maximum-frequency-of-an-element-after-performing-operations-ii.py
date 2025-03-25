#
# @lc app=leetcode id=3347 lang=python3
#
# [3347] Maximum Frequency of an Element After Performing Operations II
#

# @lc code=start
from collections import Counter

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:

        nums.sort()
        n = len(nums)

        count = Counter()
        res = i = j = 0
        for num in nums:
            while j < n and nums[j] <= num + k:
                count[nums[j]] += 1
                j += 1

            while i < n and nums[i] < num - k:
                count[nums[i]] -= 1
                i += 1

            cur = min(j - i, count[num] + numOperations)
            res = max(res, cur)

        i = 0
        for j in range(n):
            while nums[i] + k + k < nums[j]:
                i += 1
            res = max(res, min(j - i + 1, numOperations))

        return res
        
# @lc code=end

