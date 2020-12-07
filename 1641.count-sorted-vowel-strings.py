#
# @lc app=leetcode id=1641 lang=python3
#
# [1641] Count Sorted Vowel Strings
#
# https://leetcode.com/problems/count-sorted-vowel-strings/description/
#
# algorithms
# Medium (76.47%)
# Likes:    255
# Dislikes: 5
# Total Accepted:    12.4K
# Total Submissions: 16.2K
# Testcase Example:  '1'
#
# Given an integer n, return the number of strings of length n that consist
# only of vowels (a, e, i, o, u) and are lexicographically sorted.
# 
# A string s is lexicographically sorted if for all valid i, s[i] is the same
# as or comes before s[i+1] in the alphabet.
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: 5
# Explanation: The 5 sorted strings that consist of vowels only are
# ["a","e","i","o","u"].
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: 15
# Explanation: The 15 sorted strings that consist of vowels only are
# ["aa","ae","ai","ao","au","ee","ei","eo","eu","ii","io","iu","oo","ou","uu"].
# Note that "ea" is not a valid string since 'e' comes after 'a' in the
# alphabet.
# 
# 
# Example 3:
# 
# 
# Input: n = 33
# Output: 66045
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 50 
# 
# 
#

# @lc code=start
class Solution:
    def countVowelStrings(self, n: int) -> int:
        # Time  complexity: O(n^5)
        # Space complexity: O(n)
        # def countVowelStringsUtil(n, vowels):
        #     if n == 0:
        #         return 1
        #     res = 0
        #     for i in range(vowels, 6):
        #         res += countVowelStringsUtil(n - 1, i)
        #     return res

        # return countVowelStringsUtil(n, 1)


        # Time  complexity: O(n^5)
        # Space complexity: O(n)
        # def countVowelStringUtil(n, vowels):
        #     if n == 1:
        #         return vowels
        #     if vowels == 1:
        #         return 1
        #     return countVowelStringUtil(n - 1, vowels) + countVowelStringUtil(n, vowels - 1)

        # return countVowelStringUtil(n, 5)
        
        
        # Bottom Up Dynamic Programming, Tabulation
        # dp[n][vowels] = dp[n - 1][vowels] + dp[n][vowels - 1]
        # Time  complexity: O(n)
        # Space complexity: O(n)
        # dp = [[0] * 6 for _ in range(n + 1)]
        # for vowel in range(1, 6):
        #     dp[1][vowel] = vowel
        # for nValue in range(2, n + 1):
        #     dp[nValue][1] = 1
        #     for vowel in range(2, 6):
        #         dp[nValue][vowel] = dp[nValue][vowel - 1] + dp[nValue - 1][vowel]
        # return dp[n][5]


        # From k = 5 vowels choose n vowels with repetion.
        # (k, n) = (k + n - 1)! / (k - 1)! / n!
        import math
        return math.factorial(5 + n - 1) // math.factorial(5 - 1) // math.factorial(n)


# @lc code=end

