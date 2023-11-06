#
# @lc app=leetcode id=2825 lang=python3
#
# [2825] Make String a Subsequence Using Cyclic Increments
#

# @lc code=start
from string import ascii_lowercase

s = ascii_lowercase + 'a'
d = dict(zip(s[:-1], s[1:]))

class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:

        n1, n2 = map(len, (str1, str2))
        i1 = i2 = 0

        while i1 < n1 and i2 < n2:
            if str1[i1] == str2[i2] or d[str1[i1]] == str2[i2]:
                i2 += 1
            i1 += 1

        return i2 == n2
        
# @lc code=end

