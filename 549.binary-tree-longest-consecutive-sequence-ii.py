#
# @lc app=leetcode id=549 lang=python3
#
# [549] Binary Tree Longest Consecutive Sequence II
#
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/description/
#
# algorithms
# Medium (46.05%)
# Likes:    489
# Dislikes: 31
# Total Accepted:    22K
# Total Submissions: 47.9K
# Testcase Example:  '[1,2,3,4]'
#
# Given a binary tree, you need to find the length of Longest Consecutive Path
# in Binary Tree.
# 
# Especially, this path can be either increasing or decreasing. For example,
# [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is
# not valid. On the other hand, the path can be in the child-Parent-child
# order, where not necessarily be parent-child order.
# 
# Example 1:
# 
# 
# Input:
# ⁠       1
# ⁠      / \
# ⁠     2   3
# Output: 2
# Explanation: The longest consecutive path is [1, 2] or [2, 1].
# 
# 
# 
# 
# Example 2:
# 
# 
# Input:
# ⁠       2
# ⁠      / \
# ⁠     1   3
# Output: 3
# Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
# 
# 
# 
# 
# Note: All the values of tree nodes are in the range of [-1e7, 1e7].
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
    def longestConsecutive(self, root: TreeNode) -> int:
        # Time  complexity: O(n)
        # Space complexity: O(n)
        # def get_max(node):
        #     if not node: return 0, 0, 0

        #     inc, dec = 1, 1

        #     li, ld, lt = get_max(node.left)
        #     ri, rd, rt = get_max(node.right)

        #     if node.left:
        #         if li and node.left.val - node.val == 1:
        #             inc = li + 1
        #         if ld and node.left.val - node.val == -1:
        #             dec = ld + 1

        #     if node.right:
        #         if ri and node.right.val - node.val == 1:
        #             inc = max(inc, ri + 1)
        #         if rd and node.right.val - node.val == -1:
        #             dec = max(dec, rd + 1)

        #     return inc, dec, max(inc + dec - 1, lt, rt)

        # return max(get_max(root))


        def get_max(node):
            if not node: return 0, 0

            inc, dec = 1, 1
            
            if node.left:
                li, ld = get_max(node.left)
                if node.val == node.left.val - 1:
                    inc = li + 1
                elif node.val == node.left.val + 1:
                    dec = ld + 1

            if node.right:
                ri, rd = get_max(node.right)
                if node.val == node.right.val - 1:
                    inc = max(inc, ri + 1)
                elif node.val == node.right.val + 1:
                    dec = max(dec, rd + 1)

            self.maxval = max(self.maxval, inc + dec - 1)
            return inc, dec

        self.maxval = 0
        get_max(root)
        return self.maxval
        
# @lc code=end

