#
# @lc app=leetcode id=2141 lang=python3
#
# [2141] Maximum Running Time of N Computers
#

# @lc code=start
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:


        batteries.sort()
        total = sum(batteries)

        while batteries[-1] > total / n:
            n -= 1
            total -= batteries.pop()

        return total // n
        
# @lc code=end

