#
# @lc app=leetcode id=2709 lang=python3
#
# [2709] Greatest Common Divisor Traversal
#

# @lc code=start
import math

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:


        if len(nums) == 1: return True
        if 1 in nums: return False

        if len(set(nums)) == 1 and nums[0] > 1: return True

        nums = sorted(nums, reverse=True)
        if (n := len(nums)) == 1: return True

        for i in range(n - 1):
            for j in range(i + 1, n):
                if math.gcd(nums[i], nums[j]) - 1:
                    nums[j] *= nums[i] 
                    break
            else:
                return False

        return True


        
# @lc code=end

