#
# @lc app=leetcode id=2778 lang=python3
#
# [2778] Sum of Squares of Special Elements 
#

# @lc code=start
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:

        n = len(nums)
        return sum(num**2 for i, num in enumerate(nums, 1) if n % i == 0)
        
# @lc code=end

