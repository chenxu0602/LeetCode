#
# @lc app=leetcode id=1218 lang=python3
#
# [1218] Longest Arithmetic Subsequence of Given Difference
#
# https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/description/
#
# algorithms
# Medium (41.87%)
# Likes:    191
# Dislikes: 19
# Total Accepted:    10.8K
# Total Submissions: 25.7K
# Testcase Example:  '[1,2,3,4]\n1'
#
# Given an integer array arr and an integer difference, return the length of
# the longest subsequence in arr which is an arithmetic sequence such that the
# difference between adjacent elements in the subsequence equals difference.
# 
# 
# Example 1:
# 
# 
# Input: arr = [1,2,3,4], difference = 1
# Output: 4
# Explanation: The longest arithmetic subsequence is [1,2,3,4].
# 
# Example 2:
# 
# 
# Input: arr = [1,3,5,7], difference = 1
# Output: 1
# Explanation: The longest arithmetic subsequence is any single element.
# 
# 
# Example 3:
# 
# 
# Input: arr = [1,5,7,8,5,3,4,2,1], difference = -2
# Output: 4
# Explanation: The longest arithmetic subsequence is [7,5,3,1].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 10^5
# -10^4 <= arr[i], difference <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:

        res = {}
        for num in arr:
            res[num] = res.get(num - difference, 0) + 1
        return max(res.values())
        
# @lc code=end

