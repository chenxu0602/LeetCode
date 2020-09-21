#
# @lc app=leetcode id=932 lang=python3
#
# [932] Beautiful Array
#
# https://leetcode.com/problems/beautiful-array/description/
#
# algorithms
# Medium (58.13%)
# Likes:    371
# Dislikes: 484
# Total Accepted:    12.2K
# Total Submissions: 20.8K
# Testcase Example:  '4'
#
# For some fixed N, an array A is beautiful if it is a permutation of the
# integers 1, 2, ..., N, such that:
# 
# For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] +
# A[j].
# 
# Given N, return any beautiful array A.  (It is guaranteed that one
# exists.)
# 
# 
# 
# Example 1:
# 
# 
# Input: 4
# Output: [2,1,4,3]
# 
# 
# 
# Example 2:
# 
# 
# Input: 5
# Output: [3,1,2,5,4]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 1000
# 
# 
# 
# 
# 
#

# @lc code=start
from functools import lru_cache

class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        # Looking at the elements 1, 2, ..., N, there are (N+1) / 2 odd numbers and N / 2 even numbers.    
        # Time  complexity: O(NlogN). The function f is called only O(logN) times, and each time does O(N) work.
        # Space complexity: O(NlogN)
      #   @lru_cache(None)    
      #   def f(N):
      #       if N == 1:
      #           return [1]    
      #       odds = f((N + 1) // 2)
      #       evens = f(N // 2)

      #       return [2*x-1 for x in odds] + [2*x for x in evens]

      #   return f(N)


        res = [1] 
        while len(res) < N:
            res = [i*2 - 1 for i in res] + [i*2 for i in res]
        return [i for i in res if i <= N]
                
            
        
# @lc code=end

