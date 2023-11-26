#
# @lc app=leetcode id=1650 lang=python3
#
# [1650] Lowest Common Ancestor of a Binary Tree III
#
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/description/
#
# algorithms
# Medium (78.63%)
# Likes:    28
# Dislikes: 3
# Total Accepted:    1.8K
# Total Submissions: 2.4K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n1'
#
# Given two nodes of a binary tree p and q, return their lowest common ancestor
# (LCA).
# 
# Each node will have a reference to its parent node. The definition for Node
# is below:
# 
# 
# class Node {
# ⁠   public int val;
# ⁠   public Node left;
# ⁠   public Node right;
# ⁠   public Node parent;
# }
# 
# 
# According to the definition of LCA on Wikipedia: "The lowest common ancestor
# of two nodes p and q in a tree T is the lowest node that has both p and q as
# descendants (where we allow a node to be a descendant of itself)."
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
# 
# 
# Example 2:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5 since a node can be a descendant
# of itself according to the LCA definition.
# 
# 
# Example 3:
# 
# 
# Input: root = [1,2], p = 1, q = 2
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [2, 10^5].
# -10^9 <= Node.val <= 10^9
# All Node.val are unique.
# p != q
# p and q exist in the tree.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # the concept of two runners on the circle track
        """
        p1, p2 = p, q
        while p1 != p2:
            p1 = p1.parent if p1.parent else q
            p2 = p2.parent if p2.parent else p
        return p1
        """

        path = set()
        while p:
            path.add(p)
            p = p.parent
        while q not in path:
            q = q.parent
        return q



        
# @lc code=end

