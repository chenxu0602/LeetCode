#
# @lc app=leetcode id=2367 lang=python3
#
# [2367] Number of Arithmetic Triplets
#

# @lc code=start
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:

        seen = set(nums)
        return sum(num - diff in seen and num - diff * 2 in seen for num in seen)
        
# @lc code=end

