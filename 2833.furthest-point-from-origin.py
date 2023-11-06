#
# @lc app=leetcode id=2833 lang=python3
#
# [2833] Furthest Point From Origin
#

# @lc code=start
from collections import Counter

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        count = Counter(moves)
        return abs(count['L'] - count['R']) + count['_']
        
# @lc code=end

