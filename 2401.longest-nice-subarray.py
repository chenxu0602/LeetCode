#
# @lc app=leetcode id=2401 lang=python3
#
# [2401] Longest Nice Subarray
#

# @lc code=start
class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res = AND = i = 0
        for j in range(len(nums)):
            while AND & nums[j]:
                AND ^= nums[i]
                i += 1

            AND |= nums[j]
            res = max(res, j - i + 1)
        return res
        
# @lc code=end

