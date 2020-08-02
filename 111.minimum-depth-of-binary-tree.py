#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
#
# algorithms
# Easy (36.51%)
# Likes:    1015
# Dislikes: 584
# Total Accepted:    363.3K
# Total Submissions: 994.7K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, find its minimum depth.
# 
# The minimum depth is the number of nodes along the shortest path from the
# root node down to the nearest leaf node.
# 
# Note: A leaf is a node with no children.
# 
# Example:
# 
# Given binary tree [3,9,20,null,null,15,7],
# 
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# return its minimum depth = 2.
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
    def minDepth(self, root: TreeNode) -> int:

        # Recursion
        # Time  complexity: O(N)
        # Space complexity: O(logN)
        # if not root:
        #     return 0

        # children = [root.left, root.right]
        # if not any(children):
        #     return 1

        # min_depth = float("inf")
        # for c in children:
        #     if c:
        #         min_depth = min(self.minDepth(c), min_depth)
        
        # return min_depth + 1
        

        # DFS Iteration
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # if not root:
        #     return 0
        # else:
        #     stack, min_depth = [(1, root),], float("inf")

        # while stack:
        #     depth, root = stack.pop()
        #     children = [root.left, root.right]
        #     if not any(children):
        #         min_depth = min(depth, min_depth)
        #     for c in children:
        #         if c:
        #             stack.append((depth + 1, c))

        # return min_depth
        

        # BFS Iteration
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # One way to optimize the complexity is to use the BFS strategy. We iterate the tree level by level, and the first leaf we reach corresponds to the minimum depth. 
        if not root:
            return 0
        else:
            node_deque = deque([(1, root),])

        while node_deque:
            depth, root = node_deque.popleft()
            children = [root.left, root.right]
            if not any(children):
                return depth
            for c in children:
                if c:
                    node_deque.append((depth + 1, c))


# @lc code=end

