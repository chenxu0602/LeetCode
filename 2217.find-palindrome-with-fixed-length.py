#
# @lc app=leetcode id=2217 lang=python3
#
# [2217] Find Palindrome With Fixed Length
#

# @lc code=start
import enum


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:

        base = 10 ** ((intLength - 1) // 2)
        res = [q - 1 + base for q in queries]

        for i, v in enumerate(res):
            v = str(v) + str(v)[-1 - intLength % 2::-1]
            res[i] = int(v) if len(v) == intLength else -1

        return res
        
# @lc code=end

