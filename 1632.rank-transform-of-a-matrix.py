#
# @lc app=leetcode id=1632 lang=python3
#
# [1632] Rank Transform of a Matrix
#
# https://leetcode.com/problems/rank-transform-of-a-matrix/description/
#
# algorithms
# Hard (29.54%)
# Likes:    159
# Dislikes: 6
# Total Accepted:    2.6K
# Total Submissions: 8.9K
# Testcase Example:  '[[1,2],[3,4]]'
#
# Given an m x n matrix, return a new matrix answer where answer[row][col] is
# the rank of matrix[row][col].
# 
# The rank is an integer that represents how large an element is compared to
# other elements. It is calculated using the following rules:
# 
# 
# The rank is an integer starting from 1.
# If two elements p and q are in the same row or column, then:
# 
# If p < q then rank(p) < rank(q)
# If p == q then rank(p) == rank(q)
# If p > q then rank(p) > rank(q)
# 
# 
# The rank should be as small as possible.
# 
# 
# It is guaranteed that answer is unique under the given rules.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,2],[3,4]]
# Output: [[1,2],[2,3]]
# Explanation:
# The rank of matrix[0][0] is 1 because it is the smallest integer in its row
# and column.
# The rank of matrix[0][1] is 2 because matrix[0][1] > matrix[0][0] and
# matrix[0][0] is rank 1.
# The rank of matrix[1][0] is 2 because matrix[1][0] > matrix[0][0] and
# matrix[0][0] is rank 1.
# The rank of matrix[1][1] is 3 because matrix[1][1] > matrix[0][1],
# matrix[1][1] > matrix[1][0], and both matrix[0][1] and matrix[1][0] are rank
# 2.
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[7,7],[7,7]]
# Output: [[1,1],[1,1]]
# 
# 
# Example 3:
# 
# 
# Input: matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]
# Output: [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]
# 
# 
# Example 4:
# 
# 
# Input: matrix = [[7,3,6],[1,4,5],[9,8,2]]
# Output: [[5,1,4],[1,2,3],[6,3,1]]
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 500
# -10^9 <= matrix[row][col] <= 10^9
# 
# 
#

# @lc code=start
from collections import defaultdict

class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        # Sorting + BFS
        # Time  complexity: O(mnlogmn)
        # Space complexity: O(mn)
        # m, n = map(len, (matrix, matrix[0]))
        # # link row to col, and link col to row
        # graphs = {} # graphs[v]: the connection graph of value v
        # for i in range(m):
        #     for j in range(n):
        #         v = matrix[i][j]
        #         # if not initialized, initial it
        #         if v not in graphs:
        #             graphs[v] = {}
        #         if i not in graphs[v]:
        #             graphs[v][i] = []
        #         if ~j not in graphs[v]:
        #             graphs[v][~j] = []
        #         # link i to j, and link j to i
        #         graphs[v][i].append(~j)
        #         graphs[v][~j].append(i)

        # # put points into `value2index` dict, grouped by connection
        # value2index = {} # {v: [[points1], [points2], ...], ...}
        # seen = set() # mark whether put into `value2index` or not
        # for i in range(m):
        #     for j in range(n):
        #         if (i, j) in seen:
        #             continue
        #         seen.add((i, j))
        #         v = matrix[i][j]
        #         graph = graphs[v]
        #         # start bfs
        #         q = [i, ~j]
        #         rowcols = {i, ~j} # store visited row and col
        #         while q:
        #             node = q.pop(0)
        #             for rowcol in graph[node]:
        #                 if rowcol not in rowcols:
        #                     q.append(rowcol)
        #                     rowcols.add(rowcol)
        #         # transform rowcols into points
        #         points = set()
        #         for rowcol in rowcols:
        #             for k in graph[rowcol]:
        #                 if k >= 0:
        #                     points.add((k, ~rowcol))
        #                     seen.add((k, ~rowcol))
        #                 else:
        #                     points.add((rowcol, ~k))
        #                     seen.add((rowcol, ~k))
        #         if v not in value2index:
        #             value2index[v] = []
        #         value2index[v].append(points)

        # answer = [[0] * n for _ in range(m)] # the required rank matrix
        # rowmax = [0] * m # rowmax[i]: the max rank in i row
        # colmax = [0] * n # colmax[j]: the max rank in j col
        # for v in sorted(value2index.keys()):
        #     # update by connected points with same value
        #     for points in value2index[v]:
        #         rank = 1
        #         for i, j in points:
        #             rank = max(rank, max(rowmax[i], colmax[j]) + 1)
        #         for i, j in points:
        #             answer[i][j] = rank
        #             # update rowmax and colmax
        #             rowmax[i] = max(rowmax[i], rank)
        #             colmax[j] = max(colmax[j], rank)

        # return answer


        
        # Sorting + DFS
        # Time  complexity: O(mnlogmn)
        # Space complexity: O(mn)
        # m, n = map(len, (matrix, matrix[0]))
        # # link row to col, and link col to row
        # graphs = {} # graphs[v]: the connection graph of value v
        # for i in range(m):
        #     for j in range(n):
        #         v = matrix[i][j]
        #         # if not initialized, initial it
        #         if v not in graphs:
        #             graphs[v] = {}
        #         if i not in graphs[v]:
        #             graphs[v][i] = []
        #         if ~j not in graphs[v]:
        #             graphs[v][~j] = []
        #         # link i to j, and link j to i
        #         graphs[v][i].append(~j)
        #         graphs[v][~j].append(i)

        # # put points into `value2index` dict, grouped by connection
        # value2index = {} # {v: [[points1], [points2], ...], ...}
        # seen = set()

        # def dfs(node, graph, rowcols):
        #     rowcols.add(node)
        #     for rowcol in graph[node]:
        #         if rowcol not in rowcols:
        #             dfs(rowcol, graph, rowcols)

        # for i in range(m):
        #     for j in range(n):
        #         if (i, j) in seen:
        #             continue
        #         seen.add((i, j))
        #         v = matrix[i][j]
        #         graph = graphs[v]
        #         # use dfs to find the connected parts
        #         rowcols = set() # store visited row and col
        #         dfs(i, graph, rowcols)
        #         dfs(~j, graph, rowcols)
        #         # transform rowcols into points
        #         points = set()
        #         for rowcol in rowcols:
        #             for k in graph[rowcol]:
        #                 if k >= 0:
        #                     points.add((k, ~rowcol))
        #                     seen.add((k, ~rowcol))
        #                 else:
        #                     points.add((rowcol, ~k))
        #                     seen.add((rowcol, ~k))

        #         if v not in value2index:
        #             value2index[v] = []
        #         value2index[v].append(points)

        # answer = [[0] * n for _ in range(m)] # the required rank matrix
        # rowmax = [0] * m # rowmax[i]: the max rank in i row
        # colmax = [0] * n # colmax[j]: the max rank in j col
        # for v in sorted(value2index.keys()):
        #     # update by connected points with same value
        #     for points in value2index[v]:
        #         rank = 1
        #         for i, j in points:
        #             rank = max(rank, max(rowmax[i], colmax[j]) + 1)
        #         for i, j in points:
        #             answer[i][j] = rank
        #             # update rowmax and colmax
        #             rowmax[i] = max(rowmax[i], rank)
        #             colmax[j] = max(colmax[j], rank)

        # return answer


        # Sorting + Union-Find
        # Time  complexity: O(mnlogmn)
        # Space complexity: O(mn)
        # m, n = map(len, (matrix, matrix[0]))

        # def find(UF, x):
        #     if x != UF[x]:
        #         UF[x] = find(UF, UF[x])
        #     return UF[x]

        # def union(UF, x, y):
        #     UF.setdefault(x, x)
        #     UF.setdefault(y, y)
        #     UF[find(UF, x)] = find(UF, y)

        # # link row and col together
        # UFs = {}
        # for i in range(m):
        #     for j in range(n):
        #         v = matrix[i][j]
        #         if v not in UFs:
        #             UFs[v] = {}
        #         # union i to j
        #         union(UFs[v], i, ~j)

        # # put points into `value2index` dict, grouped by connection
        # value2index = {}
        # for i in range(m):
        #     for j in range(n):
        #         v = matrix[i][j]
        #         if v not in value2index:
        #             value2index[v] = {}
        #         f  = find(UFs[v], i)
        #         if f not in value2index[v]:
        #             value2index[v][f] = []
        #         value2index[v][f].append((i, j))

        # answer = [[0] * n for _ in range(m)] # the required rank matrix
        # rowmax = [0] * m # rowmax[i]: the max rank in i row
        # colmax = [0] * n # colmax[j]: the max rank in j col
        # for v in sorted(value2index.keys()):
        #     # update by connected points with same value
        #     for points in value2index[v].values():
        #         rank = 1
        #         for i, j in points:
        #             rank = max(rank, max(rowmax[i], colmax[j]) + 1)
        #         for i, j in points:
        #             answer[i][j] = rank
        #             # update rowmax and colmax
        #             rowmax[i] = max(rowmax[i], rank)
        #             colmax[j] = max(colmax[j], rank)

        # return answer


        # dict[a] records all element index [i,j] with A[i][j] = a
        # Time  complexity: O(mnlogmn)
        # Space complexity: O(mn)
        m, n = map(len, (matrix, matrix[0]))
        rank = [0] * (m + n)
        d = defaultdict(list)
        for i in range(m):
            for j in range(n):
                d[matrix[i][j]].append([i, j])

        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]

        for a in sorted(d):
            p = list(range(m + n))
            rank2 = rank[:]
            for i, j in d[a]:
                i, j = find(i), find(j + m)
                p[i] = j
                rank2[j] = max(rank2[i], rank2[j])

            for i, j in d[a]:
                rank[i] = rank[j + m] = matrix[i][j] = rank2[find(i)] + 1

        return matrix


# @lc code=end

