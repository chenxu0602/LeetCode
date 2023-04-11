#
# @lc app=leetcode id=2600 lang=python3
#
# [2600] K Items With the Maximum Sum
#

# @lc code=start
class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:

        return min(k, numOnes) - max(0, k - numZeros - numOnes)
        
# @lc code=end

