#
# @lc app=leetcode id=3274 lang=python3
#
# [3274] Check if Two Chessboard Squares Have the Same Color
#

# @lc code=start
class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:

        one = ord(coordinate1[0]) + int(coordinate1[1])
        two = ord(coordinate2[0]) + int(coordinate2[1])
        return one % 2 == two % 2
        
# @lc code=end

