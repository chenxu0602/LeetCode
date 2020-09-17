#
# @lc app=leetcode id=915 lang=python3
#
# [915] Partition Array into Disjoint Intervals
#
# https://leetcode.com/problems/partition-array-into-disjoint-intervals/description/
#
# algorithms
# Medium (45.25%)
# Likes:    379
# Dislikes: 28
# Total Accepted:    21.3K
# Total Submissions: 46.9K
# Testcase Example:  '[5,0,3,8,6]'
#
# Given an array A, partition it into two (contiguous) subarrays left and right
# so that:
# 
# 
# Every element in left is less than or equal to every element in right.
# left and right are non-empty.
# left has the smallest possible size.
# 
# 
# Return the length of left after such a partitioning.  It is guaranteed that
# such a partitioning exists.
# 
# 
# 
# Example 1:
# 
# 
# Input: [5,0,3,8,6]
# Output: 3
# Explanation: left = [5,0,3], right = [8,6]
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,1,1,0,6,12]
# Output: 4
# Explanation: left = [1,1,1,0], right = [6,12]
# 
# 
# 
# 
# 
# Note:
# 
# 
# 2 <= A.length <= 30000
# 0 <= A[i] <= 10^6
# It is guaranteed there is at least one way to partition A as described.
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def partitionDisjoint(self, A: List[int]) -> int:
        # Next Array
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # N = len(A)
        # maxleft, minright = [None] * N, [None] * N

        # m = A[0]
        # for i in range(N):
        #     m = max(m, A[i])
        #     maxleft[i] = m

        # m = A[-1]
        # for i in range(N - 1, -1, -1):
        #     m = min(m, A[i])
        #     minright[i] = m

        # for i in range(1, N):
        #     if maxleft[i - 1] <= minright[i]:
        #         return i


        disjoint = 0
        v = A[disjoint]
        max_so_far = v
        for i in range(len(A)):
            max_so_far = max(max_so_far, A[i])
            if A[i] < v:
                disjoint = i
                v = max_so_far
        return disjoint + 1
        
# @lc code=end

