#
# @lc app=leetcode id=2193 lang=python3
#
# [2193] Minimum Number of Moves to Make Palindrome
#

# @lc code=start
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        res = 0
        while s:
            i = s.index(s[-1])
            if i == len(s) - 1:
                res += i // 2
            else:
                res += i
                s.pop(i)
            s.pop()
        return res
        
# @lc code=end

