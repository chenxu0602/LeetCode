#
# @lc app=leetcode id=2597 lang=python3
#
# [2597] The Number of Beautiful Subsets
#

# @lc code=start
from collections import Counter, deque
import operator, functools

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:

        """
        n = len(nums)
        res = 0

        def dfs(i, ctr):
            nonlocal res
            if i == n:
                if ctr:
                    res += 1
                return

            if nums[i] - k not in ctr and nums[i] + k not in ctr:
                ctr[nums[i]] += 1
                dfs(i + 1, ctr)
                ctr[nums[i]] -= 1
                if not ctr[nums[i]]:
                    del ctr[nums[i]]

            dfs(i + 1, ctr)

        dfs(0, Counter())
        return res
        """

        """
        queue = deque([([], -1)])
        res = 0

        while queue:
            cur, idx = queue.popleft()
            res += 1

            for i in range(idx + 1, len(nums)):
                if nums[i] - k in cur or nums[i] + k in cur:
                    continue

                queue.append((cur + [nums[i]], i))

        return res - 1
        """

        """
        # dp0 is the ways that without A[i]
        # dp1 is the ways that with A[i]

        count = [Counter() for i in range(k)]
        for n in nums:
            count[n % k][n] += 1

        res = 1
        for i in range(k):
            prev, dp0, dp1 = 0, 1, 0
            for n in sorted(count[i]):
                v = pow(2, count[i][n])
                if prev + k == n:
                    dp0, dp1 = dp0 + dp1, dp0 * (v - 1)
                else:
                    dp0, dp1 = dp0 + dp1, (dp0 + dp1) * (v - 1)

                prev = n

            res *= dp0 + dp1

        return res - 1
        """

        # Count the frequency of A, and then consider all the arithmetic sequence with difference k.
        # Each arithmetic sequence can be solve as a hourse robber problem.
        # We solve the hourse robber by dp.
        # dp(a) return the result for sequence no bigger than a.

        # dp(a)[0] is the ways that without a
        # dp(a)[1] is the ways that with a

        # dp(a)[0] = dp(a - k)[0] + dp(a - k)[1]
        # dp(a)[1] = dp(a - k)[0] * (2 ^ count(a) - 1

        count = Counter(nums)

        def dp(n):
            dp0, dp1 = dp(n - k) if n - k in count else (1, 0)
            return dp0 + dp1, dp0 * (pow(2, count[n]) - 1)

        return functools.reduce(operator.mul, (sum(dp(n)) for n in count if not count[n + k])) - 1
        
# @lc code=end

