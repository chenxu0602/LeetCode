#
# @lc app=leetcode id=2748 lang=python3
#
# [2748] Number of Beautiful Pairs
#

# @lc code=start
import math

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:

        ans = 0

        first = list(map(lambda x: int(str(x)[0]), nums))
        last = list(map(lambda x: x % 10, nums))

        for i, n1 in enumerate(first):
            for n2 in last[i + 1:]:
                ans += math.gcd(n1, n2) == 1

        return ans

        
# @lc code=end

