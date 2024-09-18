#
# @lc app=leetcode id=3238 lang=python3
#
# [3238] Find the Number of Winning Players
#

# @lc code=start
from collections import Counter

class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:

        counts = Counter(map(tuple, pick))
        return len({player for (player, _), count in counts.items() if count > player})
        
# @lc code=end

