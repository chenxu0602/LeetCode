#
# @lc app=leetcode id=3295 lang=python3
#
# [3295] Report Spam Message
#

# @lc code=start
class Solution:
    def reportSpam(self, message: List[str], bannedWords: List[str]) -> bool:

        s = set(bannedWords)
        return sum(m in s for m in message) > 1
        
# @lc code=end

