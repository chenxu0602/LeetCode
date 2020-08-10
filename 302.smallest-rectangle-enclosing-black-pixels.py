#
# @lc app=leetcode id=302 lang=python3
#
# [302] Smallest Rectangle Enclosing Black Pixels
#
# https://leetcode.com/problems/smallest-rectangle-enclosing-black-pixels/description/
#
# algorithms
# Hard (51.53%)
# Likes:    204
# Dislikes: 51
# Total Accepted:    28K
# Total Submissions: 54.2K
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

# @lc code=start
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        # Binary Search
        # Time  complexity: O(nlogm + mlogn)
        # Space complexity: O(1)
        def binarySearch(i, j, check):
            while i < j:
                mid = (i + j) // 2
                if check(mid):
                    j = mid
                else:
                    i = mid + 1
            return i

        top = binarySearch(0, x, lambda mid: '1' in image[mid]) 
        bottom = binarySearch(x + 1, len(image), lambda mid: '1' not in image[mid])
        left = binarySearch(0, y, lambda mid: any(image[k][mid] == '1' for k in range(top, bottom)))
        right = binarySearch(y + 1, len(image[0]), lambda mid: all(image[k][mid] == '0' for k in range(top, bottom)))

        return (right - left) * (bottom - top)
        
# @lc code=end

