#
# @lc app=leetcode id=897 lang=python3
#
# [897] Increasing Order Search Tree
#
# https://leetcode.com/problems/increasing-order-search-tree/description/
#
# algorithms
# Easy (70.40%)
# Likes:    771
# Dislikes: 474
# Total Accepted:    73.6K
# Total Submissions: 103.1K
# Testcase Example:  '[5,3,6,2,4,null,8,1,null,null,null,7,9]\r'
#
# Given a binary search tree, rearrange the tree in in-order so that the
# leftmost node in the tree is now the root of the tree, and every node has no
# left child and only 1 right child.
# 
# 
# Example 1:
# Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]
# 
# ⁠      5
# ⁠     / \
# ⁠   3    6
# ⁠  / \    \
# ⁠ 2   4    8
# /        / \ 
# 1        7   9
# 
# Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
# 
# ⁠1
# \
# 2
# \
# 3
# \
# 4
# \
# 5
# \
# 6
# \
# 7
# \
# 8
# \
# ⁠                9  
# 
# Constraints:
# 
# 
# The number of nodes in the given tree will be between 1 and 100.
# Each node will have a unique integer value from 0 to 1000.
# 
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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        # In-Order Traversal
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # def inorder(node):
        #     if node:
        #         yield from inorder(node.left)
        #         yield node.val
        #         yield from inorder(node.right)

        # ans = cur = TreeNode(None)
        # for v in inorder(root):
        #     cur.right = TreeNode(v)
        #     cur = cur.right
        # return ans.right


        # Traversal with Relinking
        # Time  complexity: O(N)
        # Space complexity: O(H)
        def inorder(node):
            if node:
                inorder(node.left)
                node.left = None
                self.cur.right = node
                self.cur = node
                inorder(node.right)

        ans = self.cur = TreeNode(None)
        inorder(root)
        return ans.right
        
# @lc code=end

