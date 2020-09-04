#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#
# https://leetcode.com/problems/search-in-a-binary-search-tree/description/
#
# algorithms
# Easy (73.04%)
# Likes:    940
# Dislikes: 120
# Total Accepted:    203.7K
# Total Submissions: 278.5K
# Testcase Example:  '[4,2,7,1,3]\n2'
#
# Given the root node of a binary search tree (BST) and a value. You need to
# find the node in the BST that the node's value equals the given value. Return
# the subtree rooted with that node. If such node doesn't exist, you should
# return NULL.
# 
# For example, 
# 
# 
# Given the tree:
# ⁠       4
# ⁠      / \
# ⁠     2   7
# ⁠    / \
# ⁠   1   3
# 
# And the value to search: 2
# 
# 
# You should return this subtree:
# 
# 
# ⁠     2     
# ⁠    / \   
# ⁠   1   3
# 
# 
# In the example above, if we want to search the value 5, since there is no
# node with value 5, we should return NULL.
# 
# Note that an empty tree is represented by NULL, therefore you would see the
# expected output (serialized tree format) as [], not null.
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
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        # Recursion
        # Time complexity: O(H)
        # Master theorem T(N) = aT(N/b) + Theta(N^d). The equation represents dividing the problem up into a subproblems of size N/b in Theta(N^d) time.
        # Here at a step there is only one subproblem a = 1, its size is a half of the initial problem b = 2,
        # and all this happens in a constant time d = 0, as for the binary search.
        # That means that log_b(a) = d and hence we're dealing with case 2 that results in O(n^log_b(a) x log^(d+1)(N)) = log(N) time complexity.
        # Space complexity: O(H)
        # if root is None or val == root.val:
        #     return root

        # return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)


        # Iteration
        # Time  complexity: O(H)
        # Space complexity: O(1)
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root
        
# @lc code=end

