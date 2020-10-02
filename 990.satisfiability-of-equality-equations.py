#
# @lc app=leetcode id=990 lang=python3
#
# [990] Satisfiability of Equality Equations
#
# https://leetcode.com/problems/satisfiability-of-equality-equations/description/
#
# algorithms
# Medium (44.82%)
# Likes:    582
# Dislikes: 5
# Total Accepted:    21.3K
# Total Submissions: 46.8K
# Testcase Example:  '["a==b","b!=a"]'
#
# Given an array equations of strings that represent relationships between
# variables, each string equations[i] has length 4 and takes one of two
# different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not
# necessarily different) that represent one-letter variable names.
# 
# Return true if and only if it is possible to assign integers to variable
# names so as to satisfy all the given equations.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is
# satisfied, but not the second.  There is no way to assign the variables to
# satisfy both equations.
# 
# 
# 
# Example 2:
# 
# 
# Input: ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
# 
# 
# 
# Example 3:
# 
# 
# Input: ["a==b","b==c","a==c"]
# Output: true
# 
# 
# 
# Example 4:
# 
# 
# Input: ["a==b","b!=c","c==a"]
# Output: false
# 
# 
# 
# Example 5:
# 
# 
# Input: ["c==c","b==d","x!=z"]
# Output: true
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] and equations[i][3] are lowercase letters
# equations[i][1] is either '=' or '!'
# equations[i][2] is '='
# 
# 
# 
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # Connected Components
        # Time  complexity: O(N) where N is the length of equations.
        # Space complexity: O(1)
        graph = [[] for _ in range(26)]

        for eqn in equations:
            if eqn[1] == '=':
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                graph[x].append(y)
                graph[y].append(x)

        color = [None] * 26
        t = 0
        for start in range(26):
            if color[start] is None:
                t += 1
                stack = [start]
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if color[nei] is None:
                            color[nei] = t
                            stack.append(nei)

        for eqn in equations:
            if eqn[1] == '!':
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                if x == y: return False
                if color[x] is not None and color[x] == color[y]:
                    return False

        return True


        # Union Rank
        # p, rank = list(range(26)), [0] * 26
        # def find(x):
        #     if p[x] != x:
        #         p[x] = find(p[x])
        #     return p[x]

        # def union(x, y):
        #     xr, yr = map(find, (x, y))
        #     if xr != yr:
        #         if rank[xr] < rank[yr]:
        #             xr, yr = yr, xr
        #         p[yr], rank[xr] = xr, rank[xr] + 1

        # eqs, neqs = [], []
        # for a, e, _, b in equations:
        #     a, b = ord(a) - 97, ord(b) - 97
        #     if e == '=':
        #         eqs.append((a, b))
        #     else:
        #         neqs.append((a, b))

        # for a, b in eqs:
        #     union(a, b)

        # for a, b in neqs:
        #     if find(a) == find(b):
        #         return False

        # return True
        
# @lc code=end

