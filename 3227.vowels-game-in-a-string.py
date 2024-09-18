#
# @lc app=leetcode id=3227 lang=python3
#
# [3227] Vowels Game in a String
#

# @lc code=start
class Solution:
    def doesAliceWin(self, s: str) -> bool:

        for c in s:
            if c in 'aeiou':
                return True
        return False
        
# @lc code=end

