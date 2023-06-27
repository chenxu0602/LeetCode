#
# @lc app=leetcode id=2745 lang=python3
#
# [2745] Construct the Longest New String
#

# @lc code=start
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:

        return 2 * (2 * min(x, y) + z + (1 if x != y else 0))
        
# @lc code=end

