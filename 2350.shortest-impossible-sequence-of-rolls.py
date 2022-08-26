#
# @lc app=leetcode id=2350 lang=python3
#
# [2350] Shortest Impossible Sequence of Rolls
#

# @lc code=start
class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        res = 1
        s = set()
        for r in rolls:
            s.add(r)
            if len(s) == k:
                res += 1
                s.clear()

        return res
        
# @lc code=end

