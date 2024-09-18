#
# @lc app=leetcode id=3228 lang=python3
#
# [3228] Maximum Number of Operations to Move Ones to the End
#

# @lc code=start
class Solution:
    def maxOperations(self, s: str) -> int:

        # For each 0 we count how many 1s can pass it
        res, cnt = 0, 0
        for num in list(map(len, s.split('0'))):
            if num == 0: continue
            cnt += num
            res += cnt

        # Check if the last bit is 0
        return res if num == 0 else res - cnt

        
# @lc code=end

