#
# @lc app=leetcode id=1522 lang=python3
#
# [1522] Diameter of N-Ary Tree
#
# https://leetcode.com/problems/diameter-of-n-ary-tree/description/
#
# algorithms
# Medium (72.25%)
# Likes:    22
# Dislikes: 0
# Total Accepted:    645
# Total Submissions: 892
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# Given a root of an N-ary tree, you need to compute the length of the diameter
# of the tree.
# 
# The diameter of an N-ary tree is the length of the longest path between any
# two nodes in the tree. This path may or may not pass through the root.
# 
# (Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value.)
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,null,3,2,4,null,5,6]
# Output: 3
# Explanation: Diameter is shown in red color.
# 
# Example 2:
# 
# 
# 
# 
# Input: root = [1,null,2,null,3,4,null,5,null,6]
# Output: 4
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output: 7
# 
# 
# 
# Constraints:
# 
# 
# The depth of the n-ary tree is less than or equal to 1000.
# The total number of nodes is between [0, 10^4].
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        # Distance with Height
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # def height(node):
        #     nonlocal diameter

        #     if len(node.children) == 0:
        #         return 0

        #     # select the top two heights
        #     max_height_1, max_height_2 = 0, 0
        #     for child in node.children:
        #         parent_height = height(child) + 1
        #         if parent_height > max_height_1:
        #             max_height_1, max_height_2 = parent_height, max_height_1
        #         elif parent_height > max_height_2:
        #             max_height_2 = parent_height

        #     # calculate the distance between the two farthest leaves nodes.
        #     distance = max_height_1 + max_height_2
        #     diameter = max(diameter, distance)

        #     return max_height_1

        # diameter = 0
        # height(root)
        # return diameter


        # Distance with Depth
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # def maxDepth(node, curr_depth):
        #     nonlocal diameter

        #     if len(node.children) == 0:
        #         return curr_depth

        #     # select the top 2 depths from its children
        #     max_depth_1, max_depth_2 = curr_depth, 0
        #     for child in node.children:
        #         depth = maxDepth(child, curr_depth + 1)
        #         if depth > max_depth_1:
        #             max_depth_1, max_depth_2 = depth, max_depth_1
        #         elif depth > max_depth_2:
        #             max_depth_2 = depth

        #     # calculate the distance between the two farthest leaves nodes
        #     distance = max_depth_1 + max_depth_2 - 2 * curr_depth
        #     diameter = max(diameter, distance)

        #     return max_depth_1


        # diameter = 0
        # maxDepth(root, 0)
        # return diameter



        def dfs(node):
            depths = [0, 0]
            for nei in node.children:
                depths.append(dfs(nei))
            depths.sort()
            self.ans = max(self.ans, depths[-1] + depths[-2])
            return depths[-1] + 1

        self.ans = 0
        dfs(root)
        return self.ans


# @lc code=end

