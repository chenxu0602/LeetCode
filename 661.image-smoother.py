#
# @lc app=leetcode id=661 lang=python3
#
# [661] Image Smoother
#
# https://leetcode.com/problems/image-smoother/description/
#
# algorithms
# Easy (49.08%)
# Likes:    188
# Dislikes: 847
# Total Accepted:    37.5K
# Total Submissions: 76.3K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a 2D integer matrix M representing the gray scale of an image, you need
# to design a smoother to make the gray scale of each cell becomes the average
# gray scale (rounding down) of all the 8 surrounding cells and itself.  If a
# cell has less than 8 surrounding cells, then use as many as you can.
# 
# Example 1:
# 
# Input:
# [[1,1,1],
# ⁠[1,0,1],
# ⁠[1,1,1]]
# Output:
# [[0, 0, 0],
# ⁠[0, 0, 0],
# ⁠[0, 0, 0]]
# Explanation:
# For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
# For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
# For the point (1,1): floor(8/9) = floor(0.88888889) = 0
# 
# 
# 
# Note:
# 
# The value in the given matrix is in the range of [0, 255].
# The length and width of the given matrix are in the range of [1, 150].
# 
# 
#
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        # Time  complexity: O(N)
        # Space complexity: O(N)
        R, C = map(len, (M, M[0]))
        ans = [[0] * C for _ in M]

        for r in range(R):
            for c in range(C):
                count = 0
                for nr in (r - 1, r, r + 1):
                    for nc in (c - 1, c, c + 1):
                        if 0 <= nr < R and 0 <= nc < C:
                            ans[r][c] += M[nr][nc]
                            count += 1
                ans[r][c] //= count

        return ans
        

