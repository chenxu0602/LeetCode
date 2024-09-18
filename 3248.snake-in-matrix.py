#
# @lc app=leetcode id=3248 lang=python3
#
# [3248] Snake in Matrix
#

# @lc code=start
class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:

        i = j = 0
        d = {
            'UP':     (-1, 0),
            'DOWN':   (1, 0),
            'LEFT':   (0, -1),
            'RIGHT':  (0, 1),
        }

        for cmd in commands:
            a, b = d[cmd]
            i += a
            j += b

        return i * n + j
        
# @lc code=end

