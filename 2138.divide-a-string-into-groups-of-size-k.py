#
# @lc app=leetcode id=2138 lang=python3
#
# [2138] Divide a String Into Groups of Size k
#

# @lc code=start
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        return [(s+k*fill)[i*k:i*k+k] for i in range(len(s)//k+(0<len(s)%k))]
        
# @lc code=end

