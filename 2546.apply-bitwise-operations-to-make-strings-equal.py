#
# @lc app=leetcode id=2546 lang=python3
#
# [2546] Apply Bitwise Operations to Make Strings Equal
#

# @lc code=start
class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:

        return ('1' in s) == ('1' in target)
        
# @lc code=end

