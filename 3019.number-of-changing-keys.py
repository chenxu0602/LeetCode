#
# @lc app=leetcode id=3019 lang=python3
#
# [3019] Number of Changing Keys
#

# @lc code=start
class Solution:
    def countKeyChanges(self, s: str) -> int:

        cnt = 0
        for i in range(1, len(s)):
            x = ord(s[i]) - ord(s[i - 1])
            if x != 32 and x != -32 and x != 0:
                cnt += 1

        return cnt
        
# @lc code=end

