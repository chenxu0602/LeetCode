#
# @lc app=leetcode id=2499 lang=python3
#
# [2499] Minimum Total Cost to Make Arrays Unequal
#

# @lc code=start
from collections import Counter

class Solution:
    def minimumTotalCost(self, nums1: List[int], nums2: List[int]) -> int:

        n = len(nums1)
        indices = {i for i in range(n) if nums1[i] == nums2[i]}
        if not indices: return 0

        count = Counter(nums1[i] for i in indices)
        major = max(count, key=count.__getitem__)

        to_add = max(count[major] * 2 - len(indices), 0)

        for i in range(n):
            if to_add and nums1[i] != major != nums2[i] and i not in indices:
                to_add -= 1
                indices.add(i)

        return -1 if to_add else sum(indices)

        
# @lc code=end

