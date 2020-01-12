#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (47.76%)
# Likes:    612
# Dislikes: 90
# Total Accepted:    155.5K
# Total Submissions: 316.6K
# Testcase Example:  '3'
#
# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n^2 in spiral order.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
# 
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        A, lo = [], n*n + 1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [list(range(lo, hi))] + [*zip(*A[::-1])]

        return A
        
# @lc code=end

