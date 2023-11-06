#
# @lc app=leetcode id=2810 lang=python3
#
# [2810] Faulty Keyboard
#

# @lc code=start
class Solution:
    def finalString(self, s: str) -> str:

        n = len(s)
        x = s[0]
        for i in range(1, n):
            if s[i] == 'i':
                x = x[::-1]
            else:
                x += s[i]

        return x 
        
# @lc code=end

