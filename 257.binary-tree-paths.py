#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
# https://leetcode.com/problems/binary-tree-paths/description/
#
# algorithms
# Easy (48.97%)
# Likes:    1319
# Dislikes: 87
# Total Accepted:    281.5K
# Total Submissions: 572.3K
# Testcase Example:  '[1,2,3,null,5]'
#
# Given a binary tree, return all root-to-leaf paths.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# 
# Input:
# 
# ⁠  1
# ⁠/   \
# 2     3
# ⁠\
# ⁠ 5
# 
# Output: ["1->2->5", "1->3"]
# 
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        # def dfs(node, path):
        #     if node:
        #         if node.left is node.right:
        #             res.append('->'.join(map(str, path + [node.val])))

        #         if node.left:
        #             dfs(node.left, path + [node.val])

        #         if node.right:
        #             dfs(node.right, path + [node.val])

        # res = []
        # dfs(root, [])
        # return res

        if not root: return []
        res = []
        stack = [(root, [])]

        while stack:
            node, path = stack.pop()
            if node:
                if node.left is node.right:
                    res.append('->'.join(map(str, path + [node.val])))

                if node.left:
                    stack.append((node.left, path + [node.val]))

                if node.right:
                    stack.append((node.right, path + [node.val]))

        return res
        
# @lc code=end

