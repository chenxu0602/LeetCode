#
# @lc app=leetcode id=1008 lang=python3
#
# [1008] Construct Binary Search Tree from Preorder Traversal
#
# https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/description/
#
# algorithms
# Medium (74.99%)
# Likes:    535
# Dislikes: 20
# Total Accepted:    36.2K
# Total Submissions: 48.2K
# Testcase Example:  '[8,5,1,7,10,12]'
#
# Return the root node of a binary search tree that matches the given preorder
# traversal.
# 
# (Recall that a binary search tree is a binary tree where for every node, any
# descendant of node.left has a value < node.val, and any descendant of
# node.right has a value > node.val.  Also recall that a preorder traversal
# displays the value of the node first, then traverses node.left, then
# traverses node.right.)
# 
# 
# 
# Example 1:
# 
# 
# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
# 
# 
# 
# 
# 
# Note: 
# 
# 
# 1 <= preorder.length <= 100
# The values of preorder are distinct.
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

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        # Construct binary tree from preorder and inorder traversal
        # Time  complexity: O(NlogN). O(NlogN) to sort preorder array and O(N) to construct the binary tree.
        # Space complexity: O(N) the inorder traversal and the tree.
        # def helper(in_left=0, in_right=len(preorder)):
        #     nonlocal pre_idx
        #     if in_left == in_right:
        #         return None

        #     # pick up pre_idx element as a root
        #     root_val = preorder[pre_idx]
        #     root = TreeNode(root_val)

        #     # root splits inorder list
        #     # into left and right subtrees
        #     index = idx_map[root_val]

        #     # recursion
        #     pre_idx += 1
        #     root.left = helper(in_left, index)
        #     root.right = helper(index + 1, in_right)
        #     return root

        # inorder = sorted(preorder)
        # # start from first preorder element
        # pre_idx = 0
        # # build a hashmap value -> its index
        # idx_map = {val: idx for idx, val in enumerate(inorder)}
        # return helper()


        # Recursion
        # Time  complexity: O(N) since we visit each node exactly once.
        # Space complexity: O(N) to keep the entire tree.
        # def helper(lower=float("-inf"), upper=float("inf")):
        #     nonlocal idx
        #     # if all elements from preorder are used
        #     # then the tree is constructed
        #     if idx == n:
        #         return None

        #     val = preorder[idx]
        #     # if the current element 
        #     # couldn't be placed here to meet BST requirements
        #     if val < lower or val > upper:
        #         return None

        #     # place the current element
        #     # and recursively construct subtrees
        #     idx += 1
        #     root = TreeNode(val)
        #     root.left = helper(lower, val)
        #     root.right = helper(val, upper)
        #     return root

        # idx = 0
        # n = len(preorder)
        # return helper()


        # Iteration
        # Time  complexity: O(N) since we visit each node eactly once.
        # Space complexity: O(N) to keep the stack and the tree.
        n = len(preorder)
        if not n:
            return None

        root = TreeNode(preorder[0])
        stack = [root,]

        for i in range(1, n):
            # take the last element of the stack as a parent
            # and create a child from the next preorder element
            node, child = stack[-1], TreeNode(preorder[i])
            # adjust the parent 
            while stack and stack[-1].val < child.val:
                node = stack.pop()

            # follow BST logic to create a parent-child link
            if node.val < child.val:
                node.right = child
            else:
                node.left = child
            # add the child into stack
            stack.append(child)

        return root



        
# @lc code=end

