#
# @lc app=leetcode id=1185 lang=python3
#
# [1185] Day of the Week
#
# https://leetcode.com/problems/day-of-the-week/description/
#
# algorithms
# Easy (64.09%)
# Likes:    131
# Dislikes: 1173
# Total Accepted:    25.8K
# Total Submissions: 40.9K
# Testcase Example:  '31\n8\n2019'
#
# Given a date, return the corresponding day of the week for that date.
# 
# The input is given as three integers representing the day, month and year
# respectively.
# 
# Return the answer as one of the following values {"Sunday", "Monday",
# "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"}.
# 
# 
# Example 1:
# 
# 
# Input: day = 31, month = 8, year = 2019
# Output: "Saturday"
# 
# 
# Example 2:
# 
# 
# Input: day = 18, month = 7, year = 1999
# Output: "Sunday"
# 
# 
# Example 3:
# 
# 
# Input: day = 15, month = 8, year = 1993
# Output: "Sunday"
# 
# 
# 
# Constraints:
# 
# 
# The given dates are valid dates between the years 1971 and 2100.
# 
# 
#

# @lc code=start
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # Zelle formula
        # O(1)
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        if month < 3:
            month += 12
            year -= 1
            
        c, year = divmod(year, 100)
        w = (c // 4 - 2 * c + year + year // 4 + 13 * (month+1) // 5 + day - 1) % 7
        return days[w]
        
# @lc code=end

