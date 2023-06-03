#
# @lc app=leetcode id=2710 lang=python3
#
# [2710] Remove Trailing Zeros From a String
#

# @lc code=start
class Solution:
    def removeTrailingZeros(self, num: str) -> str:

        return num.rstrip('0')
        
# @lc code=end

