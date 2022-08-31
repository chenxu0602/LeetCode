#
# @lc app=leetcode id=2379 lang=python3
#
# [2379] Minimum Recolors to Get K Consecutive Black Blocks
#

# @lc code=start
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:

        n = len(blocks)
        i = 0
        res = 0
        for j in range(k):
            if blocks[j] == 'W':
                res += 1

        ans = res
        for j in range(k, n):
            if blocks[j] == 'W':
                res += 1
            res -= blocks[i] == 'W'
            ans = min(res, ans)
            i += 1

        return ans
        
# @lc code=end

