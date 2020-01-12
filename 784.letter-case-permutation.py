#
# @lc app=leetcode id=784 lang=python3
#
# [784] Letter Case Permutation
#
# https://leetcode.com/problems/letter-case-permutation/description/
#
# algorithms
# Easy (58.31%)
# Likes:    730
# Dislikes: 88
# Total Accepted:    54.8K
# Total Submissions: 93.6K
# Testcase Example:  '"a1b2"'
#
# Given a string S, we can transform every letter individually to be lowercase
# or uppercase to create another string.  Return a list of all possible strings
# we could create.
# 
# 
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
# 
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
# 
# Input: S = "12345"
# Output: ["12345"]
# 
# 
# Note:
# 
# 
# S will be a string with length between 1 and 12.
# S will consist only of letters or digits.
# 
# 
#
import itertools

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:

        """
        digits = {str(x) for x in range(10)}
        A = ['']
        for c in S:
            B = []
            if c in digits:
                for a in A:
                    B.append(a+c)
            else:
                for a in A:
                    B.append(a+c.lower())
                    B.append(a+c.upper())
            A = B
        return A
        """

        """
        B = sum(letter.isalpha() for letter in S)
        ans = []

        for bits in range(1 << B):
            b = 0
            word = []
            for letter in S:
                if letter.isalpha():
                    if (bits >> b) & 1:
                        word.append(letter.lower())
                    else:
                        word.append(letter.upper())
                    b+= 1
                else:
                    word.append(letter)
                
            ans.append("".join(word))
        return ans
        """

        f = lambda x: (x.lower, x.upper()) if x.isalpha() else x
        return map("".join, itertools.product(*map(f, S)))


        

