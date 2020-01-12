#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (48.98%)
# Likes:    1353
# Dislikes: 73
# Total Accepted:    201.5K
# Total Submissions: 403K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
# 
# Example:
# 
# 
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
# 
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
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
    def rightSideView(self, root: TreeNode) -> List[int]:
        """
        if not root:
            return []

        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right):]
        """

        """
        rightmost_value_at_depth = dict()
        max_depth = -1

        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()

            if node:
                max_depth = max(max_depth, depth)

                rightmost_value_at_depth.setdefault(depth, node.val)

                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]
        """

        rightmost_value_at_depth = dict()
        max_depth = -1

        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()

            if node:
                max_depth = max(max_depth, depth)

                rightmost_value_at_depth[depth] = node.val

                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))

        return [rightmost_value_at_depth[depth] for depth in range(max_depth+1)]

        
# @lc code=end

