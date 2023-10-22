#
# @lc app=leetcode id=2767 lang=python3
#
# [2767] Partition String Into Minimum Beautiful Substrings
#

# @lc code=start
powers = tuple(bin(pow(5, i))[2:] for i in range(7))

class Solution:

    def minimumBeautifulSubstrings(self, s: str) -> int:
        
        def dp(s):
            if s in powers: return 1
            if not s: return float("inf")

            return 1 + min((dp(s[len(p):]) for p in powers if s.startswith(p)), default=float("inf"))

        ans = dp(s)
        return ans if ans < float("inf") else -1

        
# @lc code=end

