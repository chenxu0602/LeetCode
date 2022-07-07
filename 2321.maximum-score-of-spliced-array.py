#
# @lc app=leetcode id=2321 lang=python3
#
# [2321] Maximum Score Of Spliced Array
#

# @lc code=start

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:

        def kadane(A, B):
            res = cur = 0
            for i in range(len(A)):
                cur = max(0, cur + A[i] - B[i])
                res = max(res, cur)
            return res + sum(B)

        return max(kadane(nums1, nums2), kadane(nums2, nums1))
        
# @lc code=end

