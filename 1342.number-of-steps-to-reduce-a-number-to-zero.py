#
# @lc app=leetcode id=1342 lang=python3
#
# [1342] Number of Steps to Reduce a Number to Zero
#
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/description/
#
# algorithms
# Easy (85.93%)
# Likes:    568
# Dislikes: 61
# Total Accepted:    128.6K
# Total Submissions: 149.7K
# Testcase Example:  '14'
#
# Given a non-negative integer num, return the number of steps to reduce it to
# zero. If the current number is even, you have to divide it by 2, otherwise,
# you have to subtract 1 from it.
# 
# 
# Example 1:
# 
# 
# Input: num = 14
# Output: 6
# Explanation: 
# Step 1) 14 is even; divide by 2 and obtain 7. 
# Step 2) 7 is odd; subtract 1 and obtain 6.
# Step 3) 6 is even; divide by 2 and obtain 3. 
# Step 4) 3 is odd; subtract 1 and obtain 2. 
# Step 5) 2 is even; divide by 2 and obtain 1. 
# Step 6) 1 is odd; subtract 1 and obtain 0.
# 
# 
# Example 2:
# 
# 
# Input: num = 8
# Output: 4
# Explanation: 
# Step 1) 8 is even; divide by 2 and obtain 4. 
# Step 2) 4 is even; divide by 2 and obtain 2. 
# Step 3) 2 is even; divide by 2 and obtain 1. 
# Step 4) 1 is odd; subtract 1 and obtain 0.
# 
# 
# Example 3:
# 
# 
# Input: num = 123
# Output: 12
# 
# 
# 
# Constraints:
# 
# 
# 0 <= num <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def numberOfSteps (self, num: int) -> int:
        # O(logn)

        # steps = 0
        # while num > 0:
        #     if num % 2 == 0:
        #         num //= 2
        #     else:
        #         num -= 1
        #     steps += 1
        # return steps


        # steps = 0
        # binary = bin(num)[2:]
        # for bit in binary:
        #     if bit == '1':
        #         steps += 2
        #     else:
        #         steps += 1
        # return steps - 1


        binary = bin(num)[2:]
        ones = binary.count('1')
        return ones + len(binary) - 1

        
# @lc code=end

