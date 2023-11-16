#
# @lc app=leetcode id=2933 lang=python3
#
# [2933] High-Access Employees
#

# @lc code=start
from collections import defaultdict

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:

        d, ans = defaultdict(list), []

        for e, t in access_times:
            d[e].append(60 * int(t[:2]) + int(t[2:]))

        for e in d:
            d[e].sort()

            for x, y in zip(d[e], d[e][2:]):
                if y - x < 60:
                    ans += e,
                    break

        return ans
        
# @lc code=end

