#
# @lc app=leetcode id=943 lang=python3
#
# [943] Find the Shortest Superstring
#
# https://leetcode.com/problems/find-the-shortest-superstring/description/
#
# algorithms
# Hard (38.62%)
# Likes:    204
# Dislikes: 57
# Total Accepted:    6.2K
# Total Submissions: 15.6K
# Testcase Example:  '["alex","loves","leetcode"]'
#
# Given an array A of strings, find any smallest string that contains each
# string in A as a substring.
# 
# We may assume that no string in A is substring of another string in A.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["alex","loves","leetcode"]
# Output: "alexlovesleetcode"
# Explanation: All permutations of "alex","loves","leetcode" would also be
# accepted.
# 
# 
# 
# Example 2:
# 
# 
# Input: ["catg","ctaagt","gcta","ttca","atgcatc"]
# Output: "gctaagttcatgcatc"
# 
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 12
# 1 <= A[i].length <= 20
# 
# 
# 
# 
# 
#
from functools import lru_cache

class Solution:
    def shortestSuperstring(self, A: List[str]) -> str:

        """
        N = len(A)

        overlaps = [[0] * N for _ in range(N)]
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in range(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:ans]):
                            overlaps[i][j] = ans
                            break

        dp = [[0] * N for _ in range(1 << N)]                            
        parent = [[None] * N for _ in range(1 << N)]
        for mask in range(1, 1 << N):
            for bit in range(N):
                if (mask >> bit) & 1:
                    pmask = mask ^ (1 << bit)
                    if pmask == 0: continue
                    for i in range(N):
                        if (pmask >> i) & 1:
                            value = dp[pmask][i] + overlaps[i][bit]
                            if value > dp[mask][bit]:
                                dp[mask][bit] = value
                                parent[mask][bit] = i

        perm = []
        mask = (1 << N) - 1
        i = max(range(N), key=dp[-1].__getitem__)
        while i is not None:
            perm.append(i)
            mask, i = mask ^ (1 << i), parent[mask][i]

        perm = perm[::-1]
        seen = [False] * N
        for x in perm:
            seen[x] = True
        perm.extend([i for i in range(N) if not seen[i]])

        ans = [A[perm[0]]]
        for i in range(1, len(perm)):
            overlap = overlaps[perm[i-1]][perm[i]]
            ans.append(A[perm[i]][overlap:])

        return "".join(ans)
        """

        n = len(A)
        graph = [[0] * n for _ in range(n)]
        for i, word1 in enumerate(A):
            for j, word2 in enumerate(A):
                if i == j: continue
                for k in range(min(len(word1), len(word2)))[::-1]:
                    if word1[:-k] == word2[:k]:
                        graph[i][j] = k
                        break

                
        @lru_cache(None)
        def search(i, k):
            if not (i & (1 << k)): return ""
            if i == (1 << k): return A[k]
            ans = ""
            for j in range(n):
                if j != k and i & (1 << j):
                    candidate = search(i ^ (1 << k), j) + A[k][graph[j][k]:]
                    if ans == "" or len(candidate) < len(ans):
                        ans = candidate
            return ans
            

        res = ""
        for k in range(n):
            candidate = search((1 << n) - 1, k)
            if res == "" or len(candidate) < len(res):
                res = candidate
        return res
        

