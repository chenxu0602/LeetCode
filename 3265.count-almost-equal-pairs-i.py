#
# @lc app=leetcode id=3265 lang=python3
#
# [3265] Count Almost Equal Pairs I
#

# @lc code=start
from collections import defaultdict
from itertools import combinations
from math import log10

class Solution:
    def countPairs(self, nums: List[int]) -> int:
        d, ans = defaultdict(list), 0
        max_ = int(log10(max(nums))) + 1
        nums = map(lambda x: (str(x).rjust(max_, '0')), nums)

        for num in nums:
            d[''.join(sorted(num))] += num,

        for k in d:
            for s1, s2 in combinations(d[k], 2):
                if sum(c1 != c2 for c1, c2 in zip(s1, s2)) < 3:
                    ans += 1

        return ans


        
# @lc code=end

