#
# @lc app=leetcode id=2958 lang=python3
#
# [2958] Length of Longest Subarray With at Most K Frequency
#

# @lc code=start
from collections import defaultdict, Counter

class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:

        freq = Counter()
        ans = left = 0
        for i, v in enumerate(nums):
            freq[v] += 1
            while freq[v] > k:
                freq[nums[left]] -= 1
                left += 1
            ans = max(ans, i - left + 1)

        return ans
        
# @lc code=end

