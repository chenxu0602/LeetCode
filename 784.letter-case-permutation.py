#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#
# https://leetcode.com/problems/letter-case-permutation/description/
#
# algorithms
# Easy (64.27%)
# Likes:    1405
# Dislikes: 108
# Total Accepted:    96.6K
# Total Submissions: 148.9K
# Testcase Example:  '"a1b2"'
#
# Given a string S, we can transform every letter individually to be lowercase
# or uppercase to create another string.
# 
# Return a list of all possible strings we could create. You can return the
# output in any order.
# 
# 
# Example 1:
# 
# 
# Input: S = "a1b2"
# Output: ["a1b2","a1B2","A1b2","A1B2"]
# 
# 
# Example 2:
# 
# 
# Input: S = "3z4"
# Output: ["3z4","3Z4"]
# 
# 
# Example 3:
# 
# 
# Input: S = "12345"
# Output: ["12345"]
# 
# 
# Example 4:
# 
# 
# Input: S = "0"
# Output: ["0"]
# 
# 
# 
# Constraints:
# 
# 
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.
# 
# 
#

# @lc code=start
import itertools

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        # Recursion
        # Time  complexity: O(2^N x N)
        # Space complexity: O(2^N x N)
        # ans = [[]]

        # for char in S:
        #     n = len(ans)
        #     if char.isalpha():
        #         for i in range(n):
        #             ans.append(ans[i][:])
        #             ans[i].append(char.lower())
        #             ans[n + i].append(char.upper())
        #     else:
        #         for i in range(n):
        #             ans[i].append(char)

        # return map("".join, ans)


        # Binary Mask
        # O(2^N x N)
        # B = sum(letter.isalpha() for letter in S)
        # ans = []

        # for bits in range(1 << B):
        #     b, word = 0, []
        #     for letter in S:
        #         if letter.isalpha():
        #             if (bits >> b) & 1:
        #                 word.append(letter.lower())
        #             else:
        #                 word.append(letter.upper())

        #             b += 1
        #         else:
        #             word.append(letter)

        #     ans.append("".join(word))

        # return ans


        # Built-in Library Function
        # O(2^N x N)
        f = lambda x: (x.lower(), x.upper()) if x.isalpha() else x
        return map("".join, itertools.product(*map(f, S)))
        
# @lc code=end

