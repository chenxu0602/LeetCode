#
# @lc app=leetcode id=2375 lang=python3
#
# [2375] Construct Smallest Number From DI String
#

# @lc code=start
class Solution:
    def smallestNumber(self, pattern: str) -> str:

        res, stack = [], []
        for i, c in enumerate(pattern + 'I', 1):
            stack.append(str(i))
            if c == 'I':
                res += stack[::-1]
                stack = []
        return ''.join(res)

        
# @lc code=end

