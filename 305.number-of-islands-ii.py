#
# @lc app=leetcode id=305 lang=python3
#
# [305] Number of Islands II
#
# https://leetcode.com/problems/number-of-islands-ii/description/
#
# algorithms
# Hard (40.57%)
# Likes:    705
# Dislikes: 15
# Total Accepted:    67.8K
# Total Submissions: 167.2K
# Testcase Example:  '3\n3\n[[0,0],[0,1],[1,2],[2,1]]'
#
# A 2d grid map of m rows and n columns is initially filled with water. We may
# perform an addLand operation which turns the water at position (row, col)
# into a land. Given a list of positions to operate, count the number of
# islands after each addLand operation. An island is surrounded by water and is
# formed by connecting adjacent lands horizontally or vertically. You may
# assume all four edges of the grid are all surrounded by water.
# 
# Example:
# 
# 
# Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
# Output: [1,1,2,3]
# 
# 
# Explanation:
# 
# Initially, the 2d grid grid is filled with water. (Assume 0 represents water
# and 1 represents land).
# 
# 
# 0 0 0
# 0 0 0
# 0 0 0
# 
# 
# Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
# 
# 
# 1 0 0
# 0 0 0   Number of islands = 1
# 0 0 0
# 
# 
# Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
# 
# 
# 1 1 0
# 0 0 0   Number of islands = 1
# 0 0 0
# 
# 
# Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
# 
# 
# 1 1 0
# 0 0 1   Number of islands = 2
# 0 0 0
# 
# 
# Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
# 
# 
# 1 1 0
# 0 0 1   Number of islands = 3
# 0 1 0
# 
# 
# Follow up:
# 
# Can you do it in time complexity O(k log mn), where k is the length of the
# positions?
# 
#

# @lc code=start
class Union:
    def __init__(self):
        self.id = {}
        self.sz = {}
        self.count = 0

    def add(self, p):
        self.id[p] = p
        self.sz[p] = 1
        self.count += 1

    def root(self, label):
        while label != self.id[label]:
            self.id[label] = label = self.id[self.id[label]]
        return label

    def unite(self, p, q):
        i, j = map(self.root, (p, q))
        if i == j: return 
        if self.sz[i] > self.sz[j]:
            i, j = j, i
        self.id[i] = j
        self.sz[j] += self.sz[i]
        self.count -= 1


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:

        ans, islands = [], Union()
        for p in map(tuple, positions):
            if p in islands.id:
                ans += ans[-1],
                continue
            islands.add(p)
            for dp in (0, 1), (0, -1), (1, 0), (-1, 0):
                q = (p[0] + dp[0], p[1] + dp[1])
                if q in islands.id:
                    islands.unite(p, q)
            ans += islands.count,
        return ans


        
# @lc code=end

