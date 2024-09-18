#
# @lc app=leetcode id=3226 lang=python3
#
# [3226] Number of Bit Changes to Make Two Integers Equal
#

# @lc code=start
class Solution:
    def minChanges(self, n: int, k: int) -> int:

        if n & k != k: return -1
        return (n ^ k).bit_count()
        
# @lc code=end

