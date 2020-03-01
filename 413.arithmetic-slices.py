#
# @lc app=leetcode id=413 lang=python3
#
# [413] Arithmetic Slices
#
# https://leetcode.com/problems/arithmetic-slices/description/
#
# algorithms
# Medium (56.98%)
# Likes:    786
# Dislikes: 148
# Total Accepted:    76.8K
# Total Submissions: 134.8K
# Testcase Example:  '[1,2,3,4]'
#
# A sequence of number is called arithmetic if it consists of at least three
# elements and if the difference between any two consecutive elements is the
# same.
# 
# For example, these are arithmetic sequence:
# 1, 3, 5, 7, 9
# 7, 7, 7, 7
# 3, -1, -5, -9
# 
# The following sequence is not arithmetic. 1, 1, 2, 5, 7 
# 
# 
# A zero-indexed array A consisting of N numbers is given. A slice of that
# array is any pair of integers (P, Q) such that 0 
# 
# A slice (P, Q) of array A is called arithmetic if the sequence:
# ⁠   A[P], A[p + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this
# means that P + 1 < Q.
# 
# The function should return the number of arithmetic slices in the array A. 
# 
# 
# Example:
# 
# A = [1, 2, 3, 4]
# 
# return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3,
# 4] itself.
# 
#

# @lc code=start
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:

        # count, s = 0, 0
        # for i in range(2, len(A)):
        #     if A[i] - A[i-1] == A[i-1] - A[i-2]:
        #         count += 1
        #     else:
        #         s += (count + 1) * count // 2
        #         count = 0
        # s += (count + 1) * count // 2
        # return s

        # dp = [0] * len(A)
        # s = 0
        # for i in range(2, len(A)):
        #     if A[i] - A[i-1] == A[i-1] - A[i-2]:
        #         dp[i] = 1 + dp[i-1]
        # return sum(dp)

        dp, s = 0, 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp += 1
                s += dp
            else:
                dp = 0
        return s
        
        
# @lc code=end

