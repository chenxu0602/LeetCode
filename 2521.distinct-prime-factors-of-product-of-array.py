#
# @lc app=leetcode id=2521 lang=python3
#
# [2521] Distinct Prime Factors of Product of Array
#

# @lc code=start
class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:

        seen, primes = set(), {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}

        for num in nums:
            for p in primes:

                r = num % p
                if p not in seen and not r:
                    seen.add(p)

                while not r:
                    num //= p
                    r = num % p

            if num > 1:
                seen.add(num)

        return len(seen)
        
# @lc code=end

