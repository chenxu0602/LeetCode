#
# @lc app=leetcode id=2953 lang=python3
#
# [2953] Count Complete Substrings
#

# @lc code=start
from collections import deque, defaultdict

class Solution:
    def countCompleteSubstrings(self, word: str, k: int) -> int:

        q = defaultdict(deque)
        l = ans = 0
        for r, c in enumerate(word):
            q[c] += r,
            while (r > 0 and l < r and abs(ord(c) - ord(word[r - 1])) > 2) or len(q[c]) > k:
                q[word[l]].popleft()
                l += 1

            candidates = sorted((q[d][0] for d in q if len(q[d]) == k), reverse=True)
            ans += sum(1 for i, p in enumerate(candidates) if r + 1 - p == k * (i + 1))

        return ans
        
# @lc code=end

