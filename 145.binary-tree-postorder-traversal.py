#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (52.26%)
# Likes:    1367
# Dislikes: 69
# Total Accepted:    330K
# Total Submissions: 630.8K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
# 
# Example:
# 
# 
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
# 
# Output: [3,2,1]
# 
# 
# Follow up: Recursive solution is trivial, could you do it iteratively?
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
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        # Recursive Postorder Traversal
        # Time  complexity: O(N)
        # Space complexity: O(H)
        # return self.postorderTraversal(root.left) + self.postorderTraversal(root.right) + [root.val] if root else []

        # Iterative Preorder Traversal
        # Time  complexity: O(N)
        # Space complexity: O(H)
        # if root is None:
        #     return []

        # stack, output = [root,], []
        # while stack:
        #     root = stack.pop()
        #     output.append(root.val)
        #     if root.left:
        #         stack.append(root.left)
        #     if root.right:
        #         stack.append(root.right)

        # return output[::-1]


        # output, stack = [], [(root, False)]
        # while stack:
        #     node, visited = stack.pop()
        #     if node:
        #         if visited:
        #             output.append(node.val)
        #         else:
        #             stack.append((node, True))
        #             stack.append((node.right, False))
        #             stack.append((node.left, False))

        # return output



        stack, output = [], []
        while root or stack:
            # push nodes: right -> node -> left 
            while root:
                if root.right:
                    stack.append(root.right)
                stack.append(root)
                root = root.left

            root = stack.pop()

            # if the right subtree is not yet processed
            if stack and root.right == stack[-1]:
                stack[-1] = root
                root = root.right
            # if we're on the leftmost leaf
            else:
                output.append(root.val)
                root = None

        return output
# @lc code=end

