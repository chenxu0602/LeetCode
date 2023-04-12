#
# @lc app=leetcode id=2605 lang=python3
#
# [2605] Form Smallest Number From Two Digit Arrays
#

# @lc code=start
class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:

        s1, s2 = set(nums1), set(nums2)
        if s1 & s2:
            return min(s1 & s2)

        a, b = min(nums1), min(nums2)
        return min(a, b) * 10 + max(a, b)
        
# @lc code=end

