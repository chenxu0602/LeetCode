#
# @lc app=leetcode id=2265 lang=python3
#
# [2265] Count Nodes Equal to Average of Subtree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            nonlocal ans

            if not node: return 0, 0

            ls, ln = dfs(node.left)
            rs, rn = dfs(node.right)

            s = node.val + ls + rs
            n = 1 + ln + rn

            if s // n == node.val:
                ans += 1

            return s, n

        ans = 0
        dfs(root)
        return ans
        
# @lc code=end

