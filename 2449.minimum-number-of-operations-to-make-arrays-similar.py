#
# @lc app=leetcode id=2449 lang=python3
#
# [2449] Minimum Number of Operations to Make Arrays Similar
#

# @lc code=start
class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:

        nums.sort(key=lambda x: (x & 1, x))
        target.sort(key=lambda x: (x & 1, x))
        return sum(abs(a - b) for a, b in zip(nums, target)) // 4
        
# @lc code=end

