#
# @lc app=leetcode id=272 lang=python3
#
# [272] Closest Binary Search Tree Value II
#
# https://leetcode.com/problems/closest-binary-search-tree-value-ii/description/
#
# algorithms
# Hard (45.12%)
# Likes:    362
# Dislikes: 17
# Total Accepted:    37.5K
# Total Submissions: 83.1K
# Testcase Example:  '[4,2,5,1,3]\n3.714286\n2'
#
# Given a non-empty binary search tree and a target value, find k values in the
# BST that are closest to the target.
# 
# Note:
# 
# 
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that
# are closest to the target.
# 
# 
# Example:
# 
# 
# Input: root = [4,2,5,1,3], target = 3.714286, and k = 2
# 
# ⁠   4
# ⁠  / \
# ⁠ 2   5
# ⁠/ \
# 1   3
# 
# Output: [4,3]
# 
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime
# (where n = total nodes)?
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:

        stack, queue = [], deque([])

        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()

                if len(queue) < k:
                    queue.append(root.val)
                elif abs(queue[0] - target) > abs(root.val - target):
                    queue.popleft()
                    queue.append(root.val)
                else:
                    break

                root = root.right

        return list(queue)



                
        

