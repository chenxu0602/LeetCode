#
# @lc app=leetcode id=3303 lang=python3
#
# [3303] Find the Occurrence of First Almost Equal Substring
#

# @lc code=start
class Solution:
    def minStartingIndex(self, s: str, pattern: str) -> int:

        def z_function(s: str):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1
            return z

        m, n = map(len, (s, pattern))
        z1 = z_function(pattern + s)
        z2 = z_function(pattern[::-1] + s[::-1])
        for i in range(m - n + 1):
            if z1[n + i] + 1 + z2[m - i] >= n:
                return i

        return -1
        
# @lc code=end

