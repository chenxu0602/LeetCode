#
# @lc app=leetcode id=2234 lang=python3
#
# [2234] Maximum Total Beauty of the Gardens
#

# @lc code=start
import bisect

class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:

        # Greedy
        # Time  complexity: O(nlogn)
        # Space complexity: O(n)
        flowers = [min(target, x) for x in flowers]
        flowers.sort()

        if min(flowers) == target: return full * len(flowers)
        if newFlowers >= target * len(flowers) - sum(flowers):
            return max(full * len(flowers), full * (len(flowers) - 1) + partial * (target - 1))

        cost = [0]
        for i in range(1, len(flowers)):
            pre = cost[-1]
            cost.append(pre + i * (flowers[i] - flowers[i - 1]))

        j = len(flowers) - 1
        while flowers[j] == target:
            j -= 1

        ans = 0
        while newFlowers >= 0:
            idx = min(j, bisect.bisect_right(cost, newFlowers) - 1)

            bar = flowers[idx] + (newFlowers - cost[idx]) // (idx + 1)

            ans = max(ans, bar * partial + full * (len(flowers) - j - 1))

            newFlowers -= (target - flowers[j])

            j -= 1

        return ans

        
# @lc code=end

