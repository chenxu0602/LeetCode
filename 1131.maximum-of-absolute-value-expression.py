#
# @lc app=leetcode id=1131 lang=python3
#
# [1131] Maximum of Absolute Value Expression
#
# https://leetcode.com/problems/maximum-of-absolute-value-expression/description/
#
# algorithms
# Medium (53.09%)
# Likes:    218
# Dislikes: 212
# Total Accepted:    9.5K
# Total Submissions: 18.2K
# Testcase Example:  '[1,2,3,4]\n[-1,4,5,6]'
#
# Given two arrays of integers with equal lengths, return the maximum value
# of:
# 
# |arr1[i] - arr1[j]| + |arr2[i] - arr2[j]| + |i - j|
# 
# where the maximum is taken over all 0 <= i, j < arr1.length.
# 
# 
# Example 1:
# 
# 
# Input: arr1 = [1,2,3,4], arr2 = [-1,4,5,6]
# Output: 13
# 
# 
# Example 2:
# 
# 
# Input: arr1 = [1,-2,-5,0,10], arr2 = [0,-2,-1,-7,-4]
# Output: 20
# 
# 
# 
# Constraints:
# 
# 
# 2 <= arr1.length == arr2.length <= 40000
# -10^6 <= arr1[i], arr2[i] <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
        # res, n = 0, len(arr1)
        # for p, q in (1, 1), (1, -1), (-1, 1), (-1, -1):
        #     closest = p * arr1[0] + q * arr2[0] + 0
        #     for i in range(n):
        #         cur = p * arr1[i] + q * arr2[i] + i
        #         res = max(res, cur - closest)
        #         closest = min(closest, cur)
        # return res


        M = 0
        for c in (1, 1), (1, -1), (-1, 1), (-1, -1):
            m = float("inf")
            for i in [arr1[i] * c[0] + arr2[i] * c[1] + i for i in range(len(arr1))]:
                if i < m:
                    m = i
                if i - m > M:
                    M = i - m
        return M
        
# @lc code=end

