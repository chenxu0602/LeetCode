#
# @lc app=leetcode id=2224 lang=python3
#
# [2224] Minimum Number of Operations to Convert Time
#

# @lc code=start
class Solution:
    def convertTime(self, current: str, correct: str) -> int:

        current_time = 60 * int(current[:2]) + int(current[3:5])
        target_time = 60 * int(correct[:2]) + int(correct[3:5])
        diff = target_time - current_time

        count = 0
        for i in [60, 15, 5, 1]:
            count += diff // i
            diff %= i

        return count
        
# @lc code=end

