#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (50.51%)
# Likes:    1352
# Dislikes: 45
# Total Accepted:    429.3K
# Total Submissions: 842.5K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given two binary trees, write a function to check if they are the same or
# not.
# 
# Two binary trees are considered the same if they are structurally identical
# and the nodes have the same value.
# 
# Example 1:
# 
# 
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:     1         1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# Output: false
# 
# 
# Example 3:
# 
# 
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# Output: false
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

from collections import deque

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        # def check(p, q):
        #     if not p and not q:
        #         return True
        #     if not q or not p:
        #         return False
        #     if p.val != q.val:
        #         return False
        #     return True

        # deq = deque([(p, q),])
        # while deq:
        #     p, q = deq.popleft()
        #     if not check(p, q):
        #         return False

        #     if p:
        #         deq.append((p.left, q.left))
        #         deq.append((p.right, q.right))

        # return True

        return p and q and p.val == q.val and \
            all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q

        
# @lc code=end

