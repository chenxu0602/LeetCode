#
# @lc app=leetcode id=968 lang=python3
#
# [968] Binary Tree Cameras
#
# https://leetcode.com/problems/binary-tree-cameras/description/
#
# algorithms
# Hard (36.63%)
# Likes:    512
# Dislikes: 12
# Total Accepted:    14.3K
# Total Submissions: 39.1K
# Testcase Example:  '[0,0,null,0,0]'
#
# Given a binary tree, we install cameras on the nodes of the tree. 
# 
# Each camera at a node can monitor its parent, itself, and its immediate
# children.
# 
# Calculate the minimum number of cameras needed to monitor all nodes of the
# tree.
# 
# 
# 
# Example 1:
# 
# 
# 
# Input: [0,0,null,0,0]
# Output: 1
# Explanation: One camera is enough to monitor all nodes if placed as shown.
# 
# 
# 
# Example 2:
# 
# 
# Input: [0,0,null,0,null,0,null,null,0]
# Output: 2
# Explanation: At least two cameras are needed to monitor all nodes of the
# tree. The above image shows one of the valid configurations of camera
# placement.
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the given tree will be in the range [1, 1000].
# Every node has value 0.
# 
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

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # Dynamic Programming
        # [State 0] Strict subtree: All the nodes below this node are covered, but not this node.
        # [State 1] Normal subtree: All the nodes below and including this node are covered, but there is no camera here.
        # [State 2] Placed camera: All the nodes below and including this node are covered, and there is a camera here (which may cover nodes above this node).
        # To cover a strict subtree, the children of this node must be in state 1.
        # To cover a normal subtree without placing a camera here, the children of this node must be in states 1 or 2, and at least one of those children must be in state 2.
        # To cover the subtree when placing a camera here, the children can be in any state.
        # Time  complexity: O(N)
        # Space complexity: O(H)
        # def solve(node):
        #     if not node: return 0, 0, float("inf")
        #     L, R = map(solve, (node.left, node.right))

        #     dp0 = L[1] + R[1]
        #     dp1 = min(L[2] + min(R[1:]), R[2] + min(L[1:]))
        #     dp2 = 1 + min(L) + min(R)

        #     return dp0, dp1, dp2

        # return min(solve(root)[1:])
        

        # Greedy
        # If a node has its children covered and has a parent, then it is strictly better to place the camera at this node's parent.
        # If a node has children that are not covered by a camera, then we must place a camera here.
        # Additionally, if a node has no parent and it is not covered, we must place a camera here.
        # Time  complexity: O(N)
        # Space complexity: O(H)
        self.ans = 0
        covered = {None}

        def dfs(node, par=None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if par is None and node not in covered or node.left not in covered or node.right not in covered:
                    self.ans += 1
                    covered.update({node, par, node.left, node.right})

        dfs(root)
        return self.ans
                


# @lc code=end

