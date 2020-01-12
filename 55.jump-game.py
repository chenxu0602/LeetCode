#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#
# https://leetcode.com/problems/jump-game/description/
#
# algorithms
# Medium (32.42%)
# Likes:    2486
# Dislikes: 237
# Total Accepted:    315.9K
# Total Submissions: 966K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Determine if you are able to reach the last index.
# 
# Example 1:
# 
# 
# Input: [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# 
# Example 2:
# 
# 
# Input: [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its
# maximum
# jump length is 0, which makes it impossible to reach the last index.
# 
# 
#

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:

        """
        m = 0
        for i, v in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + v)
        return True
        """

        """
        step = nums[0]
        for i in range(1, len(nums)):
            if step > 0:
                step -= 1
                step = max(step, nums[i])
            else:
                return False
        return True
        """

        lastPos = len(nums)-1
        for i in range(lastPos, -1, -1):
            if i + nums[i] >= lastPos:
                lastPos = i
        return lastPos == 0


        
# @lc code=end

