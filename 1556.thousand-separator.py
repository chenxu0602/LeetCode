#
# @lc app=leetcode id=1556 lang=python3
#
# [1556] Thousand Separator
#
# https://leetcode.com/problems/thousand-separator/description/
#
# algorithms
# Easy (58.63%)
# Likes:    133
# Dislikes: 7
# Total Accepted:    16.5K
# Total Submissions: 28.2K
# Testcase Example:  '987'
#
# Given an integer n, add a dot (".") as the thousands separator and return it
# in string format.
# 
# 
# Example 1:
# 
# 
# Input: n = 987
# Output: "987"
# 
# 
# Example 2:
# 
# 
# Input: n = 1234
# Output: "1.234"
# 
# 
# Example 3:
# 
# 
# Input: n = 123456789
# Output: "123.456.789"
# 
# 
# Example 4:
# 
# 
# Input: n = 0
# Output: "0"
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n < 2^31
# 
# 
#

# @lc code=start
class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = []
        while n:
            n, r = divmod(n, 1000)
            res.append(r)

        if not res:
            return str(n)

        first = res.pop()
        res = list(map("{:03d}".format, res))
        res = [str(first)] + res[::-1]
        return ".".join(res)
        
# @lc code=end

