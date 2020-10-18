#
# @lc app=leetcode id=1214 lang=python3
#
# [1214] Two Sum BSTs
#
# https://leetcode.com/problems/two-sum-bsts/description/
#
# algorithms
# Medium (65.80%)
# Likes:    104
# Dislikes: 9
# Total Accepted:    7.1K
# Total Submissions: 10.7K
# Testcase Example:  '[2,1,4]\n[1,0,3]\n5'
#
# Given two binary search trees, return True if and only if there is a node in
# the first tree and a node in the second tree whose values sum up to a given
# integer target.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
# Output: true
# Explanation: 2 and 3 sum up to 5.
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root1 = [0,-10,10], root2 = [5,1,7,0,2], target = 18
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# Each tree has at most 5000 nodes.
# -10^9 <= target, node.val <= 10^9
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
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:

        # Recursive Inorder Traversal
        # Time  complexity: O(N1 + N2)
        # Space complexity: O(2 x N1 + N2), N1 to keep the hashset and up to N1 + N2 for the recursie stacks.
        # def in_hashset(r):
        #     return in_hashset(r.left) | {target - r.val} | in_hashset(r.right) if r else set()

        # def in_check(r):
        #     return in_check(r.left) or (r.val in s) or in_check(r.right) if r else False

        # s = in_hashset(root1)
        # return in_check(root2)


        # def dfs(node):
        #     return dfs(node.left) | dfs(node.right) | {node.val} if node else set()

        # q1 = dfs(root1)
        # return any(target - a in q1 for a in dfs(root2))


        # Iterative Inorder Traversal
        # Time  complexity: O(N1 + N2)
        # Space complexity: O(N1 + max(N1, N2)), N1 to keep the hashset and up to max(N1, N2) for the stack.
        stack, s = [], set()
        # traverse the first tree 
        # and store node complements (target - val) in hashset
        while stack or root1:
            while root1:
                stack.append(root1)
                root1 = root1.left
            root1 = stack.pop()
            s.add(target - root1.val)
            root1 = root1.right

        # traverse the second tree 
        # and check if one of the values exists in hashset
        while stack or root2:
            while root2:
                stack.append(root2)
                root2 = root2.left
            root2 = stack.pop()
            if root2.val in s:
                return True
            root2 = root2.right

        return False





        
# @lc code=end

