#
# @lc app=leetcode id=2747 lang=python3
#
# [2747] Count Zero Request Servers
#

# @lc code=start
class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:

        logs = sorted(logs, key=lambda x: x[1])
        s, e = 0, 0

        ans = {}
        cur = [0] * (n + 1)
        cnt = 0

        for q in sorted(queries):
            while e < len(logs) and logs[e][1] <= q:
                cur[logs[e][0]] += 1
                if cur[logs[e][0]] == 1:
                    cnt += 1
                e += 1

            while s < len(logs) and logs[s][1] < q - x:
                cur[logs[s][0]] -= 1
                if cur[logs[s][0]] == 0:
                    cnt -= 1
                s += 1

            ans[q] = n - cnt

        return [ans[q] for q in queries]
                
        
# @lc code=end

