#
# @lc app=leetcode id=2216 lang=python3
#
# [2216] Minimum Deletions to Make Array Beautiful
#

# @lc code=start
class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1] and (i - res) % 2 == 0:
                res += 1

        return res + (len(nums) - res) % 2
        
# @lc code=end

