#
# @lc app=leetcode id=2191 lang=python3
#
# [2191] Sort the Jumbled Numbers
#

# @lc code=start
class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:

        def convert(num: int) -> int:
            if num == 0: return mapping[0]

            n, f = 0, 1
            while num > 0:
                num, r = divmod(num, 10)
                n += mapping[r] * f
                f *= 10
            return n

        indices = sorted(range(len(nums)), key=lambda i: convert(nums[i]))
        return [nums[i] for i in indices]
        
# @lc code=end

