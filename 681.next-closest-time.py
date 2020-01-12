#
# @lc app=leetcode id=681 lang=python3
#
# [681] Next Closest Time
#
# https://leetcode.com/problems/next-closest-time/description/
#
# algorithms
# Medium (42.82%)
# Likes:    363
# Dislikes: 582
# Total Accepted:    48.6K
# Total Submissions: 113.2K
# Testcase Example:  '"19:34"'
#
# Given a time represented in the format "HH:MM", form the next closest time by
# reusing the current digits. There is no limit on how many times a digit can
# be reused.
# 
# You may assume the given input string is always valid. For example, "01:34",
# "12:09" are all valid. "1:34", "12:9" are all invalid.
# 
# Example 1:
# 
# Input: "19:34"
# Output: "19:39"
# Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
# which occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours
# and 59 minutes later.
# 
# 
# 
# Example 2:
# 
# Input: "23:59"
# Output: "22:22"
# Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
# It may be assumed that the returned time is next day's time since it is
# smaller than the input time numerically.
# 
# 
#
class Time(object):
    def __init__(self, time):
        self.time = time
        self.minutesFromMidNight = int(time[0:2])*60 + int(time[3:5])

class Solution:
    def nextClosestTime(self, time: str) -> str:
        self.start = Time(time)
        digits = set(time).difference(':')
        return min(self.getAllTimes(digits), key=self.getDiffFromeStart).time

    def getDiffFromeStart(self, time):
        diff = time.minutesFromMidNight - self.start.minutesFromMidNight
        if diff <= 0:
            diff += 60 * 24
        return diff

    def getAllTimes(self, digits):
        twoDigitsPerm = set(digit1 + digit2 for digit1 in digits for digit2 in digits)
        return set([Time(hour+":"+minute) for hour in twoDigitsPerm if int(hour) < 24 for minute in twoDigitsPerm if int(minute) < 60])
        

