#
# @lc app=leetcode id=2262 lang=python3
#
# [2262] Total Appeal of A String
#

# @lc code=start
from collections import defaultdict

class Solution:
    def appealSum(self, s: str) -> int:

        """
        last, res = {}, 0
        for i, c in enumerate(s):
            last[c] = i + 1
            res += sum(last.values())
        return res
        """

        last = defaultdict(lambda: -1)
        res, n = 0, len(s)
        for i, c in enumerate(s):
            res += (i - last[c]) * (n - i)
            last[c] = i
        return res
        
# @lc code=end

