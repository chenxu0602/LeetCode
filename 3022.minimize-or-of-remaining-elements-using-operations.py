#
# @lc app=leetcode id=3022 lang=python3
#
# [3022] Minimize OR of Remaining Elements Using Operations
#

# @lc code=start
class Solution:
    def minOrAfterOperations(self, nums: List[int], k: int) -> int:

        ans = 0
        for bit in range(30, -1, -1):
            cnt = 0
            cur = (1 << 30) - 1
            target = ans | ((1 << bit) - 1)
            for num in nums:
                cur &= num
                if cur | target == target:
                    cnt += 1
                    cur = (1 << 30) - 1

            if len(nums) - cnt > k:
                ans |= (1 << bit)

        return ans
        
# @lc code=end

