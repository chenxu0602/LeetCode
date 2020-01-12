#
# @lc app=leetcode id=930 lang=python3
#
# [930] Binary Subarrays With Sum
#
# https://leetcode.com/problems/binary-subarrays-with-sum/description/
#
# algorithms
# Medium (39.16%)
# Likes:    269
# Dislikes: 12
# Total Accepted:    12.4K
# Total Submissions: 31.3K
# Testcase Example:  '[1,0,1,0,1]\n2'
#
# In an array A of 0s and 1s, how many non-empty subarrays have sum S?
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1,0,1,0,1], S = 2
# Output: 4
# Explanation: 
# The 4 subarrays are bolded below:
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# [1,0,1,0,1]
# 
# 
# 
# 
# Note:
# 
# 
# A.length <= 30000
# 0 <= S <= A.length
# A[i] is either 0 or 1.
# 
#
from collections import Counter

class Solution:
    def numSubarraysWithSum(self, A: List[int], S: int) -> int:
       """
       indexes = [-1] + [ix for ix, v in enumerate(A) if v] + [len(A)]
       ans = 0

       if S == 0:
          for i in range(len(indexes) - 1):
             w = indexes[i+1] - indexes[i] - 1
             ans += w * (w + 1) // 2
          return ans

       for i in range(1, len(indexes) - S):
          j = i + S - 1
          left = indexes[i] - indexes[i-1]
          right = indexes[j+1] - indexes[j]
          ans += left * right

       return ans
       """

       """
       P = [0]
       for x in A:
          P.append(P[-1] + x)

       count = Counter()

       ans = 0
       for x in P:
          ans += count[x]
          count[x + S] += 1

       return ans
       """

       i_lo = i_hi = 0
       sum_lo = sum_hi = 0
       ans = 0

       for j, x in enumerate(A):
          sum_lo += x
          while i_lo < j and sum_lo > S:
             sum_lo -= A[i_lo]
             i_lo += 1

          sum_hi += x
          while i_hi < j and (sum_hi > S or sum_hi == S and not A[i_hi]):
             sum_hi -= A[i_hi]
             i_hi += 1

          if sum_lo == S:
             ans += i_hi - i_lo + 1

       return ans
        

