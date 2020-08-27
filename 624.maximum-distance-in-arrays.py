#
# @lc app=leetcode id=624 lang=python3
#
# [624] Maximum Distance in Arrays
#
# https://leetcode.com/problems/maximum-distance-in-arrays/description/
#
# algorithms
# Easy (38.83%)
# Likes:    354
# Dislikes: 50
# Total Accepted:    19.9K
# Total Submissions: 51.1K
# Testcase Example:  '[[1,2,3],[4,5],[1,2,3]]'
#
# 
# Given m arrays, and each array is sorted in ascending order. Now you can pick
# up two integers from two different arrays (each array picks one) and
# calculate the distance. We define the distance between two integers a and b
# to be their absolute difference |a-b|. Your task is to find the maximum
# distance.
# 
# 
# Example 1:
# 
# Input: 
# [[1,2,3],
# ⁠[4,5],
# ⁠[1,2,3]]
# Output: 4
# Explanation: 
# One way to reach the maximum distance 4 is to pick 1 in the first or third
# array and pick 5 in the second array.
# 
# 
# 
# Note:
# 
# Each given array will have at least 1 number. There will be at least two
# non-empty arrays.
# The total number of the integers in all the m arrays will be in the range of
# [2, 10000].
# The integers in the m arrays will be in the range of [-10000, 10000].
# 
# 
#

# @lc code=start
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        # Time  complexity: O(n)
        # Space complexity: O(n)
        min_val, max_val = arrays[0][0], arrays[0][-1]
        res = 0
        for i in range(1, len(arrays)):
            res = max(res, arrays[i][-1] - min_val, max_val - arrays[i][0])
            min_val = min(min_val, arrays[i][0])
            max_val = max(max_val, arrays[i][-1])

        return res

        
# @lc code=end

