#
# @lc app=leetcode id=2523 lang=python3
#
# [2523] Closest Prime Numbers in Range
#

# @lc code=start
import math

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:

        def is_prime(x):
            if x == 1: return False

            for divisor in range(2, math.floor(math.sqrt(x)) + 1):
                if x % divisor == 0:
                    return False
            
            return True


        primes = []
        for candidate in range(left, right + 1):
            if is_prime(candidate):
                if primes and candidate <= primes[-1] + 2:
                    return [primes[-1], candidate]

                primes.append(candidate)

        gaps = ([primes[i - 1], primes[i]] for i in range(1, len(primes)))

        return min(gaps, key=lambda gap: (gap[1] - gap[0], gap[0]), default=[-1, -1])
        
# @lc code=end

