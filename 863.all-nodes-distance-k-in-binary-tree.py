#
# @lc app=leetcode id=863 lang=python3
#
# [863] All Nodes Distance K in Binary Tree
#
# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
#
# algorithms
# Medium (52.59%)
# Likes:    1415
# Dislikes: 32
# Total Accepted:    52.2K
# Total Submissions: 99.3K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]\n5\n2'
#
# We are given a binary tree (with root node root), a target node, and an
# integer value K.
# 
# Return a list of the values of all nodes that have a distance K from the
# target node.  The answer can be returned in any order.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
# 
# Output: [7,4,1]
# 
# Explanation: 
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
# 
# 
# 
# Note that the inputs "root" and "target" are actually TreeNodes.
# The descriptions of the inputs above are just serializations of these
# objects.
# 
# 
# 
# 
# Note:
# 
# 
# The given tree is non-empty.
# Each node in the tree has unique values 0 <= node.val <= 500.
# The target node is a node in the tree.
# 0 <= K <= 1000.
# 
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
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # Annotate Parent
        # Time  complexity: O(N)
        # Space complexity: O(N)
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)

        queue = deque([(target, 0)])
        seen = {target}

        while queue:
            if queue[0][1] == K:
                return [node.val for node, d in queue]

            node, d = queue.popleft()
            for nei in node.left, node.right, node.par:
                if nei and nei not in seen:
                    seen.add(nei)
                    queue.append((nei, d + 1))

        return []
        
# @lc code=end

