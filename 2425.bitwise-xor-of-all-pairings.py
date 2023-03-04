#
# @lc app=leetcode id=2425 lang=python3
#
# [2425] Bitwise XOR of All Pairings
#

# @lc code=start
class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:

        x = y = 0
        for a in nums1:
            x ^= a 
        for b in nums2:
            y ^= b
        return (len(nums1) % 2 * y) ^ (len(nums2) % 2 * x)
        
# @lc code=end

