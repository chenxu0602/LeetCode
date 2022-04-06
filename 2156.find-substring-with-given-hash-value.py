#
# @lc app=leetcode id=2156 lang=python3
#
# [2156] Find Substring With Given Hash Value
#

# @lc code=start
class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:

        def val(c): return ord(c) - ord('a') + 1

        res = n = len(s)
        pk = pow(power, k, modulo)
        cur = 0

        for i in range(n - 1, -1, -1):
            cur = (cur * power + val(s[i])) % modulo

            if i + k < n:
                cur = (cur - val(s[i + k]) * pk) % modulo

            if cur == hashValue:
                res = i

        return s[res:res + k]
        
# @lc code=end

