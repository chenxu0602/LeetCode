#
# @lc app=leetcode id=2788 lang=python3
#
# [2788] Split Strings by Separator
#

# @lc code=start
class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:

        return [w for word in words for w in word.split(separator) if w]
        
# @lc code=end

