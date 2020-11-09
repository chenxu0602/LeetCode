#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#
# https://leetcode.com/problems/balance-a-binary-search-tree/description/
#
# algorithms
# Medium (75.48%)
# Likes:    398
# Dislikes: 23
# Total Accepted:    21.9K
# Total Submissions: 29.1K
# Testcase Example:  '[1,null,2,null,3,null,4,null,null]'
#
# Given a binary search tree, return a balanced binary search tree with the
# same node values.
# 
# A binary search tree is balanced if and only if the depth of the two subtrees
# of every node never differ by more than 1.
# 
# If there is more than one answer, return any of them.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,null,2,null,3,null,4,null,null]
# Output: [2,1,3,null,null,null,4]
# Explanation: This is not the only correct answer, [3,1,4,null,2,null,null] is
# also correct.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is between 1 and 10^4.
# The tree nodes will have distinct values between 1 and 10^5.
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
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # O(N)

        def dfs(node):
            return dfs(node.left) + [node.val] + dfs(node.right) if node else []

        def chain(data):
            if not data: return None
            mid = len(data) // 2
            head = TreeNode(data[mid])
            head.left = chain(data[:mid])
            head.right = chain(data[mid + 1:])
            return head

        if not root: return root
        data = dfs(root)
        return chain(data)
        
# @lc code=end

