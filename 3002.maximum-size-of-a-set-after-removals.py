#
# @lc app=leetcode id=3002 lang=python3
#
# [3002] Maximum Size of a Set After Removals
#

# @lc code=start
class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:

        s1, s2 = set(nums1), set(nums2)
        n = len(nums1)
        inter = s1.intersection(s2)

        ex1 = min(len(s1) - len(inter), n // 2)
        ex2 = min(len(s2) - len(inter), n // 2)
        return min(ex1 + ex2 + len(inter), n)
        
# @lc code=end

