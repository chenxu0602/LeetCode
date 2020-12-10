#
# @lc app=leetcode id=1663 lang=python3
#
# [1663] Smallest String With A Given Numeric Value
#
# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/description/
#
# algorithms
# Medium (59.88%)
# Likes:    127
# Dislikes: 3
# Total Accepted:    8.8K
# Total Submissions: 14.7K
# Testcase Example:  '3\n27'
#
# The numeric value of a lowercase character is defined as its position
# (1-indexed) in the alphabet, so the numeric value of a is 1, the numeric
# value of b is 2, the numeric value of c is 3, and so on.
# 
# The numeric value of a string consisting of lowercase characters is defined
# as the sum of its characters' numeric values. For example, the numeric value
# of the string "abe" is equal to 1 + 2 + 5 = 8.
# 
# You are given two integers n and k. Return the lexicographically smallest
# string with length equal to n and numeric value equal to k.
# 
# Note that a string x is lexicographically smaller than string y if x comes
# before y in dictionary order, that is, either x is a prefix of y, or if i is
# the first position such that x[i] != y[i], then x[i] comes before y[i] in
# alphabetic order.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, k = 27
# Output: "aay"
# Explanation: The numeric value of the string is 1 + 1 + 25 = 27, and it is
# the smallest string with such a value and length equal to 3.
# 
# 
# Example 2:
# 
# 
# Input: n = 5, k = 73
# Output: "aaszz"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^5
# n <= k <= 26 * n
# 
# 
#

# @lc code=start
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # O(n)

        # result = [""] * n
        # for pos in range(n):
        #     posLeft = n - pos - 1
        #     if k > posLeft * 26:
        #         add = k - posLeft * 26
        #         result[pos] = chr(ord('a') + add - 1)
        #         k -= add
        #     else:
        #         result[pos] = 'a'
        #         k -= 1

        # return "".join(result)


        # result = ['a'] * n
        # k -= n
        # for pos in range(n - 1, -1, -1):
        #     add = min(k, 25)
        #     result[pos] = chr(ord(result[pos]) + add)
        #     k -= add

        # return "".join(result)


        result = [0] * n
        for pos in range(n - 1, -1, -1):
            add = min(k - pos, 26)
            result[pos] = add 
            k -= add

        return "".join(map(lambda c: chr(ord('a') + c - 1), result))
        
# @lc code=end

