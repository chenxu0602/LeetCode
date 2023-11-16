#
# @lc app=leetcode id=2918 lang=python3
#
# [2918] Minimum Equal Sum of Two Arrays After Replacing Zeros
#

# @lc code=start
class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        # sa is the minimum total of array A
        # sb is the minimum total of array A

        # a0 is the number of 0 in A.
        # b0 is the number of 0 in B.

        # If sa < sb && a0 == 0, return -1.
        # If sa > sb && b0 == 0, return -1.
        s1 = sum(max(a, 1) for a in nums1)
        s2 = sum(max(b, 1) for b in nums2)
        if s1 < s2 and nums1.count(0) == 0: return -1
        if s1 > s2 and nums2.count(0) == 0: return -1
        return max(s1, s2)
        
# @lc code=end

