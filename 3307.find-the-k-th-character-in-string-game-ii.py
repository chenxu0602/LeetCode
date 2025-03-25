#
# @lc app=leetcode id=3307 lang=python3
#
# [3307] Find the K-th Character in String Game II
#

# @lc code=start
class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:

        res = (k - 1) & sum(v << i for i, v in enumerate(operations))
        return chr(ord('a') + res.bit_count() % 26)
        
# @lc code=end

