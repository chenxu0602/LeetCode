#
# @lc app=leetcode id=2697 lang=python3
#
# [2697] Lexicographically Smallest Palindrome
#

# @lc code=start
class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:

        letters = list(s)

        for i in range(len(s) // 2):
            letters[i] = letters[~i] = min(letters[i], letters[~i])

        return "".join(letters)
        
# @lc code=end

