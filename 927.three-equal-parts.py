#
# @lc app=leetcode id=927 lang=python3
#
# [927] Three Equal Parts
#
# https://leetcode.com/problems/three-equal-parts/description/
#
# algorithms
# Hard (30.89%)
# Likes:    112
# Dislikes: 41
# Total Accepted:    4.7K
# Total Submissions: 15.3K
# Testcase Example:  '[1,0,1,0,1]'
#
# Given an array A of 0s and 1s, divide the array into 3 non-empty parts such
# that all of these parts represent the same binary value.
# 
# If it is possible, return any [i, j] with i+1 < j, such that:
# 
# 
# A[0], A[1], ..., A[i] is the first part;
# A[i+1], A[i+2], ..., A[j-1] is the second part, and
# A[j], A[j+1], ..., A[A.length - 1] is the third part.
# All three parts have equal binary value.
# 
# 
# If it is not possible, return [-1, -1].
# 
# Note that the entire part is used when considering what binary value it
# represents.  For example, [1,1,0] represents 6 in decimal, not 3.  Also,
# leading zeros are allowed, so [0,1,1] and [1,1] represent the same value.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,0,1,0,1]
# Output: [0,3]
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,1,0,1,1]
# Output: [-1,-1]
# 
# 
# 
# 
# Note:
# 
# 
# 3 <= A.length <= 30000
# A[i] == 0 or A[i] == 1
# 
# 
# 
# 
# 
#
class Solution:
    def threeEqualParts(self, A: List[int]) -> List[int]:

       IMP = [-1, -1]

       S = sum(A)
       if S % 3: return IMP
       T = S // 3
       if T == 0:
          return [0, len(A) - 1]

       breaks = []
       su = 0
       for i, x in enumerate(A):
          if x:
             su += x
             if su in {1, T+1, 2*T+1}:
                breaks.append(i)
             if su in {T, 2*T, 3*T}:
                breaks.append(i)

       i1, j1, i2, j2, i3, j3 = breaks
       if not A[i1:j1+1] == A[i2:j2+1] == A[i3:j3+1]:
          return [-1, -1]

       x = i2 - j1 - 1
       y = i3 - j2 - 1
       z = len(A) - j3 - 1

       if x < z or y < z: return IMP
       j1 += z
       j2 += z
       return [j1, j2+1]
        

