#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (52.41%)
# Likes:    3461
# Dislikes: 427
# Total Accepted:    259.6K
# Total Submissions: 494.7K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
# 
# Example 1:
# 
# 
# Input: [1,3,4,2,2]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: [3,1,3,4,2]
# Output: 3
# 
# Note:
# 
# 
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
# 
# 
#

# @lc code=start
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's Tortoise and Hare (Cycle Detection)
        # The cycle appears because nums contains duplicates. The duplicate node is a cycle entrance.
        # Time  complexity: O(n)
        # Space complexity: O(1)
        slow = fast = nums[0]
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break

        fast = nums[0]
        while slow != fast:
            slow, fast = nums[slow], nums[fast]

        return fast
        
# @lc code=end

