#
# @lc app=leetcode id=2582 lang=python3
#
# [2582] Pass the Pillow
#

# @lc code=start
class Solution:
    def passThePillow(self, n: int, time: int) -> int:

        # Going forward and back to the original position,
        # take n * 2 - 2 steps.

        return n - abs(n - 1 - time % (n * 2 - 2))
        
# @lc code=end

