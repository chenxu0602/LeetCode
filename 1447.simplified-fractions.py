#
# @lc app=leetcode id=1447 lang=python3
#
# [1447] Simplified Fractions
#
# https://leetcode.com/problems/simplified-fractions/description/
#
# algorithms
# Medium (61.52%)
# Likes:    111
# Dislikes: 23
# Total Accepted:    12.8K
# Total Submissions: 20.9K
# Testcase Example:  '2\r'
#
# Given an integer n, return a list of all simplified fractions between 0 and 1
# (exclusive) such that the denominator is less-than-or-equal-to n. The
# fractions can be in any order.
# 
# 
# Example 1:
# 
# 
# Input: n = 2
# Output: ["1/2"]
# Explanation: "1/2" is the only unique fraction with a denominator
# less-than-or-equal-to 2.
# 
# Example 2:
# 
# 
# Input: n = 3
# Output: ["1/2","1/3","2/3"]
# 
# 
# Example 3:
# 
# 
# Input: n = 4
# Output: ["1/2","1/3","1/4","2/3","3/4"]
# Explanation: "2/4" is not a simplified fraction because it can be simplified
# to "1/2".
# 
# Example 4:
# 
# 
# Input: n = 1
# Output: []
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 100
# 
#

# @lc code=start
class Solution:
    def simplifiedFractions(self, n: int) -> List[str]:
        # Each GCD computation cost O(log(max(x,y))), and there are O(n ^ 2) iterations for the nested loop.
        # def gcd(x: int, y: int) -> int:
        #     return y if x == 0 else gcd(y % x, x)

        def gcd(x: int, y: int) -> int:
            while x > 0:
                x, y = y % x, x
            return y

        return [str(i) + '/' + str(j) for j in range(2, n + 1) for i in range(1, j) if gcd(i, j) == 1]

        
# @lc code=end

