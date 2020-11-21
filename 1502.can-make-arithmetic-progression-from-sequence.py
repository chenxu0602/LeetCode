#
# @lc app=leetcode id=1502 lang=python3
#
# [1502] Can Make Arithmetic Progression From Sequence
#
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/description/
#
# algorithms
# Easy (71.25%)
# Likes:    220
# Dislikes: 17
# Total Accepted:    32.6K
# Total Submissions: 45.8K
# Testcase Example:  '[3,5,1]'
#
# Given an array of numbers arr. A sequence of numbers is called an arithmetic
# progression if the difference between any two consecutive elements is the
# same.
# 
# Return true if the array can be rearranged to form an arithmetic progression,
# otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: arr = [3,5,1]
# Output: true
# Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with
# differences 2 and -2 respectively, between each consecutive elements.
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,2,4]
# Output: false
# Explanation: There is no way to reorder the elements to obtain an arithmetic
# progression.
# 
# 
# 
# Constraints:
# 
# 
# 2 <= arr.length <= 1000
# -10^6 <= arr[i] <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        m = min(arr)
        gap = (max(arr) - m) / (len(arr) - 1)
        if gap == 0: return True
        s = set(num - m for num in arr)
        return len(s) == len(arr) and all(diff % gap == 0 for diff in s)

        
# @lc code=end

