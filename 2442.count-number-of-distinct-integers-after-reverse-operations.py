#
# @lc app=leetcode id=2442 lang=python3
#
# [2442] Count Number of Distinct Integers After Reverse Operations
#

# @lc code=start
class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        return len(set(int(str(x)[::-1]) for x in nums).union(set(nums)))
        
# @lc code=end

