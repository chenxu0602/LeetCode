#
# @lc app=leetcode id=3304 lang=python3
#
# [3304] Find the K-th Character in String Game I
#

# @lc code=start
class Solution:
    def kthCharacter(self, k: int) -> str:

        return chr(ord('a') + (k - 1).bit_count())

        
# @lc code=end

