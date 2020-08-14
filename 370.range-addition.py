#
# @lc app=leetcode id=370 lang=python3
#
# [370] Range Addition
#
# https://leetcode.com/problems/range-addition/description/
#
# algorithms
# Medium (60.52%)
# Likes:    422
# Dislikes: 14
# Total Accepted:    25.2K
# Total Submissions: 41.6K
# Testcase Example:  '5\n[[1,3,2],[2,4,3],[0,2,-2]]'
#
# Assume you have an array of length n initialized with all 0's and are given k
# update operations.
# 
# Each operation is represented as a triplet: [startIndex, endIndex, inc] which
# increments each element of subarray A[startIndex ... endIndex] (startIndex
# and endIndex inclusive) with inc.
# 
# Return the modified array after all k operations were executed.
# 
# Example:
# 
# 
# Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
# Output: [-2,0,3,5,3]
# 
# 
# Explanation:
# 
# 
# Initial state:
# [0,0,0,0,0]
# 
# After applying operation [1,3,2]:
# [0,2,2,2,0]
# 
# After applying operation [2,4,3]:
# [0,2,5,5,3]
# 
# After applying operation [0,2,-2]:
# [-2,0,3,5,3]
# 
#
class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        # Range Caching
        # Time  complexity: O(n + k)
        # Space complexity: O(1)
        res = [0] * (length + 1)
        for start, end, inc in updates:
            res[start]   += inc
            res[end + 1] -= inc

        for i in range(1, length + 1):
            res[i] += res[i - 1]

        return res[:-1]



        

