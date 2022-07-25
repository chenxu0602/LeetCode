#
# @lc app=leetcode id=2334 lang=python3
#
# [2334] Subarray With Elements Greater Than Varying Threshold
#

# @lc code=start
import enum


class Union:
    def __init__(self, N):
        self.par = list(range(N))
        self.rnk = [0] * N
        self.siz = [1] * N

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        xr, yr = map(self.find, (x, y))
        if xr == yr: return False
        if self.rnk[xr] < self.rnk[yr]:
            xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1

        self.par[yr] = xr
        self.siz[xr] += self.siz[yr]
        return True

    def size(self, x):
        return self.siz[self.find(x)]


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:

        """
        n = len(nums)
        ks = []
        for i, v in enumerate(nums):
            ks.append((threshold // v + 1, i))
        ks.sort()

        uf = Union(n)
        seen = set()
        for k, i in ks:
            if i - 1 in seen: uf.union(i, i - 1)
            if i + 1 in seen: uf.union(i, i + 1)

            if uf.size(i) >= k:
                return k

            seen.add(i)
        
        return -1
        """

        nums = [0] + nums + [0]
        stack = [0]

        for i in range(1, len(nums)):
            while nums[i] < nums[stack[-1]]:
                tmp = nums[stack.pop()]
                if tmp > threshold / (i - stack[-1] - 1):
                    return i - stack[-1] - 1

            stack.append(i)

        return -1

        
        
# @lc code=end

