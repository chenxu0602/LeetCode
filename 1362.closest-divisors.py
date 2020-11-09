#
# @lc app=leetcode id=1362 lang=python3
#
# [1362] Closest Divisors
#
# https://leetcode.com/problems/closest-divisors/description/
#
# algorithms
# Medium (57.25%)
# Likes:    82
# Dislikes: 55
# Total Accepted:    10.6K
# Total Submissions: 18.4K
# Testcase Example:  '8'
#
# Given an integer num, find the closest two integers in absolute difference
# whose product equals num + 1 or num + 2.
# 
# Return the two integers in any order.
# 
# 
# Example 1:
# 
# 
# Input: num = 8
# Output: [3,3]
# Explanation: For num + 1 = 9, the closest divisors are 3 & 3, for num + 2 =
# 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.
# 
# 
# Example 2:
# 
# 
# Input: num = 123
# Output: [5,25]
# 
# 
# Example 3:
# 
# 
# Input: num = 999
# Output: [40,25]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        for x in range(int((num + 2)**0.5), 0, -1):
            if (num + 1) % x == 0:
                return [x, (num + 1) // x]
            if (num + 2) % x == 0:
                return [x, (num + 2) // x]

        
# @lc code=end

