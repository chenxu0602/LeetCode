#
# @lc app=leetcode id=117 lang=python3
#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (37.01%)
# Likes:    1258
# Dislikes: 167
# Total Accepted:    224K
# Total Submissions: 605.1K
# Testcase Example:  '[1,2,3,4,5,null,7]'
#
# Given a binary tree
# 
# 
# struct Node {
# ⁠ int val;
# ⁠ Node *left;
# ⁠ Node *right;
# ⁠ Node *next;
# }
# 
# 
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
# 
# Initially, all next pointers are set to NULL.
# 
# 
# 
# Follow up:
# 
# 
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not
# count as extra space for this problem.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,2,3,4,5,null,7]
# Output: [1,#,2,3,#,4,5,7,#]
# Explanation: Given the above binary tree (Figure A), your function should
# populate each next pointer to point to its next right node, just like in
# Figure B. The serialized output is in level order as connected by the next
# pointers, with '#' signifying the end of each level.
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the given tree is less than 6000.
# -100 <= node.val <= 100
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        # O(N)
        # if not root: return root

        # queue = deque([root,])

        # while queue:
        #     size = len(queue)
        #     for i in range(size):
        #         node = queue.popleft()
        #         if i < size - 1:
        #             node.next = queue[0]

        #         if node.left:
        #             queue.append(node.left)

        #         if node.right:
        #             queue.append(node.right)

        # return root

        # O(N) / O(1)
        def processChild(childNode, prev, leftmost):
            if childNode:
                if prev:
                    prev.next = childNode
                else:
                    leftmost = childNode

                prev = childNode

            return prev, leftmost


        if not root:
            return root

        leftmost = root
        while leftmost:
            # "prev" tracks the latest node on the "next" level
            # while "curr" tracks the latest node on the current level.
            prev, curr = None, leftmost 

            leftmost = None

            while curr:
                prev, leftmost = processChild(curr.left, prev, leftmost)
                prev, leftmost = processChild(curr.right, prev, leftmost)
                curr = curr.next

        return root

        
# @lc code=end

