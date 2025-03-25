#
# @lc app=leetcode id=3315 lang=python3
#
# [3315] Construct the Minimum Bitwise Array II
#

# @lc code=start
class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:

        res = []
        for num in nums:
            if num % 2 == 0:
                res += -1,
            else:
                res += num - ((num + 1) & (-num - 1)) // 2,

        return res

        
# @lc code=end

