hate
# @lc app=leetcode id=1736 lang=python3
#
# [1736] Latest Time by Replacing Hidden Digits
#
# https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/description/
#
# algorithms
# Easy (41.53%)
# Likes:    69
# Dislikes: 38
# Total Accepted:    10.3K
# Total Submissions: 24.7K
# Testcase Example:  '"2?:?0"'
#
# You are given a string time in the form of  hh:mm, where some of the digits
# in the string are hidden (represented by ?).
# 
# The valid times are those inclusively between 00:00 and 23:59.
# 
# Return the latest valid time you can get from time by replacing the hidden
# digits.
# 
# 
# Example 1:
# 
# 
# Input: time = "2?:?0"
# Output: "23:50"
# Explanation: The latest hour beginning with the digit '2' is 23 and the
# latest minute ending with the digit '0' is 50.
# 
# 
# Example 2:
# 
# 
# Input: time = "0?:3?"
# Output: "09:39"
# 
# 
# Example 3:
# 
# 
# Input: time = "1?:22"
# Output: "19:22"
# 
# 
# 
# Constraints:
# 
# 
# time is in the format hh:mm.
# It is guaranteed that you can produce a valid time from the given string.
# 
# 
#

# @lc code=start
class Solution:
    def maximumTime(self, time: str) -> str:
        hr, mm = time.split(':')
        if hr == "??":
            hr = "23"
        elif hr[0] == '?':
            hr_tmp = '2' + hr[1]
            if int(hr_tmp) >= 24:
                hr = '1' + hr[1]
            else:
                hr = '2' + hr[1]
        elif hr[1] == '?':
            if hr[0] < '2':
                hr = hr[0] + '9'
            else:
                hr = hr[0] + '3'

        if mm == "??":
            mm = "59"
        elif mm[0] == '?':
            mm = '5' + mm[1]
        elif mm[1] == '?':
            mm = mm[0] + '9'

        return ':'.join([hr, mm])
        
# @lc code=end

