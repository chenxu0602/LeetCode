#
# @lc app=leetcode id=3223 lang=python3
#
# [3223] Minimum Length of String After Operations
#

# @lc code=start
from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:

        mp = Counter(s)
        ans = 0
        for c, cnt in mp.items():
            ans += 1
            if cnt % 2 == 0:
                ans += 1
        return ans
        
# @lc code=end

