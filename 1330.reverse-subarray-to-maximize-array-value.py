#
# @lc app=leetcode id=1330 lang=python3
#
# [1330] Reverse Subarray To Maximize Array Value
#
# https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/description/
#
# algorithms
# Hard (35.74%)
# Likes:    183
# Dislikes: 25
# Total Accepted:    2.5K
# Total Submissions: 7K
# Testcase Example:  '[2,3,1,5,4]'
#
# You are given an integer array nums. The value of this array is defined as
# the sum of |nums[i]-nums[i+1]| for all 0 <= i < nums.length-1.
# 
# You are allowed to select any subarray of the given array and reverse it. You
# can perform this operation only once.
# 
# Find maximum possible value of the final array.
# 
# 
# Example 1:
# 
# 
# Input: nums = [2,3,1,5,4]
# Output: 10
# Explanation: By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4]
# whose value is 10.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,4,9,24,2,1,10]
# Output: 68
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 3*10^4
# -10^5 <= nums[i] <= 10^5
# 
#

# @lc code=start
class Solution:
    def maxValueAfterReverse(self, nums: List[int]) -> int:
        # maxi, mini = float("-inf"), float("inf")

        # for a, b in zip(nums, nums[1:]):
        #     maxi = max(min(a, b), maxi)
        #     mini = min(max(a, b), mini)
        # change = max(0, (maxi - mini) * 2)

        # for a, b in zip(nums, nums[1:]):
        #     tmp1 = -abs(a - b) + abs(nums[0] - b)
        #     tmp2 = -abs(a - b) + abs(nums[-1] - a)
        #     change = max([tmp1, tmp2, change])

        # original_value = sum(abs(a - b) for a, b in zip(nums, nums[1:]))
        # return original_value + change


        total, res, min2, max2 = 0, 0, float("inf"), float("-inf")
        for a, b in zip(nums, nums[1:]):
            total += abs(a - b)
            res = max(res, abs(nums[0] - b) - abs(a - b))
            res = max(res, abs(nums[-1] - a) - abs(a - b))
            min2, max2 = min(min2, max(a, b)), max(max2, min(a, b))
        return total + max(res, (max2 - min2) * 2)
        
# @lc code=end

