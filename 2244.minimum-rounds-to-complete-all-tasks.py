#
# @lc app=leetcode id=2244 lang=python3
#
# [2244] Minimum Rounds to Complete All Tasks
#

# @lc code=start
from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = Counter(tasks).values()
        return -1 if 1 in freq else sum((f + 2) // 3 for f in freq)
        
# @lc code=end

