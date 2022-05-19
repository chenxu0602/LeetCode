#
# @lc app=leetcode id=1963 lang=python3
#
# [1963] Minimum Number of Swaps to Make the String Balanced
#

# @lc code=start
class Solution:
    def minSwaps(self, s: str) -> int:

        res, bal = 0, 0
        for c in s:
            bal += 1 if c == '[' else -1
            if bal == -1:
                res += 1
                bal = 1
        return res
        
# @lc code=end

