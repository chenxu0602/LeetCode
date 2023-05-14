#
# @lc app=leetcode id=2678 lang=python3
#
# [2678] Number of Senior Citizens
#

# @lc code=start
class Solution:
    def countSeniors(self, details: List[str]) -> int:

        return sum(int(p[-4:-2]) > 60 for p in details)
        
# @lc code=end

