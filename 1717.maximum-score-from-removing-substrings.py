#
# @lc app=leetcode id=1717 lang=python3
#
# [1717] Maximum Score From Removing Substrings
#

# @lc code=start
from collections import Counter

class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = 'a', 'b'
        if x < y:
            x, y = y, x
            a, b = b, a

        seen = Counter()
        ans = 0

        for c in s + 'x':
            if c in 'ab':
                if c == b and 0 < seen[a]:
                    ans += x
                    seen[a] -= 1
                else:
                    seen[c] += 1
            else:
                ans += y * min(seen[a], seen[b])
                seen = Counter()

        return ans
        
# @lc code=end

