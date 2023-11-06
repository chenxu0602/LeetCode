#
# @lc app=leetcode id=2828 lang=python3
#
# [2828] Check if a String Is an Acronym of Words
#

# @lc code=start
class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:

        return ''.join(word[0] for word in words) == s
        
# @lc code=end

