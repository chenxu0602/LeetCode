#
# @lc app=leetcode id=1022 lang=python3
#
# [1022] Sum of Root To Leaf Binary Numbers
#
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/
#
# algorithms
# Easy (58.74%)
# Likes:    181
# Dislikes: 61
# Total Accepted:    20K
# Total Submissions: 32.8K
# Testcase Example:  '[1,0,1,0,1,0,1]'
#
# Given a binary tree, each node has value 0 or 1.  Each root-to-leaf path
# represents a binary number starting with the most significant bit.  For
# example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent
# 01101 in binary, which is 13.
# 
# For all leaves in the tree, consider the numbers represented by the path from
# the root to that leaf.
# 
# Return the sum of these numbers.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: [1,0,1,0,1,0,1]
# Output: 22
# Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree is between 1 and 1000.
# node.val is 0 or 1.
# The answer will not exceed 2^31 - 1.
# 
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        # Time  complexity: O(N)
        # Space complexity: O(H)
        
        # def dfs(node, path=None):
        #     if path is None:
        #         path = ""
        #     if node:
        #         path += str(node.val)
        #         if node.left or node.right:
        #             return dfs(node.left, path) + dfs(node.right, path)
        #         else:
        #             return int(path, 2)
        #     else:
        #         return 0
        # return dfs(root)

        # def dfs(node, val=0):
        #     if not node: return 0
        #     val = val * 2 + node.val
        #     if node.left == node.right:
        #         return val
        #     return dfs(node.left, val) + dfs(node.right, val)
        # return dfs(root)


        # root_to_leaf = 0
        # stack = [(root, 0)]

        # while stack:
        #     root, curr_number = stack.pop()
        #     if root is not None:
        #         curr_number = (curr_number << 1) | root.val
        #         if root.left is None and root.right is None:
        #             root_to_leaf += curr_number
        #         else:
        #             stack.append((root.right, curr_number))
        #             stack.append((root.left, curr_number))

        # return root_to_leaf


        # def preorder(r, curr_number):
        #     nonlocal root_to_leaf
        #     if r:
        #         curr_number = (curr_number << 1) | r.val
        #         if not (r.left or r.right):
        #             root_to_leaf += curr_number

        #         preorder(r.left, curr_number)
        #         preorder(r.right, curr_number)

        # root_to_leaf = 0
        # preorder(root, 0)
        # return root_to_leaf


        # Morris Preorder Traversal
        # Time  complexity: O(N)
        # Space complexity: O(1)
        root_to_leaf = curr_number = 0

        while root:
            # If there is a left child,
            # then compute the predecessor.
            # If there is no link predecessor.right = root --> set it.
            # If there is a link predecessor.right = root --> break it.
            if root.left:
                # Predecessor node is one step to the left 
                # and then to the right till you can.
                predecessor = root.left
                steps = 1
                while predecessor.right and predecessor.right is not root:
                    predecessor = predecessor.right
                    steps += 1

                # Set link predecessor.right = root
                # and go to explore the left subtree
                if predecessor.right is None:
                    curr_number = (curr_number << 1) | root.val

                    predecessor.right = root
                    root = root.left
                # Break the link predecessor.right = root
                # Once the link is broken, 
                # it's time to change subtree and go to the right
                else:
                    # If you're on the leaf, update the sum
                    if predecessor.left is None:
                        root_to_leaf += curr_number
                    # This part of tree is explored, backtrack
                    for _ in range(steps):
                        curr_number >>= 1
                    predecessor.right = None
                    root = root.right

            # If there is no left child
            # then just go right.       
            else:
                curr_number = (curr_number << 1) | root.val
                # if you're on the leaf, update the sum
                if root.right is None:
                    root_to_leaf += curr_number
                root = root.right

        return root_to_leaf
                


