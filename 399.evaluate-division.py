#
# @lc app=leetcode id=399 lang=python3
#
# [399] Evaluate Division
#
# https://leetcode.com/problems/evaluate-division/description/
#
# algorithms
# Medium (47.61%)
# Likes:    1339
# Dislikes: 105
# Total Accepted:    82.5K
# Total Submissions: 172.7K
# Testcase Example:  '[["a","b"],["b","c"]]\n[2.0,3.0]\n' +
#
# Equations are given in the format A / B = k, where A and B are variables
# represented as strings, and k is a real number (floating point number). Given
# some queries, return the answers. If the answer does not exist, return -1.0.
# 
# Example:
# Given  a / b = 2.0, b / c = 3.0.
# queries are:  a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
# return  [6.0, 0.5, -1.0, 1.0, -1.0 ].
# 
# The input is:  vector<pair<string, string>> equations, vector<double>&
# values, vector<pair<string, string>> queries , where equations.size() ==
# values.size(), and the values are positive. This represents the equations.
# Return  vector<double>.
# 
# According to the example above:
# 
# 
# equations = [ ["a", "b"], ["b", "c"] ],
# values = [2.0, 3.0],
# queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]
# ]. 
# 
# 
# 
# The input is always valid. You may assume that evaluating the queries will
# result in no division by zero and there is no contradiction.
# 
#
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Floyd–Warshall algorithm
        # O(V^3)
        # quotes = defaultdict(dict)
        # for (num, den), val in zip(equations, values):
        #     quotes[num][num] = quotes[den][den] = 1.0
        #     quotes[num][den] = val
        #     quotes[den][num] = 1.0 / val

        # for q in quotes:
        #     for i in quotes[q]:
        #         for j in quotes[q]:
        #             quotes[i][j] = quotes[i][q] * quotes[q][j]

        # return [quotes[num].get(den, -1.0) for num, den in queries]

        g = defaultdict(set)
        for (x, y), v in zip(equations, values):
            g[x].add((y, v))
            g[y].add((x, 1.0 / v))

        def bfs(src, dst):
            if not (src in g and dst in g):
                return -1

            q, seen = [(src, 1.0)], set()
            for x, v in q:
                if x == dst: return v
                seen.add(x)
                for y, k in g[x]:
                    if y not in seen:
                        q.append((y, v * k))
                        seen.add(y)

            return -1.0

        return [bfs(s, d) for s, d in queries]




