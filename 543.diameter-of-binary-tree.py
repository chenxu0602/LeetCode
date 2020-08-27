#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (48.34%)
# Likes:    3291
# Dislikes: 202
# Total Accepted:    356.9K
# Total Submissions: 736.6K
# Testcase Example:  '[1,2,3,4,5]'
#
# 
# Given a binary tree, you need to compute the length of the diameter of the
# tree. The diameter of a binary tree is the length of the longest path between
# any two nodes in a tree. This path may or may not pass through the root.
# 
# 
# 
# Example:
# Given a binary tree 
# 
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \     
# ⁠     4   5    
# 
# 
# 
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
# 
# 
# Note:
# The length of path between two nodes is represented by the number of edges
# between them.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # Time  complexity: O(N)
        # Space complexity: O(N), the size of our implicit call stack during our depth first search.
        def dfs(node):
            if not node: return 0
            L, R = map(dfs, (node.left, node.right))
            self.ans = max(self.ans, L + R)
            return max(L, R) + 1

        self.ans = 0
        dfs(root)
        return self.ans
        
# @lc code=end

