#
# @lc app=leetcode id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#
# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
#
# algorithms
# Medium (29.87%)
# Likes:    266
# Dislikes: 4
# Total Accepted:    7.4K
# Total Submissions: 24.6K
# Testcase Example:  '[1,1,4,2,3]\n5'
#
# You are given an integer array nums and an integer x. In one operation, you
# can either remove the leftmost or the rightmost element from the array nums
# and subtract its value from x. Note that this modifies the array for future
# operations.
# 
# Return the minimum number of operations to reduce x to exactly 0 if it's
# possible, otherwise, return -1.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to
# reduce x to zero.
# 
# 
# Example 2:
# 
# 
# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and
# the first two elements (5 operations in total) to reduce x to zero.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 1 <= x <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # LC325


        total = sum(nums)
        n = len(nums)
        maxi = -1
        left = current = 0

        for right in range(n):
            current += nums[right]
            while current > total - x and left <= right:
                current -= nums[left]
                left += 1

            if current == total - x:
                maxi = max(maxi, right - left + 1)

        return n - maxi if maxi != -1 else -1


        # current = sum(nums)
        # n = len(nums)
        # mini = float("inf")
        # left = 0

        # for right in range(n):
        #     current -= nums[right]
        #     while current < x and left <= right:
        #         current += nums[left]
        #         left += 1

        #     if current == x:
        #         mini = min(mini, (n - 1 - right) + left)

        # return mini if mini != float("inf") else -1
        
        
# @lc code=end

