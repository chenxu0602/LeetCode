#
# @lc app=leetcode id=2798 lang=python3
#
# [2798] Number of Employees Who Met the Target
#

# @lc code=start
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:

        return sum(h >= target for h in hours)
        
# @lc code=end

