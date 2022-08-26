#
# @lc app=leetcode id=2358 lang=python3
#
# [2358] Maximum Number of Groups Entering a Competition
#

# @lc code=start
class Solution:
    def maximumGroups(self, grades: List[int]) -> int:
        n = len(grades)
        k = 0
        while n >= k + 1:
            k += 1
            n -= k
        return k
        
# @lc code=end

