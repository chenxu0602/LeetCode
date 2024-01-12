#
# @lc app=leetcode id=2947 lang=python3
#
# [2947] Count Beautiful Substrings I
#

# @lc code=start
class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:

        n = len(s)
        res = 0
        cc = ['a', 'e', 'i', 'o', 'u']

        for j in range(n):
            c = v = 0
            for i in range(j, n):
                if s[i] in cc:
                    v += 1
                else:
                    c += 1

                if c == v and (c * v) % k == 0:
                    res += 1

        return res
        
# @lc code=end

