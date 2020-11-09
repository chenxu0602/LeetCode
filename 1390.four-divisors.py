#
# @lc app=leetcode id=1390 lang=python3
#
# [1390] Four Divisors
#
# https://leetcode.com/problems/four-divisors/description/
#
# algorithms
# Medium (38.76%)
# Likes:    85
# Dislikes: 98
# Total Accepted:    12.9K
# Total Submissions: 33.4K
# Testcase Example:  '[21,4,7]'
#
# Given an integer array nums, return the sum of divisors of the integers in
# that array that have exactly four divisors.
# 
# If there is no such integer in the array, return 0.
# 
# 
# Example 1:
# 
# 
# Input: nums = [21,4,7]
# Output: 32
# Explanation:
# 21 has 4 divisors: 1, 3, 7, 21
# 4 has 3 divisors: 1, 2, 4
# 7 has 2 divisors: 1, 7
# The answer is the sum of divisors of 21 only.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^4
# 1 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
from math import sqrt, floor

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def four_div_sum(num):
            divs = set()

            for i in range(1, floor(sqrt(num)) + 1):
                if num % i == 0:
                    divs.update({i, num // i})
                if len(divs) > 4:
                    return 0

            return sum(divs) if len(divs) == 4 else 0

        return sum(four_div_sum(num) for num in nums)

        
# @lc code=end

