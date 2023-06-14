#
# @lc app=leetcode id=2717 lang=python3
#
# [2717] Semi-Ordered Permutation
#

# @lc code=start
class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:

        n = len(nums)
        i, j = nums.index(1), nums.index(n)
        return i + n - 1 - j - (i > j)
        
# @lc code=end

