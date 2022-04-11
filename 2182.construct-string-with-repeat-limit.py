#
# @lc app=leetcode id=2182 lang=python3
#
# [2182] Construct String With Repeat Limit
#

# @lc code=start
from collections import Counter
import heapq

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        pq = [(-ord(k), v) for k, v in Counter(s).items()]
        heapq.heapify(pq)
        ans = []

        while pq:
            k, v = heapq.heappop(pq)
            if ans and ans[-1] == k:
                if not pq: break
                kk, vv = heapq.heappop(pq)
                ans.append(kk)
                if vv - 1:
                    heapq.heappush(pq, (kk, vv - 1))
                heapq.heappush(pq, (k, v))
            else:
                m = min(v, repeatLimit)
                ans.extend([k] * m)
                if v - m:
                    heapq.heappush(pq, (k, v - m))

        return "".join(chr(-x) for x in ans)
        
# @lc code=end

