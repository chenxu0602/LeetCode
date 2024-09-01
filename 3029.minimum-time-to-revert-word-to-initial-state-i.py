#
# @lc app=leetcode id=3029 lang=python3
#
# [3029] Minimum Time to Revert Word to Initial State I
#

# @lc code=start
class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:

        cnt, n = 0, len(word)
        for i in range(1, n // k + 1):
            cnt = i 
            if word[k * i:] == word[:n - k * i]:
                return i

        return cnt + 1


        
# @lc code=end

