#
# @lc app=leetcode id=2541 lang=python3
#
# [2541] Minimum Operations to Make Array Equal II
#

# @lc code=start
class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:

        if k == 0:
            return 0 if nums1 == nums2 else -1
        
        ops = bal = 0
        for a, b in zip(nums1, nums2):
            if (a - b) % k != 0:
                return -1
            
            bal += a - b
            if a > b:
                ops += (a - b) // k

        return ops if bal == 0 else -1

        
# @lc code=end

