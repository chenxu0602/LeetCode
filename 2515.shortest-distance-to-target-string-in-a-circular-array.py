#
# @lc app=leetcode id=2515 lang=python3
#
# [2515] Shortest Distance to Target String in a Circular Array
#

# @lc code=start
class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:

        n = len(words)
        ans = float("inf")

        for i in range(n):
            if words[i] == target:
                ans = min(ans, min(abs(startIndex - i), abs(n - abs(startIndex - i))))

        return -1 if ans == float("inf") else ans
        
# @lc code=end

