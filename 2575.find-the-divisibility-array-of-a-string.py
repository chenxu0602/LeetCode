#
# @lc app=leetcode id=2575 lang=python3
#
# [2575] Find the Divisibility Array of a String
#

# @lc code=start
class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:

        ans = []
        prefix = 0
        for i, v in enumerate(word):
            prefix = prefix * 10 + ord(v) - 48
            prefix %= m
            if prefix == 0:
                ans.append(1)
            else:
                ans.append(0)

        return ans
        
# @lc code=end

