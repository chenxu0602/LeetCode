#
# @lc app=leetcode id=2564 lang=python3
#
# [2564] Substring XOR Queries
#

# @lc code=start
from collections import defaultdict

class Solution:
    def substringXorQueries(self, s: str, queries: List[List[int]]) -> List[List[int]]:

        # val ^ first == second
        # val ^ first ^ first == second ^ first
        # val == second ^ first

        """
        res = []
        for fir, sec in queries:
            x = bin(sec ^ fir)[2:]
            i = s.find(x)
            res += [[-1, -1]] if i < 0 else [[i , i + len(x) - 1]]
        return res
        """

        n = len(s)
        seen = defaultdict(lambda: [-1, -1])
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                seen[0] = [i, i]
                continue

            v = 0
            for j in range(i, n):
                v = v * 2 + int(s[j])
                if v > 2 ** 32: break
                seen[v] = [i, j]

        return [seen[sec ^ fir] for fir, sec in queries]


        
# @lc code=end

