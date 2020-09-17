#
# @lc app=leetcode id=865 lang=python3
#
# [865] Smallest Subtree with all the Deepest Nodes
#
# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/description/
#
# algorithms
# Medium (59.26%)
# Likes:    543
# Dislikes: 168
# Total Accepted:    29.6K
# Total Submissions: 49.9K
# Testcase Example:  '[3,5,1,6,2,0,8,null,null,7,4]'
#
# Given a binary tree rooted at root, the depth of each node is the shortest
# distance to the root.
# 
# A node is deepest if it has the largest depth possible among any node in the
# entire tree.
# 
# The subtree of a node is that node, plus the set of all descendants of that
# node.
# 
# Return the node with the largest depth such that it contains all the deepest
# nodes in its subtree.
# 
# 
# 
# Example 1:
# 
# 
# Input: [3,5,1,6,2,0,8,null,null,7,4]
# Output: [2,7,4]
# Explanation:
# 
# 
# 
# We return the node with value 2, colored in yellow in the diagram.
# The nodes colored in blue are the deepest nodes of the tree.
# The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]" is a serialization of the
# given tree.
# The output "[2, 7, 4]" is a serialization of the subtree rooted at the node
# with value 2.
# Both the input and output have TreeNode type.
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the tree will be between 1 and 500.
# The values of each node are unique.
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
from collections import namedtuple

class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        # Paint Deepest Nodes
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # Tag each node with it's depth.
        # depth = {None: -1}
        # def dfs(node, parent=None):
        #     if node:
        #         depth[node] = depth[parent] + 1
        #         dfs(node.left, node)
        #         dfs(node.right, node)

        # dfs(root)

        # max_depth = max(depth.values())

        # def answer(node):
        #     # Return the answer for the subtree at node.
        #     if not node or depth.get(node, None) == max_depth:
        #         return node
        #     L, R = map(answer, (node.left, node.right))
        #     return node if L and R else L or R

        # return answer(root)


        # Recursion
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # Result = namedtuple("Result", ("node", "dist"))
        # def dfs(node):
        #     if not node: return Result(None, 0)
        #     L, R = map(dfs, (node.left, node.right))
        #     if L.dist > R.dist: return Result(L.node, L.dist + 1)
        #     if L.dist < R.dist: return Result(R.node, R.dist + 1)
        #     return Result(node, L.dist + 1)

        # return dfs(root).node


        # Time  complexity: O(N)
        # Space complexity: O(H)
        # def deepestDepth(node, depth=0):
        #     if not node:
        #         return node, depth

        #     left, leftDepth = deepestDepth(node.left, depth + 1)
        #     right, rightDepth = deepestDepth(node.right, depth + 1)

        #     if leftDepth > rightDepth:
        #         return left, leftDepth

        #     if rightDepth > leftDepth:
        #         return right, rightDepth

        #     return node, leftDepth

        # return deepestDepth(root)[0]


        # Same as LeetCode 1123
        # Time  complexity: O(N)
        # Space complexity: O(H)
        def dfs(node):
            if not node: return 0, None
            h1, lca1 = dfs(node.left)
            h2, lca2 = dfs(node.right)

            if h1 > h2:
                return h1 + 1, lca1
            elif h1 < h2:
                return h2 + 1, lca2
            else:
                return h1 + 1, node

        return dfs(root)[1]


        
# @lc code=end

