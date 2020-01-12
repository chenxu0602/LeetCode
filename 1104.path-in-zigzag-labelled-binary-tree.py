#
# @lc app=leetcode id=1104 lang=python3
#
# [1104] Path In Zigzag Labelled Binary Tree
#
# https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/description/
#
# algorithms
# Medium (70.47%)
# Likes:    124
# Dislikes: 93
# Total Accepted:    8.7K
# Total Submissions: 12.3K
# Testcase Example:  '14'
#
# In an infinite binary tree where every node has two children, the nodes are
# labelled in row order.
# 
# In the odd numbered rows (ie., the first, third, fifth,...), the labelling is
# left to right, while in the even numbered rows (second, fourth, sixth,...),
# the labelling is right to left.
# 
# 
# 
# Given the label of a node in this tree, return the labels in the path from
# the root of the tree to the node with that label.
# 
# 
# Example 1:
# 
# 
# Input: label = 14
# Output: [1,3,4,14]
# 
# 
# Example 2:
# 
# 
# Input: label = 26
# Output: [1,2,6,10,26]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= label <= 10^6
# 
# 
#
class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:

        res = []
        while label:
            res.append(label)
            label //= 2
        res = res[::-1]
        for i in range(len(res)-2, 0, -2):
            res[i] = 2**(i+1) - 1 + 2**i - res[i]
        return res



