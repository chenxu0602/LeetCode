#
# @lc app=leetcode id=2980 lang=python3
#
# [2980] Check if Bitwise OR Has Trailing Zeros
#

# @lc code=start
class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:

        even = 0

        for num in nums:
            if num % 2 == 0:
                even += 1

        return even >= 2
        
# @lc code=end

