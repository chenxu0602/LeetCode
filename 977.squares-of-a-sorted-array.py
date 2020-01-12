#
# @lc app=leetcode id=977 lang=python3
#
# [977] Squares of a Sorted Array
#
# https://leetcode.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (71.82%)
# Likes:    510
# Dislikes: 55
# Total Accepted:    112.6K
# Total Submissions: 157K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# Given an array of integers A sorted in non-decreasing order, return an array
# of the squares of each number, also in sorted non-decreasing order.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# 
# 
# 
# Example 2:
# 
# 
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.
# 
# 
# 
#
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        N = len(A)

        if A[0]*A[-1] >= 0:
            if A[0] >= 0:
                return [x**2 for x in A]
            else:
                return [x**2 for x in reversed(A)]


        j = 0
        while j < N and A[j] < 0:
            j += 1
        i = j - 1

        ans = []
        while 0 <= i and j < N:
            if A[i]**2 < A[j]**2:
                ans.append(A[i]**2)
                i -= 1
            else:
                ans.append(A[j]**2)
                j += 1

        while i >= 0:
            ans.append(A[i]**2)
            i -= 1

        while j < N:
            ans.append(A[j]**2)
            j += 1

        return ans
        

