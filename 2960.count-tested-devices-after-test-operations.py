#
# @lc app=leetcode id=2960 lang=python3
#
# [2960] Count Tested Devices After Test Operations
#

# @lc code=start
class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:

        ans = 0
        for x in batteryPercentages:
            if ans < x: ans += 1
        return ans
        
# @lc code=end

