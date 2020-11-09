#
# @lc app=leetcode id=1363 lang=python3
#
# [1363] Largest Multiple of Three
#
# https://leetcode.com/problems/largest-multiple-of-three/description/
#
# algorithms
# Hard (33.73%)
# Likes:    193
# Dislikes: 35
# Total Accepted:    8.6K
# Total Submissions: 25.4K
# Testcase Example:  '[8,1,9]'
#
# Given an integer array of digits, return the largest multiple of three that
# can be formed by concatenating some of the given digits in any order.
# 
# Since the answer may not fit in an integer data type, return the answer as a
# string.
# 
# If there is no answer return an empty string.
# 
# 
# Example 1:
# 
# 
# Input: digits = [8,1,9]
# Output: "981"
# 
# 
# Example 2:
# 
# 
# Input: digits = [8,6,7,1,0]
# Output: "8760"
# 
# 
# Example 3:
# 
# 
# Input: digits = [1]
# Output: ""
# 
# 
# Example 4:
# 
# 
# Input: digits = [0,0,0,0,0,0]
# Output: "0"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= digits.length <= 10^4
# 0 <= digits[i] <= 9
# The returning answer must not contain unnecessary leading zeros.
# 
# 
#

# @lc code=start
class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        d1 = sorted([i for i in digits if i % 3 == 1])
        d2 = sorted([i for i in digits if i % 3 == 2])
        d3 = [i for i in digits if i % 3 == 0]

        if sum(digits) % 3 == 1:
            if len(d1) != 0:
                res = d1[1:] + d2 + d3
            else:
                res = d2[2:] + d3
        elif sum(digits) % 3 == 2:
            if len(d2) != 0:
                res = d1 + d2[1:] + d3
            else:
                res = d1[2:] + d3
        else:
            res = digits

        res.sort(reverse=True)
        return str(int("".join(map(str, res)))) if res else ""
        
# @lc code=end

