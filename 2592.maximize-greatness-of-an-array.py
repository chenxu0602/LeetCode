#
# @lc app=leetcode id=2592 lang=python3
#
# [2592] Maximize Greatness of an Array
#

# @lc code=start
class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:

        nums.sort()
        i = 0
        for x in nums:
            if x > nums[i]:
                i += 1
        return i
        
# @lc code=end

