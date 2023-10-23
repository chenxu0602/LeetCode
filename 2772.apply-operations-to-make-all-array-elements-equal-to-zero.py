#
# @lc app=leetcode id=2772 lang=python3
#
# [2772] Apply Operations to Make All Array Elements Equal to Zero
#

# @lc code=start
class Solution:
    def checkArray(self, nums: List[int], k: int) -> bool:

        curr = 0
        for i, v in enumerate(nums):
            if curr > v: return False 

            nums[i], curr = v - curr, v 
            if i >= k - 1:
                curr -= nums[i - k + 1]

        return curr == 0 
        
# @lc code=end

