#
# @lc app=leetcode id=2453 lang=python3
#
# [2453] Destroy Sequential Targets
#

# @lc code=start
from collections import Counter

class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:

        count = Counter(x % space for x in nums)
        maxc = max(count.values())
        return min(x for x in nums if count[x % space] == maxc)
        
# @lc code=end

