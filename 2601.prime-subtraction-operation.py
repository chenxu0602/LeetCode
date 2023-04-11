#
# @lc app=leetcode id=2601 lang=python3
#
# [2601] Prime Subtraction Operation
#

# @lc code=start

import bisect

def sieve(num):
    prime = [True] * (num + 1)
    prime[0] = prime[1] = False

    for i in range(2, int(num ** 0.5) + 1):
        if prime[i]:
            for j in range(i * i, num + 1, i):
                prime[j] = False

    return [i for i in range(len(prime)) if prime[i]]

primes = sieve(1000)

class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # curr - x > prev
        # x < curr - prev
        # x < = curr - prev - 1
        # then find the closest x in the primes (upto 1000) using binary search
        # then subtract it from the curr num
        # if not possible to find the closest then remain the curr number as it is

        n = len(nums)
        prev = 0
        for i in range(n):
            req = nums[i] - prev - 1
            idx = bisect.bisect_left(primes, req)
            takeCurr = False
            if idx >= len(primes) or primes[idx] > req:
                if idx > 0 and primes[idx - 1] <= req:
                    idx = idx - 1
                else:
                    takeCurr = True

            curr = nums[i]
            if not takeCurr:
                curr = nums[i] - primes[idx]

            if curr <= prev:
                return False

            prev = curr

        return True
        
# @lc code=end

