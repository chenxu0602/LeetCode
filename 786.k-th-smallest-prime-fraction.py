#
# @lc app=leetcode id=786 lang=python3
#
# [786] K-th Smallest Prime Fraction
#
# https://leetcode.com/problems/k-th-smallest-prime-fraction/description/
#
# algorithms
# Hard (41.15%)
# Likes:    392
# Dislikes: 25
# Total Accepted:    14.2K
# Total Submissions: 34.5K
# Testcase Example:  '[1,2,3,5]\n3'
#
# A sorted list A contains 1, plus some number of primes.  Then, for every p <
# q in the list, we consider the fraction p/q.
# 
# What is the K-th smallest fraction considered?  Return your answer as an
# array of ints, where answer[0] = p and answer[1] = q.
# 
# 
# Examples:
# Input: A = [1, 2, 3, 5], K = 3
# Output: [2, 5]
# Explanation:
# The fractions to be considered in sorted order are:
# 1/5, 1/3, 2/5, 1/2, 3/5, 2/3.
# The third fraction is 2/5.
# 
# Input: A = [1, 7], K = 1
# Output: [1, 7]
# 
# 
# Note:
# 
# 
# A will have length between 2 and 2000.
# Each A[i] will be between 1 and 30000.
# K will be between 1 and A.length * (A.length - 1) / 2.
# 
#

# @lc code=start
import heapq
from fractions import Fraction

class Solution:
    def kthSmallestPrimeFraction(self, A: List[int], K: int) -> List[int]:
        # Heap
        # Time  complexity: O(K x logN)
        # Space complexity: O(N)
        # pq = [(A[0] / float(A[i]), 0, i) for i in range(len(A) - 1, 0, -1)]

        # for _ in range(K - 1):
        #     frac, i, j = heapq.heappop(pq)
        #     i += 1
        #     if i < j:
        #         heapq.heappush(pq, (A[i] / float(A[j]), i, j))

        # return A[pq[0][1]], A[pq[0][2]]


        # Binary Search
        # Time  complexity: O(N x logW)
        # Space complexity: O(1)
        def under(x):
            # Return the number of fractions below x, and the largest such fraction
            count, best, i = 0, 0, -1
            for j in range(1, len(A)):
                while A[i + 1] < A[j] * x:
                    i += 1
                count += i + 1
                if i >= 0:
                    best = max(best, Fraction(A[i], A[j]))
            return count, best

        # Binary search for x such that there are K fractions below x.
        lo, hi = 0.0, 1.0
        while hi - lo > 1e-9:
            mi = (lo + hi) / 2.0
            count, best = under(mi)
            if count < K:
                lo = mi
            else:
                ans = best
                hi = mi

        return ans.numerator, ans.denominator

        
# @lc code=end

