#
# @lc app=leetcode id=3330 lang=python3
#
# [3330] Find the Original Typed String I
#

# @lc code=start
from itertools import groupby

class Solution:
    def possibleStringCount(self, word: str) -> int:

        return len(word) - len(list(groupby(word))) + 1

        
# @lc code=end

