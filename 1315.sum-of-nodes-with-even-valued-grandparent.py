#
# @lc app=leetcode id=1315 lang=python3
#
# [1315] Sum of Nodes with Even-Valued Grandparent
#
# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/
#
# algorithms
# Medium (83.72%)
# Likes:    657
# Dislikes: 29
# Total Accepted:    47.3K
# Total Submissions: 56.5K
# Testcase Example:  '[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]'
#
# Given a binary tree, return the sum of values of nodes with even-valued
# grandparent.  (A grandparent of a node is the parent of its parent, if it
# exists.)
# 
# If there are no nodes with an even-valued grandparent, return 0.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
# Output: 18
# Explanation: The red nodes are the nodes with even-value grandparent while
# the blue nodes are the even-value grandparents.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is between 1 and 10^4.
# The value of nodes is between 1 and 100.
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
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        # O(N) / O(H)
        def dfs(node, par=1, grandpar=1):
            return dfs(node.left, node.val, par) \
                + dfs(node.right, node.val, par) \
                + node.val * (1 - grandpar % 2) if node else 0

        return dfs(root)
        
# @lc code=end

