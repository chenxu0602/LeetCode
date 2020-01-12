#
# @lc app=leetcode id=996 lang=python3
#
# [996] Number of Squareful Arrays
#
# https://leetcode.com/problems/number-of-squareful-arrays/description/
#
# algorithms
# Hard (47.78%)
# Likes:    183
# Dislikes: 14
# Total Accepted:    7.6K
# Total Submissions: 16K
# Testcase Example:  '[1,17,8]'
#
# Given an array A of non-negative integers, the array is squareful if for
# every pair of adjacent elements, their sum is a perfect square.
# 
# Return the number of permutations of A that are squareful.  Two permutations
# A1 and A2 differ if and only if there is some index i such that A1[i] !=
# A2[i].
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,17,8]
# Output: 2
# Explanation: 
# [1,8,17] and [17,8,1] are the valid permutations.
# 
# 
# Example 2:
# 
# 
# Input: [2,2,2]
# Output: 1
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 12
# 0 <= A[i] <= 1e9
# 
#
from collections import Counter
import math

class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
        N = len(A)
        count = Counter(A)
        graph = {x: [] for x in count}
        for x in count:
            for y in count:
                if int((x+y)**.5 + 0.5) ** 2 == x + y:
                    graph[x].append(y)

        def dfs(x, todo):
            count[x] -= 1
            if todo == 0:
                ans = 1
            else:
                ans = 0
                for y in graph[x]:
                    if count[y]:
                        ans += dfs(y, todo - 1)
            count[x] += 1
            return ans

        return sum(dfs(x, len(A) - 1) for x in count)

        """
        def backtrack(i, A):
            if i > 1:
                val = A[i-2] + A[i-1]
                is_square = math.sqrt(val) == math.floor(math.sqrt(val))
                if not is_square:
                    return
            if i == len(A):
                output.append(A)
                return

            for j in range(i, len(A)):
                A[i], A[j] = A[j], A[i]

                search = (i, A[i], tuple(A[:i]))
                if search not in seen:
                    seen.add(search)
                    backtrack(i+1, A)

                A[i], A[j] = A[j], A[i]

        output = []
        seen = set()
        backtrack(0, A)
        return len(output)
        """
        

