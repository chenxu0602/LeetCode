#
# @lc app=leetcode id=733 lang=python3
#
# [733] Flood Fill
#
# https://leetcode.com/problems/flood-fill/description/
#
# algorithms
# Easy (55.18%)
# Likes:    1354
# Dislikes: 198
# Total Accepted:    179.4K
# Total Submissions: 324K
# Testcase Example:  '[[1,1,1],[1,1,0],[1,0,1]]\n1\n1\n2'
#
# 
# An image is represented by a 2-D array of integers, each integer representing
# the pixel value of the image (from 0 to 65535).
# 
# Given a coordinate (sr, sc) representing the starting pixel (row and column)
# of the flood fill, and a pixel value newColor, "flood fill" the image.
# 
# To perform a "flood fill", consider the starting pixel, plus any pixels
# connected 4-directionally to the starting pixel of the same color as the
# starting pixel, plus any pixels connected 4-directionally to those pixels
# (also with the same color as the starting pixel), and so on.  Replace the
# color of all of the aforementioned pixels with the newColor.
# 
# At the end, return the modified image.
# 
# Example 1:
# 
# Input: 
# image = [[1,1,1],[1,1,0],[1,0,1]]
# sr = 1, sc = 1, newColor = 2
# Output: [[2,2,2],[2,2,0],[2,0,1]]
# Explanation: 
# From the center of the image (with position (sr, sc) = (1, 1)), all pixels
# connected 
# by a path of the same color as the starting pixel are colored with the new
# color.
# Note the bottom corner is not colored 2, because it is not 4-directionally
# connected
# to the starting pixel.
# 
# 
# 
# Note:
# The length of image and image[0] will be in the range [1, 50].
# The given starting pixel will satisfy 0  and 0 .
# The value of each color in image[i][j] and newColor will be an integer in [0,
# 65535].
# 
#

# @lc code=start
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # R, C = map(len, (image, image[0]))
        # color = image[sr][sc]
        # if color == newColor: return image
        # def dfs(r, c):
        #     if image[r][c] == color:
        #         image[r][c] = newColor
        #         if r >= 1: dfs(r - 1, c)
        #         if r + 1 < R: dfs(r + 1, c)
        #         if c >= 1: dfs(r, c - 1)
        #         if c + 1 < C: dfs(r, c + 1)

        # dfs(sr, sc)
        # return image


        if image[sr][sc] != newColor:
            old, image[sr][sc], m, n = image[sr][sc], newColor, len(image), len(image[0])
            for i, j in zip((sr + 1, sr - 1, sr, sr), (sc, sc, sc + 1, sc - 1)):
                if 0 <= i < m and 0 <= j < n and image[i][j] == old:
                    self.floodFill(image, i, j, newColor)

        return image
        
# @lc code=end

