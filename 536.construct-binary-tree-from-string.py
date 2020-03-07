#
# @lc app=leetcode id=536 lang=python3
#
# [536] Construct Binary Tree from String
#
# https://leetcode.com/problems/construct-binary-tree-from-string/description/
#
# algorithms
# Medium (47.07%)
# Likes:    339
# Dislikes: 82
# Total Accepted:    24.2K
# Total Submissions: 51.4K
# Testcase Example:  '"4(2(3)(1))(6(5))"'
#
# You need to construct a binary tree from a string consisting of parenthesis
# and integers. 
# 
# The whole input represents a binary tree. It contains an integer followed by
# zero, one or two pairs of parenthesis. The integer represents the root's
# value and a pair of parenthesis contains a child binary tree with the same
# structure. 
# 
# You always start to construct the left child node of the parent first if it
# exists.
# 
# Example:
# 
# Input: "4(2(3)(1))(6(5))"
# Output: return the tree root node representing the following tree:
# 
# ⁠      4
# ⁠    /   \
# ⁠   2     6
# ⁠  / \   / 
# ⁠ 3   1 5   
# 
# 
# 
# Note:
# 
# There will only be '(',  ')',  '-' and  '0' ~ '9' in the input string.
# An empty tree is represented by "" instead of "()".
# 
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
    def str2tree(self, s: str) -> TreeNode:

        # def t(val, left=None, right=None):
        #     node, node.left, node.right = TreeNode(val), left, right
        #     return node
        # return eval("t(" + s.replace("(", ",t(") + ")") if s else None


        def dfs(s, i):
            start = i
            while i < len(s) and (s[i] == '-' or s[i].isdigit()):
                i += 1
            node = TreeNode(int(s[start:i]))

            if i < len(s) and s[i] == '(':
                i += 1
                node.left, i = dfs(s, i)
                i += 1
            if i < len(s) and s[i] == '(':
                i += 1
                node.right, i = dfs(s, i)
                i += 1
            return node, i

        if not s or len(s) == 0: 
            return None
        root, _ = dfs(s, 0)
        return root

        
# @lc code=end

