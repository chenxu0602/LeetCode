#
# @lc app=leetcode id=945 lang=python3
#
# [945] Minimum Increment to Make Array Unique
#
# https://leetcode.com/problems/minimum-increment-to-make-array-unique/description/
#
# algorithms
# Medium (43.37%)
# Likes:    217
# Dislikes: 10
# Total Accepted:    14K
# Total Submissions: 32.1K
# Testcase Example:  '[1,2,2]'
#
# Given an array of integers A, a move consists of choosing any A[i], and
# incrementing it by 1.
# 
# Return the least number of moves to make every value in A unique.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,2]
# Output: 1
# Explanation:  After 1 move, the array could be [1, 2, 3].
# 
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1,2,1,7]
# Output: 6
# Explanation:  After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
# It can be shown with 5 or less moves that it is impossible for the array to
# have all unique values.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= A.length <= 40000
# 0 <= A[i] < 40000
# 
# 
# 
# 
# 
#
from collections import Counter

class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        count = Counter(A)
        taken = []

        ans = 0
        for x in range(100000):
            if count[x] >= 2:
                taken.extend([x] * (count[x] - 1))
            elif taken and count[x] == 0:
                ans += x - taken.pop()
        return ans
        

