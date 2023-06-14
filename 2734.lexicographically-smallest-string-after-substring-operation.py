#
# @lc app=leetcode id=2734 lang=python3
#
# [2734] Lexicographically Smallest String After Substring Operation
#

# @lc code=start
class Solution:
    def smallestString(self, s: str) -> str:

        i, n, s = 0, len(s), list(s)
        while i < n and s[i] == 'a':
            i += 1
        if i == n:
            s[-1] = 'z'
        while i < n and s[i] != 'a':
            s[i] = chr(ord(s[i]) - 1)
            i += 1
        return "".join(s)
        
# @lc code=end

