#
# @lc app=leetcode id=1631 lang=python3
#
# [1631] Path With Minimum Effort
#
# https://leetcode.com/problems/path-with-minimum-effort/description/
#
# algorithms
# Medium (40.42%)
# Likes:    362
# Dislikes: 15
# Total Accepted:    8.9K
# Total Submissions: 21.9K
# Testcase Example:  '[[1,2,2],[3,8,2],[5,3,5]]'
#
# You are a hiker preparing for an upcoming hike. You are given heights, a 2D
# array of size rows x columns, where heights[row][col] represents the height
# of cell (row, col). You are situated in the top-left cell, (0, 0), and you
# hope to travel to the bottom-right cell, (rows-1, columns-1) (i.e.,
# 0-indexed). You can move up, down, left, or right, and you wish to find a
# route that requires the minimum effort.
# 
# A route's effort is the maximum absolute difference in heights between two
# consecutive cells of the route.
# 
# Return the minimum effort required to travel from the top-left cell to the
# bottom-right cell.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: heights = [[1,2,2],[3,8,2],[5,3,5]]
# Output: 2
# Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2
# in consecutive cells.
# This is better than the route of [1,2,2,2,5], where the maximum absolute
# difference is 3.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: heights = [[1,2,3],[3,8,4],[5,3,5]]
# Output: 1
# Explanation: The route of [1,2,3,4,5] has a maximum absolute difference of 1
# in consecutive cells, which is better than route [1,3,5,3,5].
# 
# 
# Example 3:
# 
# 
# Input: heights =
# [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# Output: 0
# Explanation: This route does not require any effort.
# 
# 
# 
# Constraints:
# 
# 
# rows == heights.length
# columns == heights[i].length
# 1 <= rows, columns <= 100
# 1 <= heights[i][j] <= 10^6
# 
# 
#

# @lc code=start
import heapq

class Union:
    def __init__(self, N):
        self.par = list(range(N))
        self.rnk = [0] * N

    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = map(self.find, (x, y))
        if xr == yr: return False
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1
        self.par[yr] = xr
        return True

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Brute Force using Backtracking
        # Time  complexity: O(3^(mn))
        # Space compleixty: O(mn)
        # rows, cols = map(len, (heights, heights[0]))
        # self.max_so_far = float("inf")

        # def dfs(x, y, max_difference):
        #     if x == rows - 1 and y == cols - 1:
        #         self.max_so_far = min(self.max_so_far, max_difference)
        #         return max_difference

        #     current_height = heights[x][y]
        #     heights[x][y] = 0
        #     min_effort = float("inf")

        #     for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        #         nx, ny = x + dx, y + dy
        #         if 0 <= nx < rows and 0 <= ny < cols and heights[nx][ny]:
        #             current_diff = abs(heights[nx][ny] - current_height)
        #             max_current_diff = max(max_difference, current_diff)
        #             if max_current_diff < self.max_so_far:
        #                 result = dfs(nx, ny, max_current_diff)
        #                 min_effort = min(min_effort, result)

        #     heights[x][y] = current_height
        #     return min_effort

        # return dfs(0, 0, 0)


        # Variations of Dijkstra's Algorithm
        # Time  complexity: O(mnlog(mn))
        # Space compleixty: O(mn)
        rows, cols = map(len, (heights, heights[0]))
        diff_mat = [[float("inf")] * cols for _ in range(rows)]
        diff_mat[0][0] = 0
        visited = [[False] * cols for _ in range(rows)]
        queue = [(0, 0, 0)] # difference, x, y
        while queue:
            difference, x, y = heapq.heappop(queue)
            visited[x][y] = True
            for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
                nx, ny = x + dx, y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    curr_diff = abs(heights[nx][ny] - heights[x][y])
                    max_diff = max(curr_diff, diff_mat[x][y])

                    if diff_mat[nx][ny] > max_diff:
                        diff_mat[nx][ny] = max_diff

                        heapq.heappush(queue, (max_diff, nx, ny))

        return diff_mat[-1][-1]


        # Union Find - Disjoint Set
        # Time  complexity: O(mnlog(mn))
        # Space compleixty: O(mn)
        # rows, cols = map(len, (heights, heights[0]))
        # if rows == 1 and cols == 1:
        #     return 0

        # edge_list = []
        # for r in range(rows):
        #     for c in range(cols):
        #         if r > 0:
        #             diff = abs(heights[r][c] - heights[r - 1][c])
        #             edge_list.append((diff, r * cols + c, (r - 1) * cols + c))
        #         if c > 0:
        #             diff = abs(heights[r][c] - heights[r][c - 1])
        #             edge_list.append((diff, r * cols + c, r * cols + c - 1))

        # edge_list.sort()
        # union_find = Union(rows * cols)

        # for diff, x, y in edge_list:
        #     union_find.union(x, y)
        #     if union_find.find(0) == union_find.find(rows * cols - 1):
        #         return diff

        # return -1


        # Binary Search Using BFS
        # Time  compleixty: O(mn)
        # Space compleixty: O(mn)
        # def canReachDestination(mid):
        #     visited = [[False] * cols for _ in range(rows)]
        #     queue = [(0, 0)] # x, y
        #     while queue:
        #         x, y = queue.pop(0)
        #         if x == rows - 1 and y == cols - 1:
        #             return True
        #         visited[x][y] = True
        #         for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        #             nx, ny = x + dx, y + dy
        #             if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
        #                 curr_diff = abs(heights[nx][ny] - heights[x][y])
        #                 if curr_diff <= mid:
        #                     visited[nx][ny] = True
        #                     queue.append((nx, ny))

        #     return False

        # rows, cols = map(len, (heights, heights[0]))
        # left, right = 0, 10**7
        # while left < right:
        #     mid = left + (right - left) // 2
        #     if canReachDestination(mid):
        #         right = mid
        #     else:
        #         left = mid + 1
        # return left


        # Binary Search Using DFS
        # Time  compleixty: O(mn)
        # Space compleixty: O(mn)
        # def canReachDestination(x, y, mid):
        #     if x == rows - 1 and y == cols - 1:
        #         return True
        #     visited[x][y] = True
        #     for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        #         nx, ny = x + dx, y + dy
        #         if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
        #             curr_diff = abs(heights[nx][ny] - heights[x][y])
        #             if curr_diff <= mid:
        #                 visited[nx][ny] = True
        #                 if canReachDestination(nx, ny, mid):
        #                     return True

        #     return False

        # rows, cols = map(len, (heights, heights[0]))
        # left, right = 0, 10**7
        # while left < right:
        #     mid = left + (right - left) // 2
        #     visited = [[False] * cols for _ in range(rows)]
        #     if canReachDestination(0, 0, mid):
        #         right = mid
        #     else:
        #         left = mid + 1
        # return left

        
# @lc code=end

