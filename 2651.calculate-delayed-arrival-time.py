#
# @lc app=leetcode id=2651 lang=python3
#
# [2651] Calculate Delayed Arrival Time
#

# @lc code=start
class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:

        return (arrivalTime + delayedTime) % 24
        
# @lc code=end

