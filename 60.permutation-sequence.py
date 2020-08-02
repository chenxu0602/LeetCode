#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#
# https://leetcode.com/problems/permutation-sequence/description/
#
# algorithms
# Medium (33.82%)
# Likes:    1012
# Dislikes: 268
# Total Accepted:    153.2K
# Total Submissions: 446.1K
# Testcase Example:  '3\n3'
#
# The set [1,2,3,...,n] contains a total of n! unique permutations.
# 
# By listing and labeling all of the permutations in order, we get the
# following sequence for n = 3:
# 
# 
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# 
# 
# Given n and k, return the k^th permutation sequence.
# 
# Note:
# 
# 
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, k = 3
# Output: "213"
# 
# 
# Example 2:
# 
# 
# Input: n = 4, k = 9
# Output: "2314"
# 
# 
#

# @lc code=start
from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # numbers = list(range(1, n+1))
        # permutation = ""

        # k -= 1
        # while n > 0:
        #     n -= 1
        #     index, k = divmod(k, factorial(n))
        #     permutation += str(numbers[index])
        #     numbers.remove(numbers[index])

        # return permutation

        factorials, nums = [1], ['1']
        for i in range(1, n):
            # generate factorial system bases 0!, 1!, ..., (n - 1)!
            factorials.append(factorials[i - 1] * i)
            # generate nums 1, 2, ..., n
            nums.append(str(i + 1))

        # fit k in the interval 0 ... (n! - 1)
        k -= 1

        # compute factorial representation of k
        output = []
        for i in range(n - 1, -1, -1):
            idx = k // factorials[i]
            k -= idx * factorials[i]

            output.append(nums[idx])
            del nums[idx]

        return "".join(output)

        
# @lc code=end

