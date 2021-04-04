#
# @lc app=leetcode id=1812 lang=python3
#
# [1812] Determine Color of a Chessboard Square
#
# https://leetcode.com/problems/determine-color-of-a-chessboard-square/description/
#
# algorithms
# Easy (75.32%)
# Likes:    18
# Dislikes: 0
# Total Accepted:    3.9K
# Total Submissions: 5.2K
# Testcase Example:  '"a1"'
#
# You are given coordinates, a string that represents the coordinates of a
# square of the chessboard. Below is a chessboard for your reference.
# 
# 
# 
# Return true if the square is white, and false if the square is black.
# 
# The coordinate will always represent a valid chessboard square. The
# coordinate will always have the letter first, and the number second.
# 
# 
# Example 1:
# 
# 
# Input: coordinates = "a1"
# Output: false
# Explanation: From the chessboard above, the square with coordinates "a1" is
# black, so return false.
# 
# 
# Example 2:
# 
# 
# Input: coordinates = "h3"
# Output: true
# Explanation: From the chessboard above, the square with coordinates "h3" is
# white, so return true.
# 
# 
# Example 3:
# 
# 
# Input: coordinates = "c7"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# coordinates.length == 2
# 'a' <= coordinates[0] <= 'h'
# '1' <= coordinates[1] <= '8'
# 
# 
#

# @lc code=start
class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        x = ord(coordinates[0]) - ord('a')
        y = ord(coordinates[1]) - ord('1')
        return (x + y) % 2
        
# @lc code=end

