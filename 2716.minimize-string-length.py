#
# @lc app=leetcode id=2716 lang=python3
#
# [2716] Minimize String Length
#

# @lc code=start
class Solution:
    def minimizedStringLength(self, s: str) -> int:

        return len(set(s))
        
# @lc code=end

