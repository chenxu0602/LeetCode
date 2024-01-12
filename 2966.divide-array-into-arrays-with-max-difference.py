#
# @lc app=leetcode id=2966 lang=python3
#
# [2966] Divide Array Into Arrays With Max Difference
#

# @lc code=start
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:

        nums.sort()
        ans = []
        for i in range(0, len(nums), 3):
            if nums[i + 2] - nums[i] > k:
                return []
            ans += [nums[i], nums[i + 1], nums[i + 2]],

        return ans
        
# @lc code=end

