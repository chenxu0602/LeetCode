#
# @lc app=leetcode id=2583 lang=python3
#
# [2583] Kth Largest Sum in a Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:

        vals = []
        stack = [(root, 0)]
        while stack:
            node, i = stack.pop()
            if i == len(vals):
                vals.append(0)
            vals[i] += node.val

            if node.left:
                stack.append((node.left, i + 1))

            if node.right:
                stack.append((node.right, i + 1))

        return sorted(vals, reverse=True)[k - 1] if len(vals) >= k else -1
        
# @lc code=end

