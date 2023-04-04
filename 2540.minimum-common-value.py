#
# @lc app=leetcode id=2540 lang=python3
#
# [2540] Minimum Common Value
#

# @lc code=start
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:

        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            
            if nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1

        return -1
        
# @lc code=end

