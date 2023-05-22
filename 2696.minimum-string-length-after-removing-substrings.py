#
# @lc app=leetcode id=2696 lang=python3
#
# [2696] Minimum String Length After Removing Substrings
#

# @lc code=start
class Solution:
    def minLength(self, s: str) -> int:

        prev = len(s) + 1
        while len(s) < prev:
            s, prev = s.replace("AB", "").replace("CD", ""), len(s)

        return prev
        
# @lc code=end

