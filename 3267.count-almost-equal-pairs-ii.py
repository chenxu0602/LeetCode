#
# @lc app=leetcode id=3267 lang=python3
#
# [3267] Count Almost Equal Pairs II
#

# @lc code=start

from collections import Counter, defaultdict
from itertools import combinations

class Solution:
    def countPairs(self, nums: List[int]) -> int:

        counts = Counter(nums)
        freq = defaultdict(list)
        for c, v in counts.items():
            freq[c] += (c, v),
            s = list(str(c).zfill(7))
            for j in range(7):
                for k in range(j + 1, 7):
                    if s[j] != s[k]:
                        s[j], s[k] = s[k], s[j]
                        candidate = int(''.join(s))
                        freq[candidate] += (c, v),
                        s[j], s[k] = s[k], s[j]

        res = Counter()
        for c, vals in freq.items():
            for x1, v1 in vals:
                res[x1, x1] = v1 * (v1 - 1) // 2
            for (x1, v1), (x2, v2) in combinations(vals, 2):
                res[x1, x2] = v1 * v2

        return sum(res.values())


        
# @lc code=end

