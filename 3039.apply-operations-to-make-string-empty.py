#
# @lc app=leetcode id=3039 lang=python3
#
# [3039] Apply Operations to Make String Empty
#

# @lc code=start
from collections import Counter

class Solution:
    def lastNonEmptyString(self, s: str) -> str:

        cnt, last = Counter(s), []
        mx = max(cnt.values())
        for c in reversed(s):
            if mx == cnt[c]:
                last += c,
                cnt[c] -= 1

        return ''.join(last[::-1])
        
# @lc code=end

