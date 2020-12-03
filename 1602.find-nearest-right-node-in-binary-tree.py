#
# @lc app=leetcode id=1602 lang=python3
#
# [1602] Find Nearest Right Node in Binary Tree
#
# https://leetcode.com/problems/find-nearest-right-node-in-binary-tree/description/
#
# algorithms
# Medium (74.53%)
# Likes:    47
# Dislikes: 1
# Total Accepted:    2.4K
# Total Submissions: 3.2K
# Testcase Example:  '[1,2,3,null,4,5,6]\n4'
#
# Given the root of a binary tree and a node u in the tree, return the nearest
# node on the same level that is to the right of u, or return null if u is the
# rightmost node in its level.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,2,3,null,4,5,6], u = 4
# Output: 5
# Explanation: The nearest node on the same level to the right of node 4 is
# node 5.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root = [3,null,4,2], u = 2
# Output: null
# Explanation: There are no nodes to the right of 2.
# 
# 
# Example 3:
# 
# 
# Input: root = [1], u = 1
# Output: null
# 
# 
# Example 4:
# 
# 
# Input: root = [3,4,2,null,null,null,1], u = 4
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 10^5].
# 1 <= Node.val <= 10^5
# All values in the tree are distinct.
# u is a node in the binary tree rooted at root.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> TreeNode:
        # BFS: Two Queues
        # One for the current level, and one for the next.
        # Time  complexity: O(N)
        # Space complexity: O(D), where D is a tree diameter.
        if root is None:
            return []

        next_level = deque([root,])
        while next_level:
            curr_level = next_level
            next_level = deque()

            while curr_level:
                node = curr_level.popleft()
                if node == u:
                    return curr_level.popleft() if curr_level else None

                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)


        # BFS: One Queue + Sentinel
        # Time  complexity: O(N)
        # Space complexity: O(D), where D is a tree diameter.
        # if root is None:
        #     return None

        # queue = deque([root, None,])
        # while queue:
        #     curr = queue.popleft()

        #     if curr == u:
        #         return queue.popleft()

        #     if curr:
        #         if curr.left:
        #             queue.append(curr.left)
        #         if curr.right:
        #             queue.append(curr.right)
        #     else:
        #         # once the level is finished,
        #         # add a sentinel to mark end of level
        #         if queue:
        #             queue.append(None)


        # BFS: One Queue + Level Size Measurements
        # Time  complexity: O(N)
        # Space complexity: O(D), where D is a tree diameter.
        # if root is None:
        #     return None

        # queue = deque([root,])
        # while queue:
        #     level_length = len(queue)

        #     for i in range(level_length):
        #         node = queue.popleft()
        #         if node == u:
        #             return queue.popleft() if i != level_length - 1 else None

        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)


        # Recursive DFS: Preorder Traversal
        # Time  complexity: O(N)
        # Space complexity: O(H) to keep the recursion stack, where H is a tree height. The worst-case situation is a skewed tree when H = N.
        # def preorder(node, depth):
        #     nonlocal u_depth, next_node
        #     # the depth to look for next node is identified
        #     if node == u:
        #         u_depth = depth
        #     # we're on the level to look for the next node
        #     elif depth == u_depth:
        #         # if this next node is not identified yet
        #         if next_node is None:
        #             next_node = node
        #     # continue to traverse the tree
        #     else:
        #         for child in [node.left, node.right]:
        #             if child:
        #                 preorder(child, depth + 1)

        # u_depth, next_node = -1, None
        # preorder(root, 0)
        # return next_node



        # queue = [root,]
        # while queue:
        #     queue2 = []
        #     for i in range(len(queue)):
        #         node = queue[i]
        #         if node.val == u.val:
        #             if i == len(queue) - 1:
        #                 return None
        #             return queue[i + 1]
                
        #         if node.left:
        #             queue2.append(node.left)
        #         if node.right:
        #             queue2.append(node.right)

        #     queue = queue2
        
# @lc code=end

