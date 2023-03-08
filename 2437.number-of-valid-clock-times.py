#
# @lc app=leetcode id=2437 lang=python3
#
# [2437] Number of Valid Clock Times
#

# @lc code=start
import re

class Solution:
    def countTime(self, time: str) -> int:
        pattern = time.replace('?', '.')
        return sum(
            re.fullmatch(pattern, f"{hour:02}:{minute:02}") is not None
            for hour in range(24)
            for minute in range(60)
        )
        
# @lc code=end

