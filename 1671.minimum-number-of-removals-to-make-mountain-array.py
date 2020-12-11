#
# @lc app=leetcode id=1671 lang=python3
#
# [1671] Minimum Number of Removals to Make Mountain Array
#
# https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description/
#
# algorithms
# Hard (46.50%)
# Likes:    154
# Dislikes: 0
# Total Accepted:    3.1K
# Total Submissions: 6.7K
# Testcase Example:  '[1,3,1]'
#
# You may recall that an array arr is a mountain array if and only if:
# 
# 
# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such
# that:
# 
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# 
# 
# 
# 
# Given an integer array nums​​​, return the minimum number of elements to
# remove to make nums​​​ a mountain array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,1]
# Output: 0
# Explanation: The array itself is a mountain array so we do not need to remove
# any elements.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,1,1,5,6,2,3,1]
# Output: 3
# Explanation: One solution is to remove the elements at indices 0, 1, and 5,
# making the array nums = [1,5,6,3,1].
# 
# 
# Example 3:
# 
# 
# Input: nums = [4,3,2,1,1,2,3,1]
# Output: 4
# 
# 
# Example 4:
# 
# 
# Input: nums = [1,2,3,4,4,3,2,1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 3 <= nums.length <= 1000
# 1 <= nums[i] <= 10^9
# It is guaranteed that you can make a mountain array out of nums.
# 
# 
#

# @lc code=start
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 3: return 0

        inc, dec = [0] * n, [0] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    inc[i] = max(inc[i], inc[j] + 1)

        for i in range(n - 2, -1, -1):
            for j in range(n - 1, i, -1):
                if nums[i] > nums[j]:
                    dec[i] = max(dec[i], dec[j] + 1)

        res = 0
        for i in range(n):
            if inc[i] > 0 and dec[i] > 0:
                res = max(res, inc[i] + dec[i])

        return n - res - 1

        
# @lc code=end

