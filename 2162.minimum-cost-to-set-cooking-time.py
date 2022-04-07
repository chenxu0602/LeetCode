#
# @lc app=leetcode id=2162 lang=python3
#
# [2162] Minimum Cost to Set Cooking Time
#

# @lc code=start
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:

        def cost(mins, secs):
            s, curr, res = str(mins * 100 + secs), str(startAt), 0
            for ch in s:
                if ch == curr:
                    res += pushCost
                else:
                    res += (pushCost + moveCost)
                    curr = ch
            return res

        maxmins, ans = targetSeconds // 60, float("inf")
        for mins in range(maxmins + 1):
            secs = targetSeconds - mins * 60
            if secs > 99 or mins > 99: continue
            ans = min(ans, cost(mins, secs))

        return ans

        
# @lc code=end

