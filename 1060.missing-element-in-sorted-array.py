#
# @lc app=leetcode id=1060 lang=python3
#
# [1060] Missing Element in Sorted Array
#
# https://leetcode.com/problems/missing-element-in-sorted-array/description/
#
# algorithms
# Medium (54.37%)
# Likes:    77
# Dislikes: 3
# Total Accepted:    2.7K
# Total Submissions: 5K
# Testcase Example:  '[4,7,9,10]\n1'
#
# Given a sorted array A of unique numbers, find the K-th missing number
# starting from the leftmost number of the array.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [4,7,9,10], K = 1
# Output: 5
# Explanation: 
# The first missing number is 5.
# 
# 
# Example 2:
# 
# 
# Input: A = [4,7,9,10], K = 3
# Output: 8
# Explanation: 
# The missing numbers are [5,6,8,...], hence the third missing number is 8.
# 
# 
# Example 3:
# 
# 
# Input: A = [1,2,4], K = 3
# Output: 6
# Explanation: 
# The missing numbers are [3,5,6,7,...], hence the third missing number is
# 6.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 50000
# 1 <= A[i] <= 1e7
# 1 <= K <= 1e8
# 
#
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:

        low, high = 0, len(nums) - 1
        while low < high:
            mid = (low + high + 1) // 2
            if nums[mid] - nums[0] - mid < k:
                low = mid
            else:
                high = mid - 1
        return nums[0] + low + k

        # missing = lambda idx: nums[idx] - nums[0] - idx
        # n = len(nums)
        # if k > missing(n-1):
        #     return nums[-1] + k - missing(n-1)

        # idx = 1
        # while missing(idx) < k:
        #     idx += 1

        # return nums[idx-1] + k - missing(idx-1)

        # missing = lambda idx: nums[idx] - nums[0] - idx
        # n = len(nums)
        # if k > missing(n-1):
        #     return nums[-1] + k - missing(n-1)

        # left, right = 0, n-1
        # while left < right:
        #     pivot = left + (right - left) // 2
        #     if missing(pivot) < k:
        #         left = pivot + 1
        #     else:
        #         right = pivot

        # return nums[left-1] + k - missing(left-1)




