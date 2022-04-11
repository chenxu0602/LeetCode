#
# @lc app=leetcode id=2190 lang=python3
#
# [2190] Most Frequent Number Following Key In an Array
#

# @lc code=start
from collections import Counter

class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        c = Counter()
        for i, v in enumerate(nums):
            if v == key and i + 1 < len(nums):
                c[nums[i + 1]] += 1
        return c.most_common(1)[0][0]
        
# @lc code=end

