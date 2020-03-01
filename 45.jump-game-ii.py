#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (28.58%)
# Likes:    1517
# Dislikes: 87
# Total Accepted:    198.1K
# Total Submissions: 683.6K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
# 
# Each element in the array represents your maximum jump length at that
# position.
# 
# Your goal is to reach the last index in the minimum number of jumps.
# 
# Example:
# 
# 
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
# 
# Note:
# 
# You can assume that you can always reach the last index.
# 
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:

        res, last, curr = 0, 0, 0

        for i in range(len(nums)):
            if i > last:
                last = curr
                res += 1
            curr = max(curr, i + nums[i])

        return res

        
# @lc code=end

