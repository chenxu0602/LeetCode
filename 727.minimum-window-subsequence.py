#
# @lc app=leetcode id=727 lang=python3
#
# [727] Minimum Window Subsequence
#
# https://leetcode.com/problems/minimum-window-subsequence/description/
#
# algorithms
# Hard (37.71%)
# Likes:    343
# Dislikes: 17
# Total Accepted:    17.8K
# Total Submissions: 47K
# Testcase Example:  '"abcdebdde"\n"bde"'
#
# Given strings S and T, find the minimum (contiguous) substring W of S, so
# that T is a subsequence of W.
# 
# If there is no such window in S that covers all characters in T, return the
# empty string "". If there are multiple such minimum-length windows, return
# the one with the left-most starting index.
# 
# Example 1:
# 
# 
# Input: 
# S = "abcdebdde", T = "bde"
# Output: "bcde"
# Explanation: 
# "bcde" is the answer because it occurs before "bdde" which has the same
# length.
# "deb" is not a smaller window because the elements of T in the window must
# occur in order.
# 
# 
# 
# 
# Note:
# 
# 
# All the strings in the input will only contain lowercase letters.
# The length of S will be in the range [1, 20000].
# The length of T will be in the range [1, 100].
# 
# 
# 
#
from functools import lru_cache

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        @lru_cache(None)
        def dfs(i, j):
            if j == len(T): return i
            ind = S.find(T[j], i + 1)
            if ind == -1:
                return float("inf")
            else:
                return dfs(ind, j + 1)

        l, res = float("inf"), ""
        for i, s in enumerate(S):
            if s == T[0]:
                j = dfs(i, 1)
                if j - i < l:
                    l, res = j - i, S[i:j + 1]

        return res



        # Dynamic Programming 
        # Time  complexity: O(S x T)
        # Space compleixty: O(S)
        # cur = [i if x == T[0] else None for i, x in enumerate(S)]
        # for j in range(1, len(T)):
        #     last = None
        #     new = [None] * len(S)
        #     # Now we would like to calculate the candidate windows
        #     # "new" for T[:j+1].  'last' is the last window seen. 
        #     for i, u in enumerate(S):
        #         if last is not None and u == T[j]:
        #             new[i] = last
        #         if cur[i] is not None:
        #             last = cur[i]
        #     cur = new

        # # Looking at the window data cur, choose the smallest length window [s, e].
        # ans = 0, len(S)
        # for e, s in enumerate(cur):
        #     if s is not None and s >= 0 and e - s < ans[1] - ans[0]:
        #         ans = s, e

        # return S[ans[0]:ans[1] + 1] if ans[1] < len(S) else ""


        # Dynamic Programming 
        # Time  complexity: O(S x T)
        # Space compleixty: O(S)
        # N = len(S)
        # nxt = [None] * N
        # last = [-1] * 26
        # for i in range(N - 1, -1, -1):
        #     last[ord(S[i]) - ord('a')] = i
        #     nxt[i] = tuple(last)

        # windows = [[i, i] for i, c in enumerate(S) if c == T[0]]
        # for j in range(1, len(T)):
        #     letter_index = ord(T[j]) - ord('a')
        #     windows = [[root, nxt[i + 1][letter_index]]
        #                for root, i in windows
        #                if 0 <= i < N - 1 and nxt[i + 1][letter_index] >= 0]

        # if not windows: return ""
        # i, j = min(windows, key=lambda x: x[1] - x[0])
        # return S[i:j + 1]
        


        

