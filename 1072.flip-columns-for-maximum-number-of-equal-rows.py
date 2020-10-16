#
# @lc app=leetcode id=1072 lang=python3
#
# [1072] Flip Columns For Maximum Number of Equal Rows
#
# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/description/
#
# algorithms
# Medium (60.82%)
# Likes:    290
# Dislikes: 27
# Total Accepted:    11.4K
# Total Submissions: 18.6K
# Testcase Example:  '[[0,1],[1,1]]'
#
# Given a matrix consisting of 0s and 1s, we may choose any number of columns
# in the matrix and flip every cell in that column.  Flipping a cell changes
# the value of that cell from 0 to 1 or from 1 to 0.
# 
# Return the maximum number of rows that have all values equal after some
# number of flips.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: [[0,1],[1,1]]
# Output: 1
# Explanation: After flipping no values, 1 row has all values equal.
# 
# 
# 
# Example 2:
# 
# 
# Input: [[0,1],[1,0]]
# Output: 2
# Explanation: After flipping values in the first column, both rows have equal
# values.
# 
# 
# 
# Example 3:
# 
# 
# Input: [[0,0,0],[0,0,1],[1,1,0]]
# Output: 2
# Explanation: After flipping values in the first two columns, the last two
# rows have equal values.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= matrix.length <= 300
# 1 <= matrix[i].length <= 300
# All matrix[i].length's are equal
# matrix[i][j] is 0 or 1
# 
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict, Counter

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        # cache = defaultdict(int)
        # for row in matrix:
        #     vals, trans = [], []
        #     for c in row:
        #         vals.append(c)
        #         trans.append(1 - c)
        #     cache[str(vals)]  += 1
        #     cache[str(trans)] += 1
        # return max(cache.values())


        return max(Counter(tuple(x ^ r[0] for x in r) for r in matrix).values())
        
# @lc code=end

