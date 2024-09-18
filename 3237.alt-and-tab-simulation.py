#
# @lc app=leetcode id=3237 lang=python3
#
# [3237] Alt and Tab Simulation
#

# @lc code=start
class Solution:
    def simulationResult(self, windows: List[int], queries: List[int]) -> List[int]:

        ans, visited = [], set()

        for q in queries[::-1]:
            if q not in visited:
                visited.add(q)
                ans += q,

        for w in windows:
            if w not in visited:
                ans += w,

        return ans
        
# @lc code=end

