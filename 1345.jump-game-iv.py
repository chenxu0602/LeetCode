#
# @lc app=leetcode id=1345 lang=python3
#
# [1345] Jump Game IV
#
# https://leetcode.com/problems/jump-game-iv/description/
#
# algorithms
# Hard (39.96%)
# Likes:    298
# Dislikes: 20
# Total Accepted:    14.9K
# Total Submissions: 37.2K
# Testcase Example:  '[100,-23,-23,404,100,23,23,23,3,404]'
#
# Given an array of integers arr, you are initially positioned at the first
# index of the array.
# 
# In one step you can jump from index i to index:
# 
# 
# i + 1 where: i + 1 < arr.length.
# i - 1 where: i - 1 >= 0.
# j where: arr[i] == arr[j] and i != j.
# 
# 
# Return the minimum number of steps to reach the last index of the array.
# 
# Notice that you can not jump outside of the array at any time.
# 
# 
# Example 1:
# 
# 
# Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
# Output: 3
# Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that
# index 9 is the last index of the array.
# 
# 
# Example 2:
# 
# 
# Input: arr = [7]
# Output: 0
# Explanation: Start index is the last index. You don't need to jump.
# 
# 
# Example 3:
# 
# 
# Input: arr = [7,6,9,6,9,6,9,7]
# Output: 1
# Explanation: You can jump directly from index 0 to index 7 which is last
# index of the array.
# 
# 
# Example 4:
# 
# 
# Input: arr = [6,1,9]
# Output: 2
# 
# 
# Example 5:
# 
# 
# Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 5 * 10^4
# -10^8 <= arr[i] <= 10^8
# 
# 
#

# @lc code=start
from collections import defaultdict
import itertools

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # O(N)

        # Breadth-First Search
        # n = len(arr)
        # if n <= 1:
        #     return 0

        # graph = {}
        # for i in range(n):
        #     if arr[i] in graph:
        #         graph[arr[i]].append(i)
        #     else:
        #         graph[arr[i]] = [i]

        # curs = [0]
        # visited = {0}
        # step = 0

        # while curs:
        #     nex = []

        #     for node in curs:
        #         if node == n - 1:
        #             return step

        #         for child in graph[arr[node]]:
        #             if child not in visited:
        #                 visited.add(child)
        #                 nex.append(child)

        #         graph[arr[node]].clear()

        #         for child in (node - 1, node + 1):
        #             if 0 <= child < len(arr) and child not in visited:
        #                 visited.add(child)
        #                 nex.append(child)

        #     curs = nex
        #     step += 1

        # return -1


        # Bidirectional BFS
        # n = len(arr)
        # if n <= 1:
        #     return 0

        # graph = {}
        # for i in range(n):
        #     if arr[i] in graph:
        #         graph[arr[i]].append(i)
        #     else:
        #         graph[arr[i]] = [i]

        # curs = [0]
        # visited = {0, n - 1}
        # step = 0

        # other = [n - 1]
        # while curs:
        #     if len(curs) > len(other):
        #         curs, other = other, curs
        #     nex = []

        #     for node in curs:
        #         for child in graph[arr[node]]:
        #             if child in other:
        #                 return step + 1
        #             if child not in visited:
        #                 visited.add(child)
        #                 nex.append(child)

        #         graph[arr[node]].clear()

        #         for child in (node - 1, node + 1):
        #             if child in other:
        #                 return step + 1
        #             if 0 <= child < len(arr) and child not in visited:
        #                 visited.add(child)
        #                 nex.append(child)

        #     curs = nex
        #     step += 1

        # return -1


        indices = defaultdict(list)
        for i, v in enumerate(arr):
            indices[v].append(i)

        done, now = {-1}, {0}
        for steps in itertools.count():
            done |= now
            if len(arr) - 1 in done:
                return steps
            now = {j for i in now for j in [i - 1, i + 1] + indices.pop(arr[i], [])} - done

        
# @lc code=end

