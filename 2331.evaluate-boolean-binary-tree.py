#
# @lc app=leetcode id=2331 lang=python3
#
# [2331] Evaluate Boolean Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:

        if root.val < 2: return root.val

        l, r = map(self.evaluateTree, (root.left, root.right))
        v = root.val ^ 1

        return l & r or l & v or r & v
        
# @lc code=end

