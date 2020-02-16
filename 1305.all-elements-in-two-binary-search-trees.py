#
# @lc app=leetcode id=1305 lang=python3
#
# [1305] All Elements in Two Binary Search Trees
#
# https://leetcode.com/problems/all-elements-in-two-binary-search-trees/description/
#
# algorithms
# Medium (74.82%)
# Likes:    166
# Dislikes: 5
# Total Accepted:    13.5K
# Total Submissions: 18.1K
# Testcase Example:  '[2,1,4]\r\n[1,0,3]\r'
#
# Given two binary search trees root1 and root2.
# 
# Return a list containing all the integers from both trees sorted in ascending
# order.
# 
# 
# Example 1:
# 
# 
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]
# 
# 
# Example 2:
# 
# 
# Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
# Output: [-10,0,0,1,2,5,7,10]
# 
# 
# Example 3:
# 
# 
# Input: root1 = [], root2 = [5,1,7,0,2]
# Output: [0,1,2,5,7]
# 
# 
# Example 4:
# 
# 
# Input: root1 = [0,-10,10], root2 = []
# Output: [-10,0,10]
# 
# 
# Example 5:
# 
# 
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
# 
# 
# 
# Constraints:
# 
# 
# Each tree has at most 5000 nodes.
# Each node's value is between [-10^5, 10^5].
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
import heapq

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # def gen(node):
        #     if node:
        #         yield from gen(node.left)
        #         yield node.val
        #         yield from gen(node.right)
        # return list(heapq.merge(gen(root1), gen(root2)))

        def dfs(node):
            return dfs(node.left) + [node.val] + dfs(node.right) if node else []

        r1, r2 = dfs(root1), dfs(root2)

        results = []

        l = r = 0
        while l < len(r1) and r < len(r2):
            if r1[l] <= r2[r]:
                results.append(r1[l])
                l += 1
            else:
                results.append(r2[r])
                r += 1

        while l < len(r1):
            results.append(r1[l])
            l += 1

        while r < len(r2):
            results.append(r2[r])
            r += 1

        return results
        
# @lc code=end

