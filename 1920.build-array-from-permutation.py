#
# @lc app=leetcode id=1920 lang=python3
#
# [1920] Build Array from Permutation
#

# @lc code=start
import quopri


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:

        q = len(nums)
        for i in range(q):
            r = nums[i]
            b = nums[nums[i]] % q
            nums[i] = q * b + r

        for i in range(q):
            nums[i] = nums[i] // q

        return nums
        
# @lc code=end

