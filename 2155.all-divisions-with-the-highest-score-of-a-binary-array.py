#
# @lc app=leetcode id=2155 lang=python3
#
# [2155] All Divisions With the Highest Score of a Binary Array
#

# @lc code=start
class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:

        right = mx = sum(nums)
        left = 0
        res = [0]

        for i, el in enumerate(nums):
            if el == 0:
                left += 1
            else:
                right -= 1

            if left + right > mx:
                mx = left + right
                res = [i + 1]
            elif left + right == mx:
                res.append(i + 1)

        return res
            
        
# @lc code=end

