#
# @lc app=leetcode id=2509 lang=python3
#
# [2509] Cycle Length Queries in a Tree
#

# @lc code=start
class Solution:
    def cycleLengthQueries(self, n: int, queries: List[List[int]]) -> List[int]:

        res = []
        for x, y in queries:
            res.append(1)
            while x != y:
                x, y = min(x, y), max(x, y) // 2
                res[-1] += 1

        return res
        
# @lc code=end

