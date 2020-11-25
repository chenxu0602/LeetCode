#
# @lc app=leetcode id=1512 lang=python3
#
# [1512] Number of Good Pairs
#
# https://leetcode.com/problems/number-of-good-pairs/description/
#
# algorithms
# Easy (89.09%)
# Likes:    224
# Dislikes: 12
# Total Accepted:    28.9K
# Total Submissions: 32.5K
# Testcase Example:  '[1,2,3,1,1,3]'
#
# Given an array of integers nums.
# 
# A pair (i,j) is called good if nums[i] == nums[j] and i < j.
# 
# Return the number of good pairs.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,1,1,3]
# Output: 4
# Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,1,1,1]
# Output: 6
# Explanation: Each pair in the array are good.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,3]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # return sum(k * (k - 1) // 2 for k in Counter(nums).values())


        repeat, num = {}, 0

        for v in nums:
            if v in repeat:
                num += repeat[v]
                repeat[v] += 1
            else:
                repeat[v] = 1

        return num



        
# @lc code=end

