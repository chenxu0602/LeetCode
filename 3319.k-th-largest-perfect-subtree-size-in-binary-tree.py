#
# @lc app=leetcode id=3319 lang=python3
#
# [3319] K-th Largest Perfect Subtree Size in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestPerfectSubtree(self, root: Optional[TreeNode], k: int) -> int:

        def dfs(node):
            nonlocal res
            if not node: return 0
            l, r = map(dfs, (node.left, node.right))
            if l == r >= 0:
                res += l + 1,
                return l + 1
            return -1

        res = []
        dfs(root)
        return (1 << sorted(res)[-k]) - 1 if k <= len(res) else -1

        
# @lc code=end

