#
# @lc app=leetcode id=767 lang=python3
#
# [767] Reorganize String
#
# https://leetcode.com/problems/reorganize-string/description/
#
# algorithms
# Medium (43.42%)
# Likes:    649
# Dislikes: 34
# Total Accepted:    33.1K
# Total Submissions: 76K
# Testcase Example:  '"aab"'
#
# Given a string S, check if the letters can be rearranged so that two
# characters that are adjacent to each other are not the same.
# 
# If possible, output any possible result.  If not possible, return the empty
# string.
# 
# Example 1:
# 
# 
# Input: S = "aab"
# Output: "aba"
# 
# 
# Example 2:
# 
# 
# Input: S = "aaab"
# Output: ""
# 
# 
# Note:
# 
# 
# S will consist of lowercase letters and have length in range [1, 500].
# 
# 
# 
# 
#
import heapq

class Solution:
    def reorganizeString(self, S: str) -> str:
        # N = len(S)
        # A = []
        # for c, x in sorted((S.count(x), x) for x in set(S)):
        #     if c > (N+1) // 2:
        #         return ""
        #     A.extend(c * x)
        # ans = [None] * N
        # ans[::2], ans[1::2] = A[N//2:], A[:N//2]
        # return "".join(ans)

        # Greedy with Heap
        # Time  complexity: O(NlogA), where N is the length of S and A is the size of the alphabet.
        # Space complexity: O(A)
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)
        if any(-nc > (len(S) + 1) // 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            ans.extend([ch1, ch2])

            if nct1 + 1:
                heapq.heappush(pq, (nct1+1, ch1))

            if nct2 + 1:
                heapq.heappush(pq, (nct2+1, ch2))

        return "".join(ans) + (pq[0][1] if pq else "")

        

