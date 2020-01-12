#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# https://leetcode.com/problems/count-complete-tree-nodes/description/
#
# algorithms
# Medium (35.73%)
# Likes:    1286
# Dislikes: 157
# Total Accepted:    152.6K
# Total Submissions: 402.6K
# Testcase Example:  '[1,2,3,4,5,6]'
#
# Given a complete binary tree, count the number of nodes.
# 
# Note: 
# 
# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is
# completely filled, and all nodes in the last level are as far left as
# possible. It can have between 1 and 2^h nodes inclusive at the last level h.
# 
# Example:
# 
# 
# Input: 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \  /
# 4  5 6
# 
# Output: 6
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
    def countNodes(self, root: TreeNode) -> int:
#        return 1 + self.countNodes(root.left) + self.countNodes(root.right) if root else 0

        """
        def getDepth(root):
            if not root:
                return 0

            return 1 + getDepth(root.left)

        if not root:
            return 0

        leftDepth = getDepth(root.left)
        rightDepth = getDepth(root.right)

        if leftDepth == rightDepth:
            return pow(2, leftDepth) + self.countNodes(root.right)
        else:
            return pow(2, rightDepth) + self.countNodes(root.left)
        """

        def getHeight(root):
            height = 0
            while root:
                height += 1
                root = root.left
            return height

        count = 0
        while root:
            l, r = map(getHeight, (root.left, root.right))
            if l == r:
                count += 2 ** l
                root = root.right
            else:
                count += 2 ** r
                root = root.left

        return count

        
# @lc code=end

