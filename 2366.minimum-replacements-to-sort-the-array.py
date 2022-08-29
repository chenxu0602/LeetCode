#
# @lc app=leetcode id=2366 lang=python3
#
# [2366] Minimum Replacements to Sort the Array
#

# @lc code=start
import math

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:

        n = len(nums)
        ret = 0
        prev = nums[n - 1]

        for i in range(n - 2, -1, -1):
            num = nums[i]
            k = math.ceil(num / prev)
            ret += k - 1
            prev = num // k

        return ret

        """
        x = nums[-1]
        res = 0
        for num in reversed(nums):
            k = (num + x - 1) // x
            x = num // k
            res += k - 1
        return res
        """
        
# @lc code=end

