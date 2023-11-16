#
# @lc app=leetcode id=2914 lang=python3
#
# [2914] Minimum Number of Changes to Make Binary String Beautiful
#

# @lc code=start
class Solution:
    def minChanges(self, s: str) -> int:

        return sum(s[i] != s[i + 1] for i in range(0, len(s) - 1, 2))
        
# @lc code=end

