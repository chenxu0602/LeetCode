#
# @lc app=leetcode id=2432 lang=python3
#
# [2432] The Employee That Worked on the Longest Task
#

# @lc code=start
class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:

        prev, ans = 0, (0, 0)

        for id, curr in logs:
            ans = min(ans, (prev - curr, id))
            prev = curr

        return ans[1]
        
# @lc code=end

