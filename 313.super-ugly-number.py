#
# @lc app=leetcode id=313 lang=python3
#
# [313] Super Ugly Number
#
# https://leetcode.com/problems/super-ugly-number/description/
#
# algorithms
# Medium (41.45%)
# Likes:    358
# Dislikes: 93
# Total Accepted:    60.9K
# Total Submissions: 146.4K
# Testcase Example:  '12\n[2,7,13,19]'
#
# Write a program to find the n^th super ugly number.
# 
# Super ugly numbers are positive numbers whose all prime factors are in the
# given prime list primes of size k.
# 
# Example:
# 
# 
# Input: n = 12, primes = [2,7,13,19]
# Output: 32 
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first
# 12 
# ⁠            super ugly numbers given primes = [2,7,13,19] of size 4.
# 
# Note:
# 
# 
# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 10^6, 0 < primes[i] < 1000.
# The n^th super ugly number is guaranteed to fit in a 32-bit signed integer.
# 
# 
#
import heapq, itertools

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        # uglies = [1]
        # def gen(prime):
        #     for ugly in uglies:
        #         yield ugly * prime

        # merged = heapq.merge(*map(gen, primes))
        # while len(uglies) < n:
        #     ugly = next(merged)
        #     if ugly != uglies[-1]:
        #         uglies.append(ugly)

        # return uglies[-1]


        uglies = [1]
        merged = heapq.merge(*map(lambda p: (u * p for u in uglies), primes))
        uniqed = (u for u, _ in itertools.groupby(merged))
        list(map(uglies.append, itertools.islice(uniqed, n - 1)))
        return uglies[-1]

        
        

