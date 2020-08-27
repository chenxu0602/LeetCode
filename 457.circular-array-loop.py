#
# @lc app=leetcode id=457 lang=python3
#
# [457] Circular Array Loop
#
# https://leetcode.com/problems/circular-array-loop/description/
#
# algorithms
# Medium (29.26%)
# Likes:    381
# Dislikes: 1326
# Total Accepted:    35.1K
# Total Submissions: 119.4K
# Testcase Example:  '[2,-1,1,2,2]'
#
# You are given a circular array nums of positive and negative integers. If a
# number k at an index is positive, then move forward k steps. Conversely, if
# it's negative (-k), move backward k steps. Since the array is circular, you
# may assume that the last element's next element is the first element, and the
# first element's previous element is the last element.
# 
# Determine if there is a loop (or a cycle) in nums. A cycle must start and end
# at the same index and the cycle's length > 1. Furthermore, movements in a
# cycle must all follow a single direction. In other words, a cycle must not
# consist of both forward and backward movements.
# 
# 
# 
# Example 1:
# 
# 
# Input: [2,-1,1,2,2]
# Output: true
# Explanation: There is a cycle, from index 0 -> 2 -> 3 -> 0. The cycle's
# length is 3.
# 
# 
# Example 2:
# 
# 
# Input: [-1,2]
# Output: false
# Explanation: The movement from index 1 -> 1 -> 1 ... is not a cycle, because
# the cycle's length is 1. By definition the cycle's length must be greater
# than 1.
# 
# 
# Example 3:
# 
# 
# Input: [-2,1,-1,-2,-2]
# Output: false
# Explanation: The movement from index 1 -> 2 -> 1 -> ... is not a cycle,
# because movement from index 1 -> 2 is a forward movement, but movement from
# index 2 -> 1 is a backward movement. All movements in a cycle must follow a
# single direction.
# 
# 
# 
# Note:
# 
# 
# -1000 ≤ nums[i] ≤ 1000
# nums[i] ≠ 0
# 1 ≤ nums.length ≤ 5000
# 
# 
# 
# 
# Follow up:
# 
# Could you solve it in O(n) time complexity and O(1) extra space complexity?
#

# @lc code=start
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:

        s, l = [], len(nums)
        for i, n in enumerate(nums):
            if i in s:
                continue

            d = []
            while n * nums[i] > 0:
                if i in d:
                    if d[-1] != i:
                        return True
                    break

                d.append(i)
                s.append(i)
                i = (i + nums[i]) % l

        return False
        
# @lc code=end

