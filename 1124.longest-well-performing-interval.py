#
# @lc app=leetcode id=1124 lang=python3
#
# [1124] Longest Well-Performing Interval
#
# https://leetcode.com/problems/longest-well-performing-interval/description/
#
# algorithms
# Medium (30.75%)
# Likes:    215
# Dislikes: 43
# Total Accepted:    6.5K
# Total Submissions: 20.5K
# Testcase Example:  '[9,9,6,0,6,6,9]'
#
# We are given hours, a list of the number of hours worked per day for a given
# employee.
# 
# A day is considered to be a tiring day if and only if the number of hours
# worked is (strictly) greater than 8.
# 
# A well-performing interval is an interval of days for which the number of
# tiring days is strictly larger than the number of non-tiring days.
# 
# Return the length of the longest well-performing interval.
# 
# 
# Example 1:
# 
# 
# Input: hours = [9,9,6,0,6,6,9]
# Output: 3
# Explanation: The longest well-performing interval is [9,9,6].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= hours.length <= 10000
# 0 <= hours[i] <= 16
# 
# 
#

# @lc code=start
class Solution:
    def longestWPI(self, hours: List[int]) -> int:

        """
        Sum, ans = 0, 0
        cache = {}
        for i, n in enumerate(hours):
            Sum = Sum + 1 if n > 8 else Sum - 1
            if Sum > 0:
                ans = i + 1
            if Sum - 1 in cache:
                ans = max(ans, i - cache[Sum-1])
            cache.setdefault(Sum, i)
        return ans
        """

        res = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        return res
        
# @lc code=end

