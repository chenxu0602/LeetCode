#
# @lc app=leetcode id=1042 lang=python3
#
# [1042] Flower Planting With No Adjacent
#
# https://leetcode.com/problems/flower-planting-with-no-adjacent/description/
#
# algorithms
# Easy (48.53%)
# Likes:    416
# Dislikes: 476
# Total Accepted:    32.8K
# Total Submissions: 68K
# Testcase Example:  '3\n[[1,2],[2,3],[3,1]]'
#
# You have n gardens, labeled from 1 to n, and an array paths where paths[i] =
# [xi, yi] describes the existence of a bidirectional path from garden xi to
# garden yi. In each garden, you want to plant one of 4 types of flowers.
# 
# There is no garden that has more than three paths coming into or leaving it.
# 
# Your task is to choose a flower type for each garden such that, for any two
# gardens connected by a path, they have different types of flowers.
# 
# Return any such a choice as an array answer, where answer[i] is the type of
# flower planted in the (i+1)^th garden.  The flower types are denoted 1, 2, 3,
# or 4.  It is guaranteed an answer exists.
# 
# 
# Example 1:
# Input: n = 3, paths = [[1,2],[2,3],[3,1]]
# Output: [1,2,3]
# Example 2:
# Input: n = 4, paths = [[1,2],[3,4]]
# Output: [1,2,1,2]
# Example 3:
# Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
# Output: [1,2,3,4]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^4
# 0 <= paths.length <= 2 * 10^4
# paths[i].length == 2
# 1 <= xi, yi <= n
# xi != yi
# No garden has four or more paths coming into or leaving it.
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        res = [0] * n
        g = defaultdict(list)
        for x, y in paths:
            g[x - 1].append(y - 1)
            g[y - 1].append(x - 1)

        for i in range(n):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in g[i]}).pop()

        return res
        
# @lc code=end

