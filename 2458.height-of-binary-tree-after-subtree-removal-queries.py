#
# @lc app=leetcode id=2458 lang=python3
#
# [2458] Height of Binary Tree After Subtree Removal Queries
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:

        """
        depths, heights = defaultdict(int), defaultdict(int)

        def dfs(node, depth):
            if not node: return -1
            depths[node.val] = depth
            cur = max(dfs(node.left, depth + 1), dfs(node.right, depth + 1)) + 1
            heights[node.val] = cur
            return cur

        dfs(root, 0)

        cousins = defaultdict(list)
        for val, depth in depths.items():
            cousins[depth].append((-heights[val], val))
            cousins[depth].sort()
            if len(cousins[depth]) > 2:
                cousins[depth].pop()

        ans = []
        for q in queries:
            depth = depths[q]
            if len(cousins[depth]) == 1:
                ans.append(depth - 1)
            elif cousins[depth][0][1] == q:
                ans.append(-cousins[depth][1][0] + depth)
            else:
                ans.append(-cousins[depth][0][0] + depth)

        return ans
        """

        res = defaultdict(int)

        def dfs(node, h, maxh):
            if not node: return maxh
            res[node.val] = max(res[node.val], maxh)
            node.left, node.right = node.right, node.left
            return dfs(node.right, h + 1, dfs(node.left, h + 1, max(maxh, h)))

        dfs(root, 0, 0)
        dfs(root, 0, 0)
        return [res[q] for q in queries]
        
# @lc code=end

