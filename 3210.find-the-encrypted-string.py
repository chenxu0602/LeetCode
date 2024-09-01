#
# @lc app=leetcode id=3210 lang=python3
#
# [3210] Find the Encrypted String
#

# @lc code=start
class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:

        n, t = len(s), list(s)
        for i in range(n):
            t[i] = s[(i + k) % n]
        return ''.join(t)
        
# @lc code=end

