#
# @lc app=leetcode id=3292 lang=python3
#
# [3292] Minimum Number of Valid Strings to Form Target II
#

# @lc code=start

class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:

        # KMP + Greedy
        def prefix_function(s):
            n = len(s)
            lps = [0] * n
            for i in range(1, n):
                j = lps[i - 1]
                while j > 0 and s[i] != s[j]:
                    j = lps[j - 1]
                if s[i] == s[j]:
                    j += 1
                lps[i] = j
            return lps

        l = len(target)
        ps = [0] * (l + 1)
        for word in words:
            lps = prefix_function(word + '#' + target)
            for i in range(1, l + 1):
                ps[i] = max(ps[i], lps[len(word) + i])

        res = 0
        while l and ps[l]:
            l -= ps[l]
            res += 1
        return res if l == 0 else -1


