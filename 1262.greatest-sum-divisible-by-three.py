#
# @lc app=leetcode id=1262 lang=python3
#
# [1262] Greatest Sum Divisible by Three
#
# https://leetcode.com/problems/greatest-sum-divisible-by-three/description/
#
# algorithms
# Medium (42.63%)
# Likes:    244
# Dislikes: 6
# Total Accepted:    7.9K
# Total Submissions: 18.5K
# Testcase Example:  '[3,6,5,1,8]'
#
# Given an array nums of integers, we need to find the maximum possible sum of
# elements of the array such that it is divisible by three.
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [3,6,5,1,8]
# Output: 18
# Explanation: Pick numbers 3, 6, 1 and 8 their sum is 18 (maximum sum
# divisible by 3).
# 
# Example 2:
# 
# 
# Input: nums = [4]
# Output: 0
# Explanation: Since 4 is not divisible by 3, do not pick any number.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3,4,4]
# Output: 12
# Explanation: Pick numbers 1, 3, 4 and 4 their sum is 12 (maximum sum
# divisible by 3).
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 4 * 10^4
# 1 <= nums[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        seen = [0, 0, 0]
        for a in nums:
            for i in seen[:]:
                seen[(i + a) % 3] = max(seen[(i + a) % 3], i + a)
        return seen[0]

        
# @lc code=end

