#
# @lc app=leetcode id=1655 lang=python3
#
# [1655] Distribute Repeating Integers
#
# https://leetcode.com/problems/distribute-repeating-integers/description/
#
# algorithms
# Hard (41.22%)
# Likes:    75
# Dislikes: 9
# Total Accepted:    3K
# Total Submissions: 7.3K
# Testcase Example:  '[1,2,3,4]\n[2]'
#
# You are given an array of n integers, nums, where there are at most 50 unique
# values in the array. You are also given an array of m customer order
# quantities, quantity, where quantity[i] is the amount of integers the i^th
# customer ordered. Determine if it is possible to distribute nums such
# that:
# 
# 
# The i^th customer gets exactly quantity[i] integers,
# The integers the i^th customer gets are all equal, and
# Every customer is satisfied.
# 
# 
# Return true if it is possible to distribute nums according to the above
# conditions.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,4], quantity = [2]
# Output: false
# Explanation: The 0th customer cannot be given two different integers.
# 
# 
# Example 2:
# 
# 
# Input: nums = [1,2,3,3], quantity = [2]
# Output: true
# Explanation: The 0th customer is given [3,3]. The integers [1,2] are not
# used.
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,1,2,2], quantity = [2,2]
# Output: true
# Explanation: The 0th customer is given [1,1], and the 1st customer is given
# [2,2].
# 
# 
# Example 4:
# 
# 
# Input: nums = [1,1,2,3], quantity = [2,2]
# Output: false
# Explanation: Although the 0th customer could be given [1,1], the 1st customer
# cannot be satisfied.
# 
# Example 5:
# 
# 
# Input: nums = [1,1,1,1,1], quantity = [2,3]
# Output: true
# Explanation: The 0th customer is given [1,1], and the 1st customer is given
# [1,1,1].
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 1 <= n <= 10^5
# 1 <= nums[i] <= 1000
# m == quantity.length
# 1 <= m <= 10
# 1 <= quantity[i] <= 10^5
# There are at most 50 unique values in nums.
# 
# 
#

# @lc code=start
from collections import Counter, defaultdict

class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:

        c = Counter(nums)
        m = len(quantity)

        left = sorted(c.values())[-m:]
        quantity.sort(reverse=True)

        def helper(left, quantity, customer):
            if customer == len(quantity):
                return True

            for i in range(len(left)):
                if left[i] >= quantity[customer]:
                    left[i] -= quantity[customer]
                    if helper(left, quantity, customer + 1):
                        return True
                    left[i] += quantity[customer]

            return False

        return helper(left, quantity, 0)

        
# @lc code=end

