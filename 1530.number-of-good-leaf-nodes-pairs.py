#
# @lc app=leetcode id=1530 lang=python3
#
# [1530] Number of Good Leaf Nodes Pairs
#
# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/description/
#
# algorithms
# Medium (55.30%)
# Likes:    517
# Dislikes: 10
# Total Accepted:    13.1K
# Total Submissions: 23.6K
# Testcase Example:  '[1,2,3,null,4]\n3'
#
# Given the root of a binary tree and an integer distance. A pair of two
# different leaf nodes of a binary tree is said to be good if the length of the
# shortest path between them is less than or equal to distance.
# 
# Return the number of good leaf node pairs in the tree.
# 
# 
# Example 1:
# 
# 
# Input: root = [1,2,3,null,4], distance = 3
# Output: 1
# Explanation: The leaf nodes of the tree are 3 and 4 and the length of the
# shortest path between them is 3. This is the only good pair.
# 
# 
# Example 2:
# 
# 
# Input: root = [1,2,3,4,5,6,7], distance = 3
# Output: 2
# Explanation: The good pairs are [4,5] and [6,7] with shortest path = 2. The
# pair [4,6] is not good because the length of ther shortest path between them
# is 4.
# 
# 
# Example 3:
# 
# 
# Input: root = [7,1,4,6,null,5,3,null,null,null,null,null,2], distance = 3
# Output: 1
# Explanation: The only good pair is [2,5].
# 
# 
# Example 4:
# 
# 
# Input: root = [100], distance = 1
# Output: 0
# 
# 
# Example 5:
# 
# 
# Input: root = [1,1,1], distance = 2
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the tree is in the range [1, 2^10].
# Each node's value is between [1, 100].
# 1 <= distance <= 10
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        def dfs(node):
            nonlocal ans
            if not node: return []
            if node.left is node.right:
                return [0]

            left, right = map(dfs, (node.left, node.right))
            ans += sum(2 + x + y <= distance for x in left for y in right)
            return [1 + x for x in left + right]

        ans = 0
        dfs(root)
        return ans
        
# @lc code=end

