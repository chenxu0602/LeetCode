#
# @lc app=leetcode id=951 lang=python3
#
# [951] Flip Equivalent Binary Trees
#
# https://leetcode.com/problems/flip-equivalent-binary-trees/description/
#
# algorithms
# Medium (65.75%)
# Likes:    754
# Dislikes: 40
# Total Accepted:    56.3K
# Total Submissions: 86.1K
# Testcase Example:  '[1,2,3,4,5,6,null,null,null,7,8]\n[1,3,2,null,6,4,5,null,null,null,null,8,7]'
#
# For a binary tree T, we can define a flip operation as follows: choose any
# node, and swap the left and right child subtrees.
# 
# A binary tree X is flip equivalent to a binary tree Y if and only if we can
# make X equal to Y after some number of flip operations.
# 
# Given the roots of two binary trees root1 and root2, return true if the two
# trees are flip equivelent or false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: root1 = [1,2,3,4,5,6,null,null,null,7,8], root2 =
# [1,3,2,null,6,4,5,null,null,null,null,8,7]
# Output: true
# Explanation: We flipped at nodes with values 1, 3, and 5.
# 
# 
# Example 2:
# 
# 
# Input: root1 = [], root2 = []
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: root1 = [], root2 = [1]
# Output: false
# 
# 
# Example 4:
# 
# 
# Input: root1 = [0,null,1], root2 = []
# Output: false
# 
# 
# Example 5:
# 
# 
# Input: root1 = [0,null,1], root2 = [0,1]
# Output: true
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in each tree is in the range [0, 100].
# Each tree will have unique node values in the range [0, 99].
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
import itertools

class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        # Recursion
        # Time  complexity: O(min(N1, N2)), where N1 and N2 are the lengths of root1 and root2.
        # Space complexity: O(min(H1, H2)), where H1 and H2 are the heights of the trees of root1 and root2.
        # if root1 is root2:
        #     return True
        # if not root1 or not root2 or root1.val != root2.val:
        #     return False
        
        # return (self.flipEquiv(root1.left, root2.left) and
        #         self.flipEquiv(root1.right, root2.right) or
        #         self.flipEquiv(root1.left, root2.right) and
        #         self.flipEquiv(root1.right, root2.left))


        # Canonical Traversal (DFS)
        # Time  complexity: O(min(N1, N2))
        # Space complexity: O(min(H1, H2))
        def dfs(node):
            if node:
                yield node.val
                L = node.left.val if node.left else -1
                R = node.right.val if node.right else -1
                if L < R:
                    yield from dfs(node.left)
                    yield from dfs(node.right)
                else:
                    yield from dfs(node.right)
                    yield from dfs(node.left)
                yield '#'

        print(list(dfs(root1)))
        print(list(dfs(root2)))

        return all(x == y for x, y in itertools.zip_longest(
            dfs(root1), dfs(root2)))
        
# @lc code=end

