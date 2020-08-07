#
# @lc app=leetcode id=229 lang=python3
#
# [229] Majority Element II
#
# https://leetcode.com/problems/majority-element-ii/description/
#
# algorithms
# Medium (32.79%)
# Likes:    1069
# Dislikes: 125
# Total Accepted:    115.6K
# Total Submissions: 346.3K
# Testcase Example:  '[3,2,3]'
#
# Given an integer array of size n, find all elements that appear more than ⌊
# n/3 ⌋ times.
# 
# Note: The algorithm should run in linear time and in O(1) space.
# 
# Example 1:
# 
# 
# Input: [3,2,3]
# Output: [3]
# 
# Example 2:
# 
# 
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
# 
#

# @lc code=start
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        ctr = Counter()
        for i in nums:
            ctr[i] += 1
            if len(ctr) == 3:
                ctr -= Counter(set(ctr))

        return [n for n in ctr if nums.count(n) > len(nums) // 3]


        
# @lc code=end

