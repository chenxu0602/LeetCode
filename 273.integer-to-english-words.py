#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#
# https://leetcode.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (24.38%)
# Likes:    534
# Dislikes: 1473
# Total Accepted:    104K
# Total Submissions: 426.8K
# Testcase Example:  '123'
#
# Convert a non-negative integer to its english words representation. Given
# input is guaranteed to be less than 2^31 - 1.
# 
# Example 1:
# 
# 
# Input: 123
# Output: "One Hundred Twenty Three"
# 
# 
# Example 2:
# 
# 
# Input: 12345
# Output: "Twelve Thousand Three Hundred Forty Five"
# 
# Example 3:
# 
# 
# Input: 1234567
# Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty
# Seven"
# 
# 
# Example 4:
# 
# 
# Input: 1234567891
# Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
# Thousand Eight Hundred Ninety One"
# 
# 
#
class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve " \
               "Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()

        tens = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()

        def words(n):
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                return [tens[n//10-2]] + words(n%10)
            if n < 1000:
                return [to19[n//100-1]] + ["Hundred"] + words(n%100)

            for p, w in enumerate(("Thousand", "Million", "Billion"), 1):
                if n < 1000**(p+1):
                    return words(n//1000**p) + [w] + words(n%1000**p)


        return " ".join(words(num)) or "Zero"
        

