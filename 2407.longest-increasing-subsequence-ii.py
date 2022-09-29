#
# @lc app=leetcode id=2407 lang=python3
#
# [2407] Longest Increasing Subsequence II
#

# @lc code=start
class SEG:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * 2 * self.n

    def query(self, l, r):
        l += self.n
        r += self.n
        ans = 0
        while l < r:
            if l & 1:
                ans = max(ans, self.tree[l])
                l += 1
            
            if r & 1:
                r -= 1
                ans = max(ans, self.tree[r])

            l >>= 1
            r >>= 1
        return ans

    def update(self, i, val):
        i += self.n
        self.tree[i] = val
        while i > 1:
            i >>= 1
            self.tree[i] = max(self.tree[i * 2], self.tree[i * 2 + 1])

class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:
        n, ans = max(nums), 1
        seg = SEG(n)
        for x in nums:
            x -= 1
            premax = seg.query(max(0, x - k), x)
            ans = max(ans, premax + 1)
            seg.update(x, premax + 1)
        return ans
        
# @lc code=end

