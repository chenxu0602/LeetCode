#
# @lc app=leetcode id=982 lang=python3
#
# [982] Triples with Bitwise AND Equal To Zero
#
# https://leetcode.com/problems/triples-with-bitwise-and-equal-to-zero/description/
#
# algorithms
# Hard (54.38%)
# Likes:    67
# Dislikes: 91
# Total Accepted:    5.5K
# Total Submissions: 10.2K
# Testcase Example:  '[2,1,3]'
#
# Given an array of integers A, find the number of triples of indices (i, j, k)
# such that:
# 
# 
# 0 <= i < A.length
# 0 <= j < A.length
# 0 <= k < A.length
# A[i] & A[j] & A[k] == 0, where & represents the bitwise-AND operator.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [2,1,3]
# Output: 12
# Explanation: We could choose the following i, j, k triples:
# (i=0, j=0, k=1) : 2 & 2 & 1
# (i=0, j=1, k=0) : 2 & 1 & 2
# (i=0, j=1, k=1) : 2 & 1 & 1
# (i=0, j=1, k=2) : 2 & 1 & 3
# (i=0, j=2, k=1) : 2 & 3 & 1
# (i=1, j=0, k=0) : 1 & 2 & 2
# (i=1, j=0, k=1) : 1 & 2 & 1
# (i=1, j=0, k=2) : 1 & 2 & 3
# (i=1, j=1, k=0) : 1 & 1 & 2
# (i=1, j=2, k=0) : 1 & 3 & 2
# (i=2, j=0, k=1) : 3 & 2 & 1
# (i=2, j=1, k=0) : 3 & 1 & 2
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 1000
# 0 <= A[i] < 2^16
# 
# 
#
from collections import Counter

class Solution:
    def countTriplets(self, A: List[int]) -> int:

        c = Counter(x & y for x in A for y in A)
        return sum(c[xy] for xy in c for z in A if xy & z == 0)
        

