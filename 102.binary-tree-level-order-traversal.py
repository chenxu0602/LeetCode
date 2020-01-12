#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (49.64%)
# Likes:    1855
# Dislikes: 48
# Total Accepted:    447.8K
# Total Submissions: 886.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
# 
# 
# For example:
# Given binary tree [3,9,20,null,null,15,7],
# 
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
# 
# 
# 
# return its level order traversal as:
# 
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        """
        levels = []
        if not root:
            return levels

        def dfs(node, level):
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            if node.left:
                dfs(node.left, level+1)
            if node.right:
                dfs(node.right, level+1)

        dfs(root, 0)
        return levels
        """

        """
        levels = []
        if not root:
            return levels

        level = 0
        queue = deque([root,])
        while queue:
            levels.append([])
            level_length = len(queue)

            for i in range(level_length):
                node = queue.popleft()
                levels[level].append(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            level += 1

        return levels
        """

        """
        if not root:
            return []

        ans, queue = [], [root,]
        while queue:
            ans.append([node.val for node in queue])
            temp = []
            for node in queue:
                temp.extend([node.left, node.right])
            queue = [child for child in temp if child]
        return ans
        """

        """
        ans, queue = [], [root,]
        while root and queue:
            ans.append([node.val for node in queue])
            LRpair = [(node.left, node.right) for node in queue]
            queue = [child for LR in LRpair for child in LR if child]
        return ans
        """

        ans, queue = [], [root,]
        while root and queue:
            ans.append([node.val for node in queue])
            queue = [child for node in queue for child in (node.left, node.right) if child]
        return ans





    
        
# @lc code=end

