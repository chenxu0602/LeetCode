#
# @lc app=leetcode id=2019 lang=python3
#
# [2019] The Score of Students Solving Math Expression
#

# @lc code=start
from functools import lru_cache

class Solution:
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return {int(s[i])}

            res = {}
            for m in range(i + 1, j, 2):
                for a in dp(i, m - 1):
                    for b in dp(m + 1, j):
                        cur = a * b if s[m] == '*' else a + b
                        if cur <= 1000:
                            res[cur] = 2

            return res


        res = {**dp(0, len(s) - 1), **{eval(s): 5}}
        return sum(res.get(a, 0) for a in answers)
        
# @lc code=end

