#
# @lc app=leetcode id=713 lang=python3
#
# [713] Subarray Product Less Than K
#
# https://leetcode.com/problems/subarray-product-less-than-k/description/
#
# algorithms
# Medium (39.09%)
# Likes:    1461
# Dislikes: 64
# Total Accepted:    64.2K
# Total Submissions: 163.9K
# Testcase Example:  '[10,5,2,6]\n100'
#
# Your are given an array of positive integers nums.
# Count and print the number of (contiguous) subarrays where the product of all
# the elements in the subarray is less than k.
# 
# Example 1:
# 
# Input: nums = [10, 5, 2, 6], k = 100
# Output: 8
# Explanation: The 8 subarrays that have product less than 100 are: [10], [5],
# [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
# Note that [10, 5, 2] is not included as the product of 100 is not strictly
# less than k.
# 
# 
# 
# Note:
# 0 < nums.length .
# 0 < nums[i] < 1000.
# 0 .
# 
#

# @lc code=start
import math, bisect, itertools

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # Binary Search on Logarithms
        # Time  complexity: O(NlogN)
        # Space complexity: O(N)
        # if k == 0: return 0
        # k = math.log(k)

        # prefix = [0]
        # for x in nums:
        #     prefix += prefix[-1] + math.log(x),

        # ans = 0
        # for i, x in enumerate(prefix):
        #     j = bisect.bisect_left(prefix, x + k - 1e-9, i + 1)
        #     ans += j - i - 1
        
        # return ans


        # Sliding Window
        # Time  complexity: O(N)
        # Space complexity: O(N)
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left + 1
        return ans
        
# @lc code=end

