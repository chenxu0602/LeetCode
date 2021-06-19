#
# @lc app=leetcode id=1854 lang=python3
#
# [1854] Maximum Population Year
#
# https://leetcode.com/problems/maximum-population-year/description/
#
# algorithms
# Easy (57.03%)
# Likes:    227
# Dislikes: 36
# Total Accepted:    14.5K
# Total Submissions: 25.4K
# Testcase Example:  '[[1993,1999],[2000,2010]]'
#
# You are given a 2D integer array logs where each logs[i] = [birthi, deathi]
# indicates the birth and death years of the i^th person.
# 
# The population of some year x is the number of people alive during that year.
# The i^th person is counted in year x's population if x is in the inclusive
# range [birthi, deathi - 1]. Note that the person is not counted in the year
# that they die.
# 
# Return the earliest year with the maximum population.
# 
# 
# Example 1:
# 
# 
# Input: logs = [[1993,1999],[2000,2010]]
# Output: 1993
# Explanation: The maximum population is 1, and 1993 is the earliest year with
# this population.
# 
# 
# Example 2:
# 
# 
# Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
# Output: 1960
# Explanation: 
# The maximum population is 2, and it had happened in years 1960 and 1970.
# The earlier year between them is 1960.
# 
# 
# Constraints:
# 
# 
# 1 <= logs.length <= 100
# 1950 <= birthi < deathi <= 2050
# 
# 
#

# @lc code=start
import itertools

class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:

        years = [0] * 101
        for b, d in logs:
            years[b - 1950] += 1
            years[d - 1950] -= 1

        years = list(itertools.accumulate(years))
        max_pop = max(years)

        for i in range(len(years)):
            if years[i] == max_pop:
                return i + 1950

        
        

        
# @lc code=end

