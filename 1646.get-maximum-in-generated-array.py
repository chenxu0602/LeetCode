#
# @lc app=leetcode id=1646 lang=python3
#
# [1646] Get Maximum in Generated Array
#
# https://leetcode.com/problems/get-maximum-in-generated-array/description/
#
# algorithms
# Easy (48.17%)
# Likes:    57
# Dislikes: 51
# Total Accepted:    9.5K
# Total Submissions: 19.6K
# Testcase Example:  '7'
#
# You are given an integer n. An array nums of length n + 1 is generated in the
# following way:
# 
# 
# nums[0] = 0
# nums[1] = 1
# nums[2 * i] = nums[i] when 2 <= 2 * i <= n
# nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
# 
# 
# Return the maximum integer in the array nums​​​.
# 
# 
# Example 1:
# 
# 
# Input: n = 7
# Output: 3
# Explanation: According to the given rules:
# ⁠ nums[0] = 0
# ⁠ nums[1] = 1
# ⁠ nums[(1 * 2) = 2] = nums[1] = 1
# ⁠ nums[(1 * 2) + 1 = 3] = nums[1] + nums[2] = 1 + 1 = 2
# ⁠ nums[(2 * 2) = 4] = nums[2] = 1
# ⁠ nums[(2 * 2) + 1 = 5] = nums[2] + nums[3] = 1 + 2 = 3
# ⁠ nums[(3 * 2) = 6] = nums[3] = 2
# ⁠ nums[(3 * 2) + 1 = 7] = nums[3] + nums[4] = 2 + 1 = 3
# Hence, nums = [0,1,1,2,1,3,2,3], and the maximum is 3.
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: 1
# Explanation: According to the given rules, the maximum between nums[0],
# nums[1], and nums[2] is 1.
# 
# 
# Example 3:
# 
# 
# Input: n = 3
# Output: 2
# Explanation: According to the given rules, the maximum between nums[0],
# nums[1], nums[2], and nums[3] is 2.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 100
# 
# 
#

# @lc code=start
class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        # if n == 0: return 0

        # nums = [0] * (n + 1)
        # maxValue = 1
        # nums[1] = 1

        # for i in range(1, n // 2 + 1):
        #     nums[i * 2] = nums[i]
        #     if i * 2 + 1 <= n:
        #         nums[i * 2 + 1] = nums[i] + nums[i + 1]
        #         maxValue = max(maxValue, nums[i * 2 + 1])

        # return maxValue


        if n == 0: return 0
        nums = [0] * (n + 1)
        maxValue = 1
        nums[1] = 1

        for i in range(2, n + 1):
            if i % 2 == 0:
                nums[i] = nums[i // 2]
            else:
                nums[i] = nums[i // 2] + nums[i // 2 + 1]

            maxValue = max(maxValue, nums[i])

        return maxValue
        
# @lc code=end

