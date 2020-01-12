#
# @lc app=leetcode id=564 lang=python3
#
# [564] Find the Closest Palindrome
#
# https://leetcode.com/problems/find-the-closest-palindrome/description/
#
# algorithms
# Hard (18.96%)
# Likes:    158
# Dislikes: 616
# Total Accepted:    14.7K
# Total Submissions: 77.3K
# Testcase Example:  '"1"'
#
# Given an integer n, find the closest integer (not including itself), which is
# a palindrome. 
# 
# The 'closest' is defined as absolute difference minimized between two
# integers.
# 
# Example 1:
# 
# Input: "123"
# Output: "121"
# 
# 
# 
# Note:
# 
# The input n is a positive integer represented by string, whose length will
# not exceed 18.
# If there is a tie, return the smaller one as answer.
# 
# 
#
class Solution:
    def nearestPalindromic(self, n: str) -> str:

        len_n = len(n)
        is_odd = len_n % 2

        int_n = int(n[:len_n // 2 + is_odd])

        max_Plaindromic = str(10**len_n + 1)
        min_Plaindromic = str(10**(len_n-1) - 1)

        if abs(int(min_Plaindromic) - int(n)) > abs(int(max_Plaindromic) - int(n)):
            nearestPalindromic = max_Plaindromic
        else:
            nearestPalindromic = min_Plaindromic

        for i in [-1, 0, 1]:
            nearestPalindromic_i = list(str(int_n + i))
            tmp = list(str(int_n + i))
            tmp.reverse()
            if is_odd:
                del tmp[0]
            nearestPalindromic_i.extend(tmp)
            if "".join(nearestPalindromic_i) == n:
                continue
            if abs(int(nearestPalindromic)-int(n))>abs(int(''.join(nearestPalindromic_i))-int(n)):
               nearestPalindromic=''.join(nearestPalindromic_i)

        return nearestPalindromic
            


        


        

