#
# @lc app=leetcode id=2940 lang=python3
#
# [2940] Find Building Where Alice and Bob Can Meet
#

# @lc code=start
import heapq

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:

        cmp = lambda x, y: 0 if x == y else 1 if x > y else -1

        stack, heap = [[] for h in heights], []
        ans = [-1] * len(queries)
        for i, (a, b) in enumerate(queries):
            if cmp(a, b) == cmp(heights[a], heights[b]):
                ans[i] = max(a, b)
            else:
                stack[max(a, b)].append([max(heights[a], heights[b]), i])

        for i, height in enumerate(heights):
            while heap and heap[0][0] < height:
                ans[heapq.heappop(heap)[1]] = i

            for st in stack[i]:
                heapq.heappush(heap, st)

        return ans

        
# @lc code=end

