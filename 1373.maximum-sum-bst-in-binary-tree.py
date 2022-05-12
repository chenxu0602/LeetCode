#
# @lc app=leetcode id=1373 lang=python3
#
# [1373] Maximum Sum BST in Binary Tree
#
# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/description/
#
# algorithms
# Hard (38.25%)
# Likes:    301
# Dislikes: 52
# Total Accepted:    11.2K
# Total Submissions: 29.2K
# Testcase Example:  '[1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]'
#
# Given a binary tree root, the task is to return the maximum sum of all keys
# of any sub-tree which is also a Binary Search Tree (BST).
# 
# Assume a BST is defined as follows:
# 
# 
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
# Output: 20
# Explanation: Maximum sum in a valid Binary search tree is obtained in root
# node with key equal to 3.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root = [4,3,null,1,2]
# Output: 2
# Explanation: Maximum sum in a valid Binary search tree is obtained in a
# single root node with key equal to 2.
# 
# 
# Example 3:
# 
# 
# Input: root = [-4,-2,-5]
# Output: 0
# Explanation: All values are negatives. Return an empty BST.
# 
# 
# Example 4:
# 
# 
# Input: root = [2,1,3]
# Output: 6
# 
# 
# Example 5:
# 
# 
# Input: root = [5,4,8,3,null,6,3]
# Output: 7
# 
# 
# 
# Constraints:
# 
# 
# The given binary tree will have between 1 and 40000 nodes.
# Each node's value is between [-4 * 10^4 , 4 * 10^4].
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
    def maxSumBST(self, root: TreeNode) -> int:
        # 1. the status of this subtree, 1 means it's empty, 2 means it's a BST, 0 means it's not a BST
        # 2. size of this subtree (we only care about size of BST though)
        # 3. the minimal value in this subtree
        # 4. the maximal value in this subtree
        def dfs(node):
            if not node:
                return 1, 0, None, None

            ls, l, ll, lr = dfs(node.left)
            rs, r, rl, rr = dfs(node.right)

            if ((ls == 2 and lr < node.val) or ls == 1) and ((rs == 2 and rl > node.val) or rs == 1):
                size = node.val + l + r
                self.res = max(self.res, size)
                return 2, size, (ll if ll else node.val), (rr if rr else node.val)

            return 0, None, None, None

        self.res = 0
        dfs(root)
        return self.res
        
# @lc code=end

