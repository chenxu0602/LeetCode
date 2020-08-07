#
# @lc app=leetcode id=247 lang=python3
#
# [247] Strobogrammatic Number II
#
# https://leetcode.com/problems/strobogrammatic-number-ii/description/
#
# algorithms
# Medium (45.03%)
# Likes:    291
# Dislikes: 90
# Total Accepted:    57.6K
# Total Submissions: 125.9K
# Testcase Example:  '2'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# 
# Find all strobogrammatic numbers that are of length = n.
# 
# Example:
# 
# 
# Input:  n = 2
# Output: ["11","69","88","96"]
# 
# 
#

# @lc code=start
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        res = [""]
        if n % 2:
            res = list("018")

        while n > 1:
            n -= 2
            res = [a + num + b for a, b in "00 11 88 69 96".split()[n<2:] for num in res]

        return res



        
# @lc code=end

