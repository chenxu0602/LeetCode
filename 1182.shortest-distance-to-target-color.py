#
# @lc app=leetcode id=1182 lang=python3
#
# [1182] Shortest Distance to Target Color
#
# https://leetcode.com/problems/shortest-distance-to-target-color/description/
#
# algorithms
# Medium (51.78%)
# Likes:    73
# Dislikes: 2
# Total Accepted:    3.7K
# Total Submissions: 7.2K
# Testcase Example:  '[1,1,2,1,3,2,2,3,3]\n[[1,3],[2,2],[6,1]]'
#
# You are given an array colors, in which there are three colors: 1, 2 and 3.
# 
# You are also given some queries. Each query consists of two integers i and c,
# return the shortest distance between the given index i and the target color
# c. If there is no solution return -1.
# 
# 
# Example 1:
# 
# 
# Input: colors = [1,1,2,1,3,2,2,3,3], queries = [[1,3],[2,2],[6,1]]
# Output: [3,0,3]
# Explanation: 
# The nearest 3 from index 1 is at index 4 (3 steps away).
# The nearest 2 from index 2 is at index 2 itself (0 steps away).
# The nearest 1 from index 6 is at index 3 (3 steps away).
# 
# 
# Example 2:
# 
# 
# Input: colors = [1,2], queries = [[0,3]]
# Output: [-1]
# Explanation: There is no 3 in the array.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= colors.length <= 5*10^4
# 1 <= colors[i] <= 3
# 1 <= queries.length <= 5*10^4
# queries[i].length == 2
# 0 <= queries[i][0] < colors.length
# 1 <= queries[i][1] <= 3
# 
# 
#

# @lc code=start
from collections import defaultdict
import bisect

class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        d, res = defaultdict(list), []
        for i in range(len(colors)):
            d[colors[i]].append(i)

        for i, c in queries:
            if c not in d:
                res.append(-1)
                continue

            l = d[c]
            t = bisect.bisect_left(l, i)
            if t == 0:
                res.append(l[0] - i)
            elif t == len(l):
                res.append(i - l[-1])
            else:
                res.append(min(l[t] - i, i - l[t - 1]))

        return res
        
# @lc code=end

