#
# @lc app=leetcode id=2441 lang=python3
#
# [2441] Largest Positive Integer That Exists With Its Negative
#

# @lc code=start
class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        Set = set(nums)
        maxSoFar = float("-inf")
        res = float("-inf")

        for x in nums:
            if x > 0 and -x in Set and x > maxSoFar:
                maxSoFar = x
                res = x

        return res if res != float("-inf") else -1
        
# @lc code=end

