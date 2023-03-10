#
# @lc app=leetcode id=2454 lang=python3
#
# [2454] Next Greater Element IV
#

# @lc code=start
class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:

        res, s1, s2 = [-1] * len(nums), [], []
        for i, v in enumerate(nums):
            while s2 and nums[s2[-1]] < v:
                res[s2.pop()] = v

            tmp = []
            while s1 and nums[s1[-1]] < v:
                tmp.append(s1.pop())

            s2 += tmp[::-1]
            s1.append(i)

        return res
        
# @lc code=end

