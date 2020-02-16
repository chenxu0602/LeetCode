#
# @lc app=leetcode id=1315 lang=python3
#
# [1315] Sum of Nodes with Even-Valued Grandparent
#
# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/
#
# algorithms
# Medium (83.63%)
# Likes:    142
# Dislikes: 6
# Total Accepted:    10.3K
# Total Submissions: 12.3K
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
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node, parent_even=False):
            if not node: return
            if parent_even:
                if node.left:
                    self.res += node.left.val
                if node.right:
                    self.res += node.right.val
            if node.val % 2 == 0:
                dfs(node.left, parent_even=True)
                dfs(node.right, parent_even=True)
            else:
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.res
        
# @lc code=end

