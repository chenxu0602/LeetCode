#
# @lc app=leetcode id=1187 lang=python3
#
# [1187] Make Array Strictly Increasing
#
# https://leetcode.com/problems/make-array-strictly-increasing/description/
#
# algorithms
# Hard (40.62%)
# Likes:    208
# Dislikes: 7
# Total Accepted:    3.9K
# Total Submissions: 9.7K
# Testcase Example:  '[1,5,3,6,7]\n[1,3,2,4]'
#
# Given two integer arrays arr1 and arr2, return the minimum number of
# operations (possibly zero) needed to make arr1 strictly increasing.
# 
# In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j
# < arr2.length and do the assignment arr1[i] = arr2[j].
# 
# If there is no way to make arr1 strictly increasing, return -1.
# 
# 
# Example 1:
# 
# 
# Input: arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]
# Output: 1
# Explanation: Replace 5 with 2, then arr1 = [1, 2, 3, 6, 7].
# 
# 
# Example 2:
# 
# 
# Input: arr1 = [1,5,3,6,7], arr2 = [4,3,1]
# Output: 2
# Explanation: Replace 5 with 3 and then replace 3 with 4. arr1 = [1, 3, 4, 6,
# 7].
# 
# 
# Example 3:
# 
# 
# Input: arr1 = [1,5,3,6,7], arr2 = [1,6,3,3]
# Output: -1
# Explanation: You can't make arr1 strictly increasing.
# 
# 
# Constraints:
# 
# 
# 1 <= arr1.length, arr2.length <= 2000
# 0 <= arr1[i], arr2[i] <= 10^9
# 
# 
# 
#

# @lc code=start

from collections import defaultdict
import bisect

class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:

        dp = {-1: 0}
        arr2.sort()
        for i in arr1:
            tmp = defaultdict(lambda: float("inf"))
            for key in dp:
                if i > key:
                    tmp[i] = min(tmp[i], dp[key])
                loc = bisect.bisect_right(arr2, key)
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp[arr2[loc]], dp[key] + 1)
            dp = tmp

        if dp:
            return min(dp.values())

        return -1

        
# @lc code=end

