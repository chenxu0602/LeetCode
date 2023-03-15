#
# @lc app=leetcode id=2476 lang=python3
#
# [2476] Closest Nodes Queries in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import bisect

class Solution:
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        nums = inorder(root)
        n = len(nums)
        results = []

        for q in queries:
            i = bisect.bisect_left(nums, q)
            if i < n and nums[i] == q:
                results.append([q, q])
            else:
                if i == 0:
                    results.append([-1, nums[0]])
                elif i == n:
                    results.append([nums[-1], -1])
                else:
                    results.append([nums[i - 1], nums[i]])

        return results
            

# @lc code=end

