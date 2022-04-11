#
# @lc app=leetcode id=2200 lang=python3
#
# [2200] Find All K-Distant Indices in an Array
#

# @lc code=start
from bisect import bisect_left

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:

        res = set()
        for i in range(len(nums)):
            if nums[i] == key:
                for j in range(max(0, i - k), min(i + k + 1, len(nums))):
                    res.add(j)

        return sorted(res)
        
# @lc code=end

