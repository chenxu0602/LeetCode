#
# @lc app=leetcode id=2934 lang=python3
#
# [2934] Minimum Operations to Maximize Last Elements in Arrays
#

# @lc code=start
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:

        # dp1 means the result with A[n-1] and B[n-1] not swapped.
        # dp2 means the result with A[n-1] and B[n-1] swapped.
        dp1 = dp2 = 0
        for n1, n2 in zip(nums1, nums2):
            if max(n1, n2) > max(nums1[-1], nums2[-1]): return -1
            if min(n1, n2) > min(nums1[-1], nums2[-1]): return -1
            if n1 > nums1[-1] or n2 > nums2[-1]: dp1 += 1
            if n1 > nums2[-1] or n2 > nums1[-1]: dp2 += 1

        return min(dp1, dp2)
        
# @lc code=end

