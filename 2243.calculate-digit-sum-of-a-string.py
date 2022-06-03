#
# @lc app=leetcode id=2243 lang=python3
#
# [2243] Calculate Digit Sum of a String
#

# @lc code=start
class Solution:
    def digitSum(self, s: str, k: int) -> str:

        while len(s) > k:
            s = "".join(str(sum(map(int, s[i:i + k]))) for i in range(0, len(s), k))
        return s
        
# @lc code=end

