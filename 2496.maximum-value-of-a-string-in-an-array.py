#
# @lc app=leetcode id=2496 lang=python3
#
# [2496] Maximum Value of a String in an Array
#

# @lc code=start
class Solution:
    def maximumValue(self, strs: List[str]) -> int:

        return max(int(n) if n.isdigit() else len(n) for n in strs)
        
# @lc code=end

