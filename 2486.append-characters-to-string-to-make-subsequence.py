#
# @lc app=leetcode id=2486 lang=python3
#
# [2486] Append Characters to String to Make Subsequence
#

# @lc code=start
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        """
        i = j = 0
        while i < len(s) and j < len(t):
            j += s[i] == t[j]
            i += 1

        return len(t) - j
        """

        it = iter(s)
        for i, c in enumerate(t):
            if c not in it:
                return len(t) - i

        return 0
        
# @lc code=end

