#
# @lc app=leetcode id=2185 lang=python3
#
# [2185] Counting Words With a Given Prefix
#

# @lc code=start
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(word.find(pref) == 0 for  word in words)
        
# @lc code=end

