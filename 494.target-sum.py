#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
# https://leetcode.com/problems/target-sum/description/
#
# algorithms
# Medium (46.24%)
# Likes:    1932
# Dislikes: 89
# Total Accepted:    131.5K
# Total Submissions: 284.3K
# Testcase Example:  '[1,1,1,1,1]\n3'
#
# 
# You are given a list of non-negative integers, a1, a2, ..., an, and a target,
# S. Now you have 2 symbols + and -. For each integer, you should choose one
# from + and - as its new symbol.
# ⁠
# 
# Find out how many ways to assign symbols to make sum of integers equal to
# target S.  
# 
# 
# Example 1:
# 
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# 
# 
# 
# Note:
# 
# The length of the given array is positive and will not exceed 20. 
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:

        def dfs(cur, i, d={}):
            if i < len(nums) and (i, cur) not in d:
                d[i, cur] = dfs(cur + nums[i], i + 1) + dfs(cur - nums[i], i + 1)
            return d.get((i, cur), int(cur == S))

        return dfs(0, 0)


        # if len(nums) == 0: return 0

        # prev = defaultdict(int)
        # prev[nums[0]] += 1
        # prev[-nums[0]] += 1

        # for i in range(1, len(nums)):
        #     temp = defaultdict(int)
        #     for k, v in prev.items():
        #         temp[k-nums[i]] += v
        #         temp[k+nums[i]] += v
        #     prev = temp

        # return prev[S]
        
# @lc code=end

