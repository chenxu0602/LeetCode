#
# @lc app=leetcode id=2239 lang=python3
#
# [2239] Find Closest Number to Zero
#

# @lc code=start
class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        return max([-abs(x), x] for x in nums)[1]
        
# @lc code=end

