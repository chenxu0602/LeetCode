#
# @lc app=leetcode id=426 lang=python3
#
# [426] Convert Binary Search Tree to Sorted Doubly Linked List
#
# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/
#
# algorithms
# Medium (52.51%)
# Likes:    423
# Dislikes: 50
# Total Accepted:    31K
# Total Submissions: 59K
# Testcase Example:  '{"$id":"1","val":4,"left":{"$id":"2","val":2,"left":{"$id":"4","val":1,"left":null,"right":null},"right":{"$id":"5","val":3,"left":null,"right":null}},"right":{"$id":"3","val":5,"left":null,"right":null}}'
#
# Convert a BST to a sorted circular doubly-linked list in-place. Think of the
# left and right pointers as synonymous to the previous and next pointers in a
# doubly-linked list.
# 
# Let's take the following BST as an example, it may help you understand the
# problem better:
# 
# 
# 
# 
# 
# We want to transform this BST into a circular doubly linked list. Each node
# in a doubly linked list has a predecessor and successor. For a circular
# doubly linked list, the predecessor of the first element is the last element,
# and the successor of the last element is the first element.
# 
# The figure below shows the circular doubly linked list for the BST above. The
# "head" symbol means the node it points to is the smallest element of the
# linked list.
# 
# 
# 
# 
# 
# Specifically, we want to do the transformation in place. After the
# transformation, the left pointer of the tree node should point to its
# predecessor, and the right pointer should point to its successor. We should
# return the pointer to the first element of the linked list.
# 
# The figure below shows the transformed BST. The solid line indicates the
# successor relationship, while the dashed line means the predecessor
# relationship.
# 
# 
# 
# 
#
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':

        # if not root: return
        # dummy = prev = Node(0, None, None)
        # stack, node = [], root
        # while stack or node:
        #     while node:
        #         stack.append(node)
        #         node = node.left
        #     node = stack.pop()
        #     node.left, prev.right, prev = prev, node, node
        #     node = node.right

        # dummy.right.left, prev.right = prev, dummy.right
        # return dummy.right
                
        def dfs(node):
            nonlocal first, last

            if node:
                dfs(node.left)

                if last:
                    last.right = node
                    node.left = last
                else:
                    first = node

                last = node

                dfs(node.right)

        if not root: return None

        last, first = None, None
        dfs(root)

        last.right = first
        first.left = last

        return first



