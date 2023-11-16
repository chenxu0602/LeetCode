#
# @lc app=leetcode id=2924 lang=python3
#
# [2924] Find Champion II
#

# @lc code=start
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:

        weak = {b for a, b in edges}
        return -1 if len(weak) < n - 1 else n * (n - 1) // 2 - sum(weak)

        
# @lc code=end

