#
# @lc app=leetcode id=426 lang=python3
#
# [426] Convert Binary Search Tree to Sorted Doubly Linked List
#
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/
#
# algorithms
# Medium (56.56%)
# Likes:    697
# Dislikes: 76
# Total Accepted:    56.7K
# Total Submissions: 100.1K
# Testcase Example:  '[4,2,5,1,3]\r'
#
# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in
# place.
# 
# You can think of the left and right pointers as synonymous to the predecessor
# and successor pointers in a doubly-linked list. For a circular doubly linked
# list, the predecessor of the first element is the last element, and the
# successor of the last element is the first element.
# 
# We want to do the transformation in place. After the transformation, the left
# pointer of the tree node should point to its predecessor, and the right
# pointer should point to its successor. You should return the pointer to the
# smallest element of the linked list.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [4,2,5,1,3]
# 
# 
# Output: [1,2,3,4,5]
# 
# Explanation: The figure below shows the transformed BST. The solid line
# indicates the successor relationship, while the dashed line means the
# predecessor relationship.
# 
# 
# 
# Example 2:
# 
# 
# Input: root = [2,1,3]
# Output: [1,2,3]
# 
# 
# Example 3:
# 
# 
# Input: root = []
# Output: []
# Explanation: Input is an empty tree. Output is also an empty Linked List.
# 
# 
# Example 4:
# 
# 
# Input: root = [1]
# Output: [1]
# 
# 
# 
# Constraints:
# 
# 
# -1000 <= Node.val <= 1000
# Node.left.val < Node.val < Node.right.val
# All values of Node.val are unique.
# 0 <= Number of Nodes <= 2000
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # # Inorder Recursion
        # # Time  complexity: O(N)
        # # Space complexity: O(N). 
        # # We have to keep a recursion stack of the size of the tree height, 
        # # which is O(logN) for the best case of completely balanced tree and
        # # and O(N) for the worst case of completely unbalanced tree.
        # def helper(node):
        #     """
        #     Performs standard inorder traversal:
        #     left -> node -> right
        #     and links all nodes into DLL
        #     """
        #     nonlocal last, first
        #     if node:
        #         # left
        #         helper(node.left)
        #         if last:
        #             # link the previous node (last)
        #             # with the current one (node)
        #             last.right = node
        #             node.left = last
        #         else:
        #             # keep the smallest node
        #             # to close DLL later on
        #             first = node
        #         last = node
        #         # right
        #         helper(node.right)

        # if not root:
        #     return None

        # # the smallest (first) and the largest (last) nodes
        # first, last = None, None
        # helper(root)
        # # close DLL
        # last.right = first
        # first.left = last
        # return first


        # Iteration
        # O(N) / O(1)
        if not root: return
        dummy = prev = Node(0, None, None)
        stack, node = [], root

        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            node = node.right

        dummy.right.left, prev.right = prev, dummy.right
        return dummy.right



        
        
# @lc code=end

