#
# @lc app=leetcode id=923 lang=python3
#
# [923] 3Sum With Multiplicity
#
# https://leetcode.com/problems/3sum-with-multiplicity/description/
#
# algorithms
# Medium (34.28%)
# Likes:    231
# Dislikes: 45
# Total Accepted:    13.3K
# Total Submissions: 38.5K
# Testcase Example:  '[1,1,2,2,3,3,4,4,5,5]\n8'
#
# Given an integer array A, and an integer target, return the number of tuples
# i, j, k  such that i < j < k and A[i] + A[j] + A[k] == target.
# 
# As the answer can be very large, return it modulo 10^9 + 7.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,1,2,2,3,3,4,4,5,5], target = 8
# Output: 20
# Explanation: 
# Enumerating by the values (A[i], A[j], A[k]):
# (1, 2, 5) occurs 8 times;
# (1, 3, 4) occurs 8 times;
# (2, 2, 4) occurs 2 times;
# (2, 3, 3) occurs 2 times.
# 
# 
# 
# Example 2:
# 
# 
# Input: A = [1,1,2,2,2,2], target = 5
# Output: 12
# Explanation: 
# A[i] = 1, A[j] = A[k] = 2 occurs 12 times:
# We choose one 1 from [1,1] in 2 ways,
# and two 2s from [2,2,2,2] in 6 ways.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 3 <= A.length <= 3000
# 0 <= A[i] <= 100
# 0 <= target <= 300
# 
#
from collections import Counter
from itertools import combinations_with_replacement

class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
       """
       MOD = 10**9+7
       ans = 0
       A.sort()

       for i, x in enumerate(A):
          T = target - A[i]
          j, k = i+1, len(A) - 1
          while j < k:
             if A[j] + A[k] < T:
                j += 1
             elif A[j] + A[k] > T:
                k -= 1
             elif A[j] != A[k]:
                left = right = 1
                while j + 1 < k and A[j] == A[j+1]:
                   left += 1
                   j += 1
                while k - 1 > j and A[k] == A[k-1]:
                   right += 1
                   k -= 1

                ans += left * right
                ans %= MOD
                j += 1
                k -= 1
             else:
                ans += (k-j+1) * (k-j) // 2
                ans %= MOD
                break

       return ans
       """

      """
       MOD = 10**9 + 7
       count = [0] * 101
       for x in A:
          count[x] += 1

       ans = 0

       for x in range(101):
          for y in range(x+1, 101):
             z = target - x - y
             if y < z <= 100:
                ans += count[x] * count[y] * count[z]
                ans %= MOD

       for x in range(101):
          z = target - 2 * x
          if x < z <= 100:
             ans += count[x] * (count[x] - 1) // 2 * count[z]
             ans %= MOD

       for x in range(101):
          if (target - x) % 2 == 0:
             y = (target - x) // 2
             if x < y <= 100:
                ans += count[x] * count[y] * (count[y] - 1) // 2
                ans %= MOD

       if target % 3 == 0:
          x = target // 3
          if 0 <= x <= 100:
             ans += count[x] * (count[x] - 1) * (count[x] - 2) // 6
             ans %= MOD

       return ans
      """

      counts = Counter(A)
      res = 0
      for i, j in combinations_with_replacement(counts, 2):
         k = target - i - j
         if i == j == k:
               res += counts[i] * (counts[i] - 1) * (counts[i] - 2) // 6
         elif i == j != k:
               res += counts[i] * (counts[i] - 1) // 2 * counts[k]
         elif k > i and k > j:
               res += counts[i] * counts[j] * counts[k]
               
      return res % (10 ** 9 + 7)
      

