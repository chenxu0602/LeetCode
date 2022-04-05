#
# @lc app=leetcode id=2149 lang=python3
#
# [2149] Rearrange Array Elements by Sign
#

# @lc code=start
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:

        a = [0] * len(nums)
        p, n = 0, 1
        for i in nums:
            if i > 0:
                a[p] = i
                p += 2
            else:
                a[n] = i
                n += 2
        return a
        
# @lc code=end

