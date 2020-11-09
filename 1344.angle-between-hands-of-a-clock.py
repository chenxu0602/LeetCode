#
# @lc app=leetcode id=1344 lang=python3
#
# [1344] Angle Between Hands of a Clock
#
# https://leetcode.com/problems/angle-between-hands-of-a-clock/description/
#
# algorithms
# Medium (61.26%)
# Likes:    415
# Dislikes: 97
# Total Accepted:    46K
# Total Submissions: 75K
# Testcase Example:  '12\n30'
#
# Given two numbers, hour and minutes. Return the smaller angle (in degrees)
# formed between the hour and the minute hand.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: hour = 12, minutes = 30
# Output: 165
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: hour = 3, minutes = 30
# Output: 75
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: hour = 3, minutes = 15
# Output: 7.5
# 
# 
# Example 4:
# 
# 
# Input: hour = 4, minutes = 50
# Output: 155
# 
# 
# Example 5:
# 
# 
# Input: hour = 12, minutes = 0
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= hour <= 12
# 0 <= minutes <= 59
# Answers within 10^-5 of the actual value will be accepted as correct.
# 
# 
#

# @lc code=start
class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:

        one_min_angle = 6
        one_hour_angle = 30

        minutes_angle = one_min_angle * minutes
        hour_angle = (hour % 12 + minutes / 60) * one_hour_angle

        diff = abs(hour_angle - minutes_angle)
        return min(diff, 360 - diff)

        
        
# @lc code=end

