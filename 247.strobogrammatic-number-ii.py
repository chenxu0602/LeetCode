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
        """
        even = ["11", "69", "88", "96", "00"]
        odd = ["0", "1", "8"]

        if n == 1:
            return odd
        if n == 2:
            return even[:-1]
        if n % 2:
            pre, mid = self.findStrobogrammatic(n-1), odd
        else:
            pre, mid = self.findStrobogrammatic(n-2), even

        premid = (n-1) // 2
        return [p[:premid] + c + p[premid:] for c in mid for p in pre]
        """

        res = [""]

        if n % 2 == 1:
            res = list("018")

        while n > 1:
            n -= 2
            res = [a + num + b for a, b in "00 11 88 69 96".split()[n<2:] for num in res]
        return res
        
# @lc code=end

