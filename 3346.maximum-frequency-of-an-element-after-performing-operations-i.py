#
# @lc app=leetcode id=3346 lang=python3
#
# [3346] Maximum Frequency of an Element After Performing Operations I
#

# @lc code=start
from collections import Counter
from bisect import bisect_left

class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:

        """
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
        """


        nums.sort()
        count = Counter(nums)

        def maxFreq(target: int):
            left = bisect_left(nums, target - k)
            right = bisect_left(nums, target + k + 1)
            options = right - left - count[target]
            return min(options, numOperations) + count[target]

        ans = 0
        for i in range(1, max(nums) + 1):
            ans = max(ans, maxFreq(i))

        return ans



        
# @lc code=end

