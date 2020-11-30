#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#
# https://leetcode.com/problems/three-consecutive-odds/description/
#
# algorithms
# Easy (65.80%)
# Likes:    139
# Dislikes: 21
# Total Accepted:    24.5K
# Total Submissions: 37.3K
# Testcase Example:  '[2,6,4,1]'
#
# Given an integer array arr, return true if there are three consecutive odd
# numbers in the array. Otherwise, return false.
# 
# Example 1:
# 
# 
# Input: arr = [2,6,4,1]
# Output: false
# Explanation: There are no three consecutive odds.
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,2,34,3,4,5,7,23,12]
# Output: true
# Explanation: [5,7,23] are three consecutive odds.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for num in arr:
            if num % 2:
                count += 1
            else:
                count = 0

            if count == 3:
                return True

        return False
        
# @lc code=end

