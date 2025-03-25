#
# @lc app=leetcode id=3287 lang=python3
#
# [3287] Find the Maximum Sequence Value of Array
#

# @lc code=start
from functools import lru_cache
from collections import defaultdict

class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:


        """
        n = len(nums)

        def get_possible(a):
            t1 = {(0, 0)}
            d = defaultdict(lambda: -1)
            for i, v in enumerate(a):
                t2 = set()
                for taken, val in t1:
                    if taken < k:
                        t2.add((taken + 1, val | v))
                        if taken + 1 == k and val | v not in d:
                            d[val | v] = i + 1
                t1.update(t2)
            return d

        a, b = map(get_possible, (nums, nums[::-1]))
        ans = float('-inf')

        for v1, x in a.items():
            for v2, y in b.items():
                if x + y <= n:
                    ans = max(ans, v1 ^ v2)

        return ans
        """


        n = len(nums)

        @lru_cache(None)
        def dp(i, k, di):
            if k == 0: return {0}
            if i < 0 or i == n: return set()
            return dp(i + di, k, di) | {v | nums[i] for v in dp(i + di, k - 1, di)}

        res = 0
        for i in range(n):
            for a in dp(i, k, -1):
                for b in dp(i + 1, k, 1):
                    res = max(res, a ^ b)

        return res

        
# @lc code=end

