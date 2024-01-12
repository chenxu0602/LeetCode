#
# @lc app=leetcode id=3001 lang=python3
#
# [3001] Minimum Moves to Capture The Queen
#

# @lc code=start
class Solution:
    def minMovesToCaptureTheQueen(self, a: int, b: int, c: int, d: int, e: int, f: int) -> int:

        if a == e:
            return 2 if c == a and (b < d < f or b > d > f) else 1

        if b == f:
            return 2 if d == f and (a < c < e or a > c > e) else 1

        if c + d == e + f:
            return 2 if a + b == c + d and (c < a < e or c > a > e) else 1

        if c - d == e - f:
            return 2 if a - b == c - d and (c < a < e or c > a > e) else 1

        return 2

        
# @lc code=end

