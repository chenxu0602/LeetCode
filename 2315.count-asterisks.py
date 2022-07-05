#
# @lc app=leetcode id=2315 lang=python3
#
# [2315] Count Asterisks
#

# @lc code=start
class Solution:
    def countAsterisks(self, s: str) -> int:
        return sum([a.count('*') for a in s.split('|')][0::2])
        
# @lc code=end

