#
# @lc app=leetcode id=906 lang=python3
#
# [906] Super Palindromes
#
# https://leetcode.com/problems/super-palindromes/description/
#
# algorithms
# Hard (30.67%)
# Likes:    53
# Dislikes: 137
# Total Accepted:    3.9K
# Total Submissions: 12.6K
# Testcase Example:  '"4"\n"1000"'
#
# Let's say a positive integer is a superpalindrome if it is a palindrome, and
# it is also the square of a palindrome.
# 
# Now, given two positive integers L and R (represented as strings), return the
# number of superpalindromes in the inclusive range [L, R].
# 
# 
# 
# Example 1:
# 
# 
# Input: L = "4", R = "1000"
# Output: 4
# Explanation: 4, 9, 121, and 484 are superpalindromes.
# Note that 676 is not a superpalindrome: 26 * 26 = 676, but 26 is not a
# palindrome.
# 
# 
# 
# Note:
# 
# 
# 1 <= len(L) <= 18
# 1 <= len(R) <= 18
# L and R are strings representing integers in the range [1, 10^18).
# int(L) <= int(R)
# 
# 
# 
# 
# 
# 
#
from math import floor, ceil, sqrt

class Solution:
    def superpalindromesInRange(self, L: str, R: str) -> int:
      #  L, R = int(L), int(R)
      #  left = int(floor(sqrt(L)))
      #  right = int(ceil(sqrt(R)))

      #  n1, n2 = len(str(left)), len(str(right))

      #  n1 = n1 // 2 if n1 % 2 == 0 else n1 // 2 + 1
      #  n2 = n2 // 2 if n2 % 2 == 0 else n2 // 2 + 1

      #  start = int('1' + '0' * (n1 - 1))
      #  end = int('9' * n2) + 1

      #  ans = 0
      #  for i in range(start, end):
      #     x = str(i)
      #     num1 = int(x + x[::-1])
      #     num2 = int(x + x[:-1][::-1])
      #     for num in [num1, num2]:
      #        cand = num * num
      #        if cand >= L and cand <= R and str(cand) == str(cand)[::-1]:
      #           ans += 1
      #  return ans


      # Mathematical
      # Time  complexity: O(W^(1/4) x logW), where W=10^18 is our upper limit for R.
      # The logW term comes from checking whether each candidate is the root of a palindrome.
      # Space complexity: O(logW)
      L, R = map(int, (L, R))
      MAGIC = 100000

      def reverse(x):
          ans = 0
          while x:
              ans = 10 * ans + x % 10
              x //= 10
          return ans

      def is_palindrome(x):
          return x == reverse(x)

      ans = 0
      # count odd length
      for k in range(MAGIC):
          s = str(k)
          t = s + s[-2::-1]
          v = int(t) ** 2
          if v > R: break
          if v >= L and is_palindrome(v):
              ans += 1

      # count even length
      for k in range(MAGIC):
          s = str(k)
          t = s + s[::-1]
          v = int(t) ** 2
          if v > R: break
          if v >= L and is_palindrome(v):
              ans += 1

      return ans
        

