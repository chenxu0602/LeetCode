#
# @lc app=leetcode id=1287 lang=python3
#
# [1287] Element Appearing More Than 25% In Sorted Array
#
# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/description/
#
# algorithms
# Easy (60.27%)
# Likes:    116
# Dislikes: 7
# Total Accepted:    9.7K
# Total Submissions: 16.2K
# Testcase Example:  '[1,2,2,6,6,6,6,7,10]'
#
# Given an integer array sorted in non-decreasing order, there is exactly one
# integer in the array that occurs more than 25% of the time.
# 
# Return that integer.
# 
# 
# Example 1:
# Input: arr = [1,2,2,6,6,6,6,7,10]
# Output: 6
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^4
# 0 <= arr[i] <= 10^5
# 
#

# @lc code=start
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
#        return max(set(arr), key=arr.count)

        n = len(arr) // 4
        for i in range(len(arr)):
            if arr[i] == arr[i+n]:
                return arr[i]
        
# @lc code=end

