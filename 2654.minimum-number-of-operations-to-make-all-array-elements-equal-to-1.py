#
# @lc app=leetcode id=2654 lang=python3
#
# [2654] Minimum Number of Operations to Make All Array Elements Equal to 1
#

# @lc code=start
import math

class Solution:
    def minOperations(self, nums: List[int]) -> int:

        cnt, n = 0, len(nums)
        for i in nums:
            if i == 1:
                cnt += 1

        n = len(nums)
        if 1 in nums:
            return n - cnt

        for steps in range(n):
            for i in range(n - steps - 1):
                nums[i] = math.gcd(nums[i], nums[i + 1])
                if nums[i] == 1:
                    return steps + n

        return -1

        
# @lc code=end

