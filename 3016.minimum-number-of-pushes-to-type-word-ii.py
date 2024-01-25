#
# @lc app=leetcode id=3016 lang=python3
#
# [3016] Minimum Number of Pushes to Type Word II
#

# @lc code=start
from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:

        count = Counter(word)
        count = sorted(list(count.items()), key=lambda x: x[1], reverse=True)

        ans = 0
        for i in range(len(count)):
            ans += (i // 8 + 1) * count[i][1]

        return ans




# @lc code=end

