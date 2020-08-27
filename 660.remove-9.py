#
# @lc app=leetcode id=660 lang=python3
#
# [660] Remove 9
#
# https://leetcode.com/problems/remove-9/description/
#
# algorithms
# Hard (51.70%)
# Likes:    75
# Dislikes: 116
# Total Accepted:    5.4K
# Total Submissions: 10.5K
# Testcase Example:  '10'
#
# Start from integer 1, remove any integer that contains 9 such as 9, 19,
# 29... 
# 
# So now, you will have a new integer sequence: 1, 2, 3, 4, 5, 6, 7, 8, 10, 11,
# ...
# 
# Given a positive integer n, you need to return the n-th integer after
# removing. Note that 1 will be the first integer.
# 
# Example 1:
# 
# Input: 9
# Output: 10
# 
# 
# 
# 
# ⁠Hint: n will not exceed 9 x 10^8.
# 
#
class Solution:
    def newInteger(self, n: int) -> int:

        # The answer is therefore just the n-th base-9 number.
        # Time  complexity: O(1)
        # Space complexity: O(1)
        ans = ""
        while n:
            ans = str(n % 9) + ans
            n //= 9
        return int(ans)
        

