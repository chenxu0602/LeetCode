#
# @lc app=leetcode id=1246 lang=python3
#
# [1246] Palindrome Removal
#
# https://leetcode.com/problems/palindrome-removal/description/
#
# algorithms
# Hard (44.60%)
# Likes:    85
# Dislikes: 1
# Total Accepted:    2.1K
# Total Submissions: 4.7K
# Testcase Example:  '[1,2]'
#
# Given an integer array arr, in one move you can select a palindromic subarray
# arr[i], arr[i+1], ..., arr[j] where i <= j, and remove that subarray from the
# given array. Note that after removing a subarray, the elements on the left
# and on the right of that subarray move to fill the gap left by the removal.
# 
# Return the minimum number of moves needed to remove all numbers from the
# array.
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,2]
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,3,4,1,5]
# Output: 3
# Explanation: Remove [4] then remove [1,3,1] then remove [5].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 100
# 1 <= arr[i] <= 20
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def minimumMoves(self, arr: List[int]) -> int:
        # @lru_cache(None)
        # def dp(i, j):
        #     if i > j:
        #         return 0

        #     res = dp(i, j - 1) + 1
        #     if arr[j] == arr[j - 1]:
        #         res = min(res, dp(i, j - 2) + 1)

        #     for k in range(i, j - 1):
        #         if arr[j] == arr[k]:
        #             res = min(res, dp(i, k - 1) + dp(k + 1, j - 1) if k < j - 1 else 1)

        #     return res

        # return dp(0, len(arr) - 1)

        @lru_cache(None)
        def dp(i, j):
            if i > j: return 0
            return min(dp(i, k - 1) + (dp(k + 1, j - 1)if k < j - 1 else 1)\
                for k in range(i, j + 1) if arr[k] == arr[j])

        return dp(0, len(arr) - 1)

        
# @lc code=end

