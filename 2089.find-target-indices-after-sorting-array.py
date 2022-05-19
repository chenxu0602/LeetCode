#
# @lc app=leetcode id=2089 lang=python3
#
# [2089] Find Target Indices After Sorting Array
#

# @lc code=start
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        lb, up = 0, 0
        for num in nums:
            if num < target:
                lb += 1
            elif num == target:
                up += 1

        return list(range(lb, lb + up))
        
# @lc code=end

