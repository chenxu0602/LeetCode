#
# @lc app=leetcode id=1289 lang=python3
#
# [1289] Minimum Falling Path Sum II
#
# https://leetcode.com/problems/minimum-falling-path-sum-ii/description/
#
# algorithms
# Hard (57.26%)
# Likes:    71
# Dislikes: 9
# Total Accepted:    4.2K
# Total Submissions: 7.3K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a square grid of integers arr, a falling path with non-zero shifts is a
# choice of exactly one element from each row of arr, such that no two elements
# chosen in adjacent rows are in the same column.
# 
# Return the minimum sum of a falling path with non-zero shifts.
# 
# 
# Example 1:
# 
# 
# Input: arr = [[1,2,3],[4,5,6],[7,8,9]]
# Output: 13
# Explanation: 
# The possible falling paths are:
# [1,5,9], [1,5,7], [1,6,7], [1,6,8],
# [2,4,8], [2,4,9], [2,6,7], [2,6,8],
# [3,4,8], [3,4,9], [3,5,7], [3,5,9]
# The falling path with the smallest sum is [1,5,7], so the answer is 13.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length == arr[i].length <= 200
# -99 <= arr[i][j] <= 99
# 
# 
#

# @lc code=start
import heapq

class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        # for i in range(1, len(arr)):
        #     r = heapq.nsmallest(2, arr[i - 1])
        #     for j in range(len(arr[0])):
        #         arr[i][j] += r[1] if arr[i - 1][j] == r[0] else r[0]
        # return min(arr[-1])


        r = [(0, -1)]
        for row in arr:
            r = heapq.nsmallest(2, ((a + r[i == r[0][1]][0], i) for i, a in enumerate(row)))
        return r[0][0]
        
# @lc code=end

