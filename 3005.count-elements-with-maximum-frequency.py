#
# @lc app=leetcode id=3005 lang=python3
#
# [3005] Count Elements With Maximum Frequency
#

# @lc code=start
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        d = Counter(nums)
        m = max(d.values())
        return m * sum(i == m for i in d.values())
        
# @lc code=end

