#
# @lc app=leetcode id=2440 lang=python3
#
# [2440] Create Components With Same Value
#

# @lc code=start
class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:

        tree = [[] for _ in nums]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        def dfs(u, p):
            """ Post-order DFS """
            ans = nums[u]
            for v in tree[u]:
                if v != p:
                    ans += dfs(v, u)
            return 0 if ans == cand else ans

        total = sum(nums)
        for cand in range(max(nums), total // 2 + 1):
            if total % cand == 0 and dfs(0, -1) == 0:
                return total // cand - 1

        return 0
        
# @lc code=end

