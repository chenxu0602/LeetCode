#
# @lc app=leetcode id=2971 lang=python3
#
# [2971] Find Polygon With the Largest Perimeter
#

# @lc code=start
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:

        nums.sort()
        previous_elements_sum = 0
        ans = -1

        for num in nums:
            if num < previous_elements_sum:
                ans = num + previous_elements_sum
            previous_elements_sum += num
        
        return ans
        
# @lc code=end

