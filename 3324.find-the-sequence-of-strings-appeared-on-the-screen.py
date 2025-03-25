#
# @lc app=leetcode id=3324 lang=python3
#
# [3324] Find the Sequence of Strings Appeared on the Screen
#

# @lc code=start
from string import ascii_lowercase

class Solution:
    def stringSequence(self, target: str) -> List[str]:

        return [target[:i] + a for i, c in enumerate(target) for a in ascii_lowercase if a <= c]
        
# @lc code=end

