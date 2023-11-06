#
# @lc app=leetcode id=2894 lang=python3
#
# [2894] Divisible and Non-divisible Sums Difference
#

# @lc code=start
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:

        i = n // m
        num2 = 0
        for i in range(1, i + 1):
            num2 += m * i

        return n * (n + 1) // 2 - 2 * num2
        
# @lc code=end

