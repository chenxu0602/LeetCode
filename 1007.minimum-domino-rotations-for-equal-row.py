#
# @lc app=leetcode id=1007 lang=python3
#
# [1007] Minimum Domino Rotations For Equal Row
#
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/description/
#
# algorithms
# Medium (50.28%)
# Likes:    462
# Dislikes: 138
# Total Accepted:    56.6K
# Total Submissions: 112.7K
# Testcase Example:  '[2,1,2,4,2,2]\n[5,2,6,2,3,2]'
#
# In a row of dominoes, A[i] and B[i] represent the top and bottom halves of
# the i-th domino.  (A domino is a tile with two numbers from 1 to 6 - one on
# each half of the tile.)
# 
# We may rotate the i-th domino, so that A[i] and B[i] swap values.
# 
# Return the minimum number of rotations so that all the values in A are the
# same, or all the values in B are the same.
# 
# If it cannot be done, return -1.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
# Output: 2
# Explanation: 
# The first figure represents the dominoes as given by A and B: before we do
# any rotations.
# If we rotate the second and fourth dominoes, we can make every value in the
# top row equal to 2, as indicated by the second figure.
# 
# 
# Example 2:
# 
# 
# Input: A = [3,5,1,2,3], B = [3,6,3,3,4]
# Output: -1
# Explanation: 
# In this case, it is not possible to rotate the dominoes to make one row of
# values equal.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A[i], B[i] <= 6
# 2 <= A.length == B.length <= 20000
# 
# 
#

# @lc code=start
from functools import reduce

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # Greedy
        # Time  complexity: O(N)
        # # Space complexity: O(1)
        # def check(x):
        #     # how many rotations should be done
        #     # to have all elements in A equal to x
        #     # and to have all elements in B equal to x
        #     rotations_a = rotations_b = 0
        #     for i in range(n):
        #         if A[i] != x and B[i] != x:
        #             return -1
        #         elif A[i] != x:
        #             rotations_a += 1
        #         elif B[i] != x:
        #             rotations_b += 1
        #     # min number of rotations to have all
        #     # elements equal to x in A or B
        #     return min(rotations_a, rotations_b)

        # n = len(A)
        # rotations = check(A[0])
        # if rotations != -1 or A[0] == B[0]:
        #     return rotations
        # else:
        #     return check(B[0])


        # for x in range(1, 7):
        #     if all(x in d for d in zip(A, B)):
        #         return len(A) - max(A.count(x), B.count(x))
        # return -1

        s = reduce(set.__and__, [set(d) for d in zip(A, B)])
        if not s: return -1
        x = s.pop()
        return len(A) - max(A.count(x), B.count(x))


            
        
# @lc code=end

