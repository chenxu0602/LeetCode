#
# @lc app=leetcode id=2870 lang=python3
#
# [2870] Minimum Number of Operations to Make Array Empty
#

# @lc code=start
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        count = Counter(nums)
        if count.most_common()[-1][1] == 1:
            return -1
        
        return sum((val - 1) // 3 + 1 for val in count.values())
        
# @lc code=end

