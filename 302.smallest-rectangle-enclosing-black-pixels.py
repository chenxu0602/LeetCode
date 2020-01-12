#
# @lc app=leetcode id=302 lang=python3
#
# [302] Smallest Rectangle Enclosing Black Pixels
#
# https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/description/
#
# algorithms
# Hard (49.25%)
# Likes:    138
# Dislikes: 38
# Total Accepted:    22.9K
# Total Submissions: 46.4K
# Testcase Example:  '[["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]]\n0\n2'
#
# An image is represented by a binary matrix with 0 as a white pixel and 1 as a
# black pixel. The black pixels are connected, i.e., there is only one black
# region. Pixels are connected horizontally and vertically. Given the location
# (x, y) of one of the black pixels, return the area of the smallest
# (axis-aligned) rectangle that encloses all black pixels.
# 
# Example:
# 
# 
# Input:
# [
# ⁠ "0010",
# ⁠ "0110",
# ⁠ "0100"
# ]
# and x = 0, y = 2
# 
# Output: 6
# 
# 
#
class Solution:
    def search(self, i, j, check):
        while i != j:
            mid = (i + j) // 2
            if check(mid):
                j = mid
            else:
                i = mid + 1

        return i

    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        top = self.search(0, x, lambda mid: '1' in image[mid])
        bottom = self.search(x+1, len(image), lambda mid: '1' not in image[mid])
        left = self.search(0, y, lambda mid: any(image[k][mid] == '1' for k in range(top, bottom)))
        right = self.search(y+1, len(image[0]), lambda mid: all(image[k][mid] == '0' for k in range(top, bottom)))

        return (right - left) * (bottom - top)

        