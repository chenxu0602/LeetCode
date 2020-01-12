#
# @lc app=leetcode id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/
#
# algorithms
# Hard (35.13%)
# Likes:    410
# Dislikes: 34
# Total Accepted:    27.8K
# Total Submissions: 79K
# Testcase Example:  '[[1,0,1],[0,-2,3]]\n2'
#
# Given a non-empty 2D matrix matrix and an integer k, find the max sum of a
# rectangle in the matrix such that its sum is no larger than k.
# 
# Example:
# 
# 
# Input: matrix = [[1,0,1],[0,-2,3]], k = 2
# Output: 2 
# Explanation: Because the sum of rectangle [[0, 1], [-2, 3]] is
# 2,
# and 2 is the max number no larger than k (k = 2).
# 
# Note:
# 
# 
# The rectangle inside the matrix must have an area > 0.
# What if the number of rows is much larger than the number of columns?
# 
#
from bisect import bisect_left, bisect_right, insort

class Solution:

    def maxSubArrayLessK(self, nums, k):
        cumset = [0]
        maxsum = -1 << 32
        cursum = 0

        for i in range(len(nums)):
            cursum += nums[i]
            idx = bisect_left(cumset, cursum - k)
            if 0 <= idx < len(cumset):
                maxsum = max(maxsum, cursum - cumset[idx])

            insort(cumset, cursum)

        return maxsum


    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])

        res = -(1 << 32)

        for left in range(n):
            cursums = [0 for _ in range(m)]

            right = left
            while right < n:
                for i in range(m):
                    cursums[i] += matrix[i][right]

                curarrmax = self.maxSubArrayLessK(cursums, k)
                res = max(res, curarrmax)
                right += 1

        return res








