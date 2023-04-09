#
# @lc app=leetcode id=2573 lang=python3
#
# [2573] Find the String with LCP
#

# @lc code=start
class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        # If lcp[i][j] > 0, then A[i] = A[j]
        # If lcp[i][j] == 0, then A[i] != A[j]
        # If A[i] == A[j],
        # then lcp[i][j] = lcp[i+1][j+1] + 1

        n = len(lcp)
        word = [0] * n
        c = 1

        for i in range(n):
            if word[i]: continue
            if c > 26: return ""
            for j in range(i, n):
                if lcp[i][j]:
                    word[j] = c
            c += 1

        for i in range(n):
            for j in range(n):
                v = lcp[i + 1][j + 1] if i + 1 < n and j + 1 < n else 0
                v = v + 1 if word[i] == word[j] else 0
                if lcp[i][j] != v:
                    return ""

        return "".join(chr(ord('a') + i - 1) for i in word)

        
# @lc code=end

