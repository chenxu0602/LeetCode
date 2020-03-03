#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (27.42%)
# Likes:    1503
# Dislikes: 182
# Total Accepted:    160.4K
# Total Submissions: 583.5K
# Testcase Example:  '[10,2]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
# 
# Example 1:
# 
# 
# Input: [10,2]
# Output: "210"
# 
# Example 2:
# 
# 
# Input: [3,30,34,5,9]
# Output: "9534330"
# 
# 
# Note: The result may be very large, so you need to return a string instead of
# an integer.
# 
#

# @lc code=start
class LargerNumber(str):
    def __lt__(self, other):
        return self + other > other + self

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = "".join(sorted(map(str, nums), key=LargerNumber))
        return '0' if largest_num[0] == '0' else largest_num
        
# @lc code=end

