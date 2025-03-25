#
# @lc app=leetcode id=3273 lang=python3
#
# [3273] Minimum Amount of Damage Dealt to Bob
#

# @lc code=start
from functools import cmp_to_key

class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:

        time_to_kill = [(h + power - 1) // power for h in health]
        ans, sum_ = 0, sum(damage)
        arr = sorted([(d / t, t, d) for t, d in zip(time_to_kill, damage)])
        while arr:
            _, t, d = arr.pop()
            ans += sum_ * t
            sum_ -= d
        return ans



        # n = len(damage)
        # time_to_kill = [(h + power - 1) // power for h in health]
        # indices = sorted(range(n), key=cmp_to_key(lambda i, j: time_to_kill[i] * damage[j] - time_to_kill[j] * damage[i]))

        # res, curTime = 0, 0
        # for idx in indices:
        #     curTime += time_to_kill[idx]
        #     res += curTime * damage[idx]

        # return res

        
# @lc code=end

