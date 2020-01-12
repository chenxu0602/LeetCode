#
# @lc app=leetcode id=756 lang=python3
#
# [756] Pyramid Transition Matrix
#
# https://leetcode.com/problems/pyramid-transition-matrix/description/
#
# algorithms
# Medium (52.57%)
# Likes:    197
# Dislikes: 276
# Total Accepted:    14.9K
# Total Submissions: 28.3K
# Testcase Example:  '"ABC"\n["ABD","BCE","DEF","FFF"]'
#
# We are stacking blocks to form a pyramid. Each block has a color which is a
# one letter string.
# 
# We are allowed to place any color block C on top of two adjacent blocks of
# colors A and B, if and only if ABC is an allowed triple.
# 
# We start with a bottom row of bottom, represented as a single string. We also
# start with a list of allowed triples allowed. Each allowed triple is
# represented as a string of length 3.
# 
# Return true if we can build the pyramid all the way to the top, otherwise
# false.
# 
# Example 1:
# 
# 
# Input: bottom = "BCD", allowed = ["BCG", "CDE", "GEA", "FFF"]
# Output: true
# Explanation:
# We can stack the pyramid like this:
# ⁠   A
# ⁠  / \
# ⁠ G   E
# ⁠/ \ / \
# B   C   D
# 
# We are allowed to place G on top of B and C because BCG is an allowed
# triple.  Similarly, we can place E on top of C and D, then A on top of G and
# E.
# 
# 
# 
# Example 2:
# 
# 
# Input: bottom = "AABA", allowed = ["AAA", "AAB", "ABA", "ABB", "BAC"]
# Output: false
# Explanation:
# We can't stack the pyramid to the top.
# Note that there could be allowed triples (A, B, C) and (A, B, D) with C !=
# D.
# 
# 
# 
# 
# Note:
# 
# 
# bottom will be a string with length in range [2, 8].
# allowed will have length in range [0, 200].
# Letters in all strings will be chosen from the set {'A', 'B', 'C', 'D', 'E',
# 'F', 'G'}.
# 
# 
# 
# 
#
from collections import defaultdict
from itertools import product

class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        """
        T = defaultdict(set)
        for u, v, w in allowed:
            T[u, v].add(w)

        seen = set()
        def solve(A):
            if len(A) == 1:
                return True
            if A in seen: 
                return False
            seen.add(A)
            return any(solve(cand) for cand in build(A, []))

        def build(A, ans, i=0):
            if i + 1 == len(A):
                yield "".join(ans)
            else:
                for w in T[A[i], A[i+1]]:
                    ans.append(w)
                    for result in build(A, ans, i+1):
                        yield result
                    ans.pop()

        return solve(bottom)
        """

        f = defaultdict(lambda: defaultdict(list))
        for a, b, c in allowed: f[a][b].append(c)

        def pyramid(bottom):
            if len(bottom) == 1: return True
            for i in product(*(f[a][b] for a, b in zip(bottom, bottom[1:]))):
                if pyramid(i): return True
            return False
        return pyramid(bottom)


        

