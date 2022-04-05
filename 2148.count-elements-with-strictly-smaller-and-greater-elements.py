#
# @lc app=leetcode id=2148 lang=python3
#
# [2148] Count Elements With Strictly Smaller and Greater Elements 
#

# @lc code=start
class Solution:
    def countElements(self, nums: List[int]) -> int:
        M, m = max(nums), min(nums)
        return sum(1 for i in nums if m < i < M)
        
# @lc code=end

