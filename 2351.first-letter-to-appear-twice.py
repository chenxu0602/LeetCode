#
# @lc app=leetcode id=2351 lang=python3
#
# [2351] First Letter to Appear Twice
#

# @lc code=start
class Solution:
    def repeatedCharacter(self, s: str) -> str:

        st = set()
        for c in s:
            if c in st:
                return c
            else:
                st.add(c)

        
# @lc code=end

