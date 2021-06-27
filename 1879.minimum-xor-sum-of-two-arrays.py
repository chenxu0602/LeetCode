#
# @lc app=leetcode id=1879 lang=python3
#
# [1879] Minimum XOR Sum of Two Arrays
#
# https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/description/
#
# algorithms
# Hard (35.40%)
# Likes:    224
# Dislikes: 6
# Total Accepted:    4.5K
# Total Submissions: 12.5K
# Testcase Example:  '[1,2]\n[2,3]'
#
# You are given two integer arrays nums1 and nums2 of length n.
# 
# The XOR sum of the two integer arrays is (nums1[0] XOR nums2[0]) + (nums1[1]
# XOR nums2[1]) + ... + (nums1[n - 1] XOR nums2[n - 1]) (0-indexed).
# 
# 
# For example, the XOR sum of [1,2,3] and [3,2,1] is equal to (1 XOR 3) + (2
# XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4.
# 
# 
# Rearrange the elements of nums2 such that the resulting XOR sum is
# minimized.
# 
# Return the XOR sum after the rearrangement.
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2], nums2 = [2,3]
# Output: 2
# Explanation: Rearrange nums2 so that it becomes [3,2].
# The XOR sum is (1 XOR 3) + (2 XOR 2) = 2 + 0 = 2.
# 
# Example 2:
# 
# 
# Input: nums1 = [1,0,3], nums2 = [5,3,4]
# Output: 8
# Explanation: Rearrange nums2 so that it becomes [5,4,3]. 
# The XOR sum is (1 XOR 5) + (0 XOR 4) + (3 XOR 3) = 4 + 4 + 0 = 8.
# 
# 
# 
# Constraints:
# 
# 
# n == nums1.length
# n == nums2.length
# 1 <= n <= 14
# 0 <= nums1[i], nums2[i] <= 10^7
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:

        # @lru_cache(None)
        # def dp(mask: int) -> int:
        #     i = bin(mask).count('1')
        #     if i >= len(nums1):
        #         return 0

        #     return min((nums1[i] ^ nums2[j]) + dp(mask + (1 << j))
        #                 for j in range(len(nums2)) if mask & (1 << j) == 0)

        # return dp(0)


        @lru_cache(None)
        def dp(mask, i):
            if i == len(nums1):
                return 0

            return min(dp(mask ^ (1 << j), i + 1) + (nums1[i] ^ nums2[j]) for j in range(len(nums2)) if mask & 1 << j)

        return dp((1 << len(nums1))  - 1, 0)
        
# @lc code=end

