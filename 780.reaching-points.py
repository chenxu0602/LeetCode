#
# @lc app=leetcode id=780 lang=python3
#
# [780] Reaching Points
#
# https://leetcode.com/problems/reaching-points/description/
#
# algorithms
# Hard (29.11%)
# Likes:    513
# Dislikes: 101
# Total Accepted:    20.9K
# Total Submissions: 70.8K
# Testcase Example:  '9\n5\n12\n8'
#
# A move consists of taking a point (x, y) and transforming it to either (x,
# x+y) or (x+y, y).
# 
# Given a starting point (sx, sy) and a target point (tx, ty), return True if
# and only if a sequence of moves exists to transform the point (sx, sy) to
# (tx, ty). Otherwise, return False.
# 
# 
# Examples:
# Input: sx = 1, sy = 1, tx = 3, ty = 5
# Output: True
# Explanation:
# One series of moves that transforms the starting point to the target is:
# (1, 1) -> (1, 2)
# (1, 2) -> (3, 2)
# (3, 2) -> (3, 5)
# 
# Input: sx = 1, sy = 1, tx = 2, ty = 2
# Output: False
# 
# Input: sx = 1, sy = 1, tx = 1, ty = 1
# Output: True
# 
# 
# 
# Note:
# 
# 
# sx, sy, tx, ty will all be integers in the range [1, 10^9].
# 
# 
#

# @lc code=start
class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        # Time  complexity: O(log(max(tx, ty)))
        # Space complexity: O(1)
        while tx >= sx and ty >= sy:
            if tx == ty:
                break
            elif tx > ty:
                if ty > sy:
                    tx %= ty
                else:
                    return (tx - sx) % ty == 0
            else:
                if tx > sx:
                    ty %= tx
                else:
                    return (ty - sy) % tx == 0

        return tx == sx and ty == sy


        # while sx < tx and sy < ty:
        #     tx, ty = tx % ty, ty % tx
        # return sx == tx and sy <= ty and (ty - sy) % sx == 0 \
        #     or sy == ty and sx <= tx and (tx - sx) % sy == 0
        
# @lc code=end

