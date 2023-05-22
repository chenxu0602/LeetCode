#
# @lc app=leetcode id=2698 lang=python3
#
# [2698] Find the Punishment Number of an Integer
#

# @lc code=start
from functools import lru_cache

class Solution:
    def punishmentNumber(self, n: int) -> int:

        @lru_cache(None)
        def possible(sum_added, cached_sum, n, target):
            if not n:
                return target == sum_added + cached_sum

            num = int(n[0])
            cas = cached_sum

            return possible(sum_added, cas * 10 + num, n[1:], target) \
                or possible(sum_added + cas, num, n[1:], target)

        ans = 0
        for i in range(1, n + 1):
            if possible(0, 0, str(i * i), i):
                ans += i * i

        return ans
        
# @lc code=end

