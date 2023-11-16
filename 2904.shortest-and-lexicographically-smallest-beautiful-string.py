#
# @lc app=leetcode id=2904 lang=python3
#
# [2904] Shortest and Lexicographically Smallest Beautiful String
#

# @lc code=start
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        # We collect the indices of ones in ones.
        ones = [i for i, v in enumerate(s) if v == '1']
        if len(ones) < k: return ''

        # We determine the delimiting indices l and r of those candidate strings incands that (a) start and end with one and (b) containkones.
        candidates = list(zip(ones, ones[k - 1:]))

        # We determine minLen, the minimum r-l of elements in cands.
        minLen = min(r - l for l, r in candidates)

        # We filtercandsto only include those candidates for which l-r = minLen
        candidates = list(filter(lambda x: x[1] - x[0] == minLen, candidates))

        # We determine the lexicographically smallest substring withmin.
        return min(s[l:r + 1] for l, r in candidates)
        
# @lc code=end


