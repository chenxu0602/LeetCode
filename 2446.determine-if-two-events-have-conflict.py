#
# @lc app=leetcode id=2446 lang=python3
#
# [2446] Determine if Two Events Have Conflict
#

# @lc code=start
class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        return max(event1[0], event2[0]) <= min(event1[1], event2[1])
        
# @lc code=end

