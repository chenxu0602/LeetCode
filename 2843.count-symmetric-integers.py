#
# @lc app=leetcode id=2843 lang=python3
#
# [2843]   Count Symmetric Integers
#

# @lc code=start
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:

        ans = len([n for n in range(11, 100, 11) if low <= n <= high])

        for i in range(max(1001, low), min(high + 1, 10000)):
            a, b, c, d = map(int, str(i))

            ans += a + b == c + d

        return ans
        
# @lc code=end

