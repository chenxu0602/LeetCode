#
# @lc app=leetcode id=1191 lang=python3
#
# [1191] K-Concatenation Maximum Sum
#
# https://leetcode.com/problems/k-concatenation-maximum-sum/description/
#
# algorithms
# Medium (25.73%)
# Likes:    193
# Dislikes: 21
# Total Accepted:    8.2K
# Total Submissions: 31.7K
# Testcase Example:  '[1,2]\n3'
#
# Given an integer array arr and an integer k, modify the array by repeating it
# k times.
# 
# For example, if arr = [1, 2] and k = 3 then the modified array will be [1, 2,
# 1, 2, 1, 2].
# 
# Return the maximum sub-array sum in the modified array. Note that the length
# of the sub-array can be 0 and its sum in that case is 0.
# 
# As the answer can be very large, return the answer modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,2], k = 3
# Output: 9
# 
# 
# Example 2:
# 
# 
# Input: arr = [1,-2,1], k = 5
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: arr = [-1,-2], k = 7
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^5
# 1 <= k <= 10^5
# -10^4 <= arr[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:

        MOD = 10**9 + 7

        def Kadane(arr, res=0, cur=0):
            for num in arr:
                cur = max(cur+num, num)
                res = max(res, cur)
            return res

        # k-2 middle arrays

        return ((k-2) * max(sum(arr), 0) + Kadane(arr*2)) % MOD if k > 1 else Kadane(arr) % MOD
        
        
# @lc code=end

