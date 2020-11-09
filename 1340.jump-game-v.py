#
# @lc app=leetcode id=1340 lang=python3
#
# [1340] Jump Game V
#
# https://leetcode.com/problems/jump-game-v/description/
#
# algorithms
# Hard (58.24%)
# Likes:    263
# Dislikes: 13
# Total Accepted:    9.8K
# Total Submissions: 16.8K
# Testcase Example:  '[6,4,14,6,8,13,9,7,10,6,12]\n2'
#
# Given an array of integers arr and an integer d. In one step you can jump
# from index i to index:
# 
# 
# i + x where: i + x < arr.length and  0 < x <= d.
# i - x where: i - x >= 0 and  0 < x <= d.
# 
# 
# In addition, you can only jump from index i to index j if arr[i] > arr[j] and
# arr[i] > arr[k] for all indices k between i and j (More formally min(i, j) <
# k < max(i, j)).
# 
# You can choose any index of the array and start jumping. Return the maximum
# number of indices you can visit.
# 
# Notice that you can not jump outside of the array at any time.
# 
# 
# Example 1:
# 
# 
# Input: arr = [6,4,14,6,8,13,9,7,10,6,12], d = 2
# Output: 4
# Explanation: You can start at index 10. You can jump 10 --> 8 --> 6 --> 7 as
# shown.
# Note that if you start at index 6 you can only jump to index 7. You cannot
# jump to index 5 because 13 > 9. You cannot jump to index 4 because index 5 is
# between index 4 and 6 and 13 > 9.
# Similarly You cannot jump from index 3 to index 2 or index 1.
# 
# 
# Example 2:
# 
# 
# Input: arr = [3,3,3,3,3], d = 3
# Output: 1
# Explanation: You can start at any index. You always cannot jump to any
# index.
# 
# 
# Example 3:
# 
# 
# Input: arr = [7,6,5,4,3,2,1], d = 1
# Output: 7
# Explanation: Start at index 0. You can visit all the indicies. 
# 
# 
# Example 4:
# 
# 
# Input: arr = [7,1,7,1,7,1], d = 2
# Output: 2
# 
# 
# Example 5:
# 
# 
# Input: arr = [66], d = 1
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= arr.length <= 1000
# 1 <= arr[i] <= 10^5
# 1 <= d <= arr.length
# 
#

# @lc code=start
from functools import lru_cache
from collections import defaultdict

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        # Time  complexity: O(n x d)
        # Space complexity: O(n)
        # def dp(i):
        #     if res[i]: 
        #         return res[i]
        #     res[i] = 1
        #     for di in (-1, 1):
        #         for j in range(i + di, i + d * di + di, di):
        #             if not (0 <= j < n and arr[j] < arr[i]):
        #                 break
        #             res[i] = max(res[i], dp(j) + 1)
        #     return res[i]

        # n = len(arr)
        # res = [0] * n
        # return max(map(dp, range(n)))


        # We can only jump lower, and one step needs the result from its lower step. 
        # So we sort A[i] do the dp starting from the smallest.
        # For each A[i], we check the lower step on the left and right.
        # This process is O(D) on both side.
        # Time  complexity: O(n x log(n) + n x d)
        # Space complexity: O(n)
        n = len(arr)
        dp = [1] * n
        for a, i in sorted([a, i] for i, a in enumerate(arr)):
            for di in (-1, 1):
                for j in range(i + di, i + d * di + di, di):
                    if not (0 <= j < n and arr[j] < arr[i]):
                        break
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


        # O(n)

        # n = len(arr)
        # dp = [1] * (n + 1)
        # stack = []
        # for i, a in enumerate(arr + [float("inf")]):
        #     while stack and arr[stack[-1]] < a:
        #         L = [stack.pop()]
        #         while stack and arr[stack[-1]] == arr[L[0]]:
        #             L.append(stack.pop())

        #         for j in L:
        #             if i - j <= d:
        #                 dp[i] = max(dp[i], dp[j] + 1)
        #             if stack and j - stack[-1] <= d:
        #                 dp[stack[-1]] = max(dp[stack[-1]], dp[j] + 1)

        #     stack.append(i)

        # return max(dp[:-1])



        def jump(iterator):
            stack = []
            for i in iterator:
                while stack and arr[stack[-1]] < arr[i]:
                    j = stack.pop()
                    if abs(i - j) <= d:
                        graph[j].append(i)
                stack.append(i)

        n = len(arr)
        graph = defaultdict(list)

        jump(range(n))
        jump(reversed(range(n)))

        @lru_cache(None)
        def height(i):
            return 1 + max(map(height, graph[i]), default=0)

        return max(map(height, range(n)))
        
# @lc code=end

