#
# @lc app=leetcode id=246 lang=python3
#
# [246] Strobogrammatic Number
#
# https://leetcode.com/problems/strobogrammatic-number/description/
#
# algorithms
# Easy (42.80%)
# Likes:    151
# Dislikes: 367
# Total Accepted:    61.6K
# Total Submissions: 142.2K
# Testcase Example:  '"69"'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# 
# Write a function to determine if a number is strobogrammatic. The number is
# represented as a string.
# 
# Example 1:
# 
# 
# Input:  "69"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:  "88"
# Output: true
# 
# Example 3:
# 
# 
# Input:  "962"
# Output: false
# 
#

# @lc code=start
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        d = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6'
        }

        l, r = 0, len(num)-1
        while l <= r:
            if not num[l] in d or d[num[l]] != num[r]:
                return False

            l += 1; r -= 1
        return True

        
# @lc code=end

