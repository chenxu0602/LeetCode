#
# @lc app=leetcode id=2365 lang=python3
#
# [2365] Task Scheduler II
#

# @lc code=start
from collections import defaultdict

class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:

        last = defaultdict(lambda: -len(tasks) - 10)
        res = 0
        for t in tasks:
            last[t] = res = max(res, last[t] + space) + 1
        return res

        
# @lc code=end

