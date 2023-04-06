#
# @lc app=leetcode id=2553 lang=python3
#
# [2553] Separate the Digits in an Array
#

# @lc code=start
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        return [int(c) for a in nums for c in str(a)]
        
# @lc code=end

