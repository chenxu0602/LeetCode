#
# @lc app=leetcode id=3264 lang=python3
#
# [3264] Final Array State After K Multiplication Operations I
#

# @lc code=start
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        n = len(nums)
        for _ in range(k):
            idx, ans = 0, nums[0]
            for i in range(1, n):
                if nums[i] < ans:
                    ans = nums[i]
                    idx = i
            nums[idx] *= multiplier

        return nums
        
# @lc code=end

