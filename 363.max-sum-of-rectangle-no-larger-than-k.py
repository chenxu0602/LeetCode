#
# @lc app=leetcode id=363 lang=python3
#
# [363] Max Sum of Rectangle No Larger Than K
#
# https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/
#
# algorithms
# Hard (37.28%)
# Likes:    809
# Dislikes: 59
# Total Accepted:    44.7K
# Total Submissions: 120K
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

# @lc code=start
import bisect

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        def maxSubArrayLessK(nums, k):
            cumset = [0]
            maxsum = -1 << 32
            cursum = 0

            for i in range(len(nums)):
                cursum += nums[i]
                idx = bisect.bisect_left(cumset, cursum - k)
                if 0 <= idx < len(cumset):
                    maxsum = max(maxsum, cursum - cumset[idx])

                bisect.insort(cumset, cursum)

            return maxsum

        if not matrix: return 0
        m, n = map(len, (matrix, matrix[0]))
        res = -1 << 32

        for left in range(n):
            cursums = [0] * m

            right = left
            while right < n:
                for i in range(m):
                    cursums[i] += matrix[i][right]

                curarrmax = maxSubArrayLessK(cursums, k)
                res = max(res, curarrmax)
                right += 1

        return res
        
# @lc code=end

