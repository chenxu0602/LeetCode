#
# @lc app=leetcode id=2507 lang=python3
#
# [2507] Smallest Value After Replacing With Sum of Prime Factors
#

# @lc code=start
class Solution:
    def smallestValue(self, n: int) -> int:

        def primes(n, s=0):
            for i in range(2, n + 1):
                while n % i == 0:
                    s += i
                    n //= i
            return s

        while n != (n := primes(n)): pass

        return n
        
# @lc code=end

