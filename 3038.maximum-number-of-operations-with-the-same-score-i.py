#
# @lc app=leetcode id=3038 lang=python3
#
# [3038] Maximum Number of Operations With the Same Score I
#

# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int]) -> int:

        a = nums[0] + nums[1]
        cnt = 1

        for i in range(2, len(nums) - 1, 2):
            if nums[i] + nums[i + 1] == a:
                cnt += 1
            else:
                break

        return cnt
        
# @lc code=end

