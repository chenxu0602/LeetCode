#
# @lc app=leetcode id=331 lang=python3
#
# [331] Verify Preorder Serialization of a Binary Tree
#
# https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/
#
# algorithms
# Medium (38.64%)
# Likes:    496
# Dislikes: 30
# Total Accepted:    58.8K
# Total Submissions: 152K
# Testcase Example:  '"9,3,4,#,#,1,#,#,2,#,6,#,#"'
#
# One way to serialize a binary tree is to use pre-order traversal. When we
# encounter a non-null node, we record the node's value. If it is a null node,
# we record using a sentinel value such as #.
# 
# 
# ⁠    _9_
# ⁠   /   \
# ⁠  3     2
# ⁠ / \   / \
# ⁠4   1  #  6
# / \ / \   / \
# # # # #   # #
# 
# 
# For example, the above binary tree can be serialized to the string
# "9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.
# 
# Given a string of comma separated values, verify whether it is a correct
# preorder traversal serialization of a binary tree. Find an algorithm without
# reconstructing the tree.
# 
# Each comma separated value in the string must be either an integer or a
# character '#' representing null pointer.
# 
# You may assume that the input format is always valid, for example it could
# never contain two consecutive commas such as "1,,3".
# 
# Example 1:
# 
# 
# Input: "9,3,4,#,#,1,#,#,2,#,6,#,#"
# Output: true
# 
# Example 2:
# 
# 
# Input: "1,#"
# Output: false
# 
# 
# Example 3:
# 
# 
# Input: "9,#,#,1"
# Output: false
#
class Solution:
    def endsWithTwoHashes(self, stack, top):
        if top < 1:
            return False
        if stack[top] == stack[top-1] == '#':
            return True
        return False

    def isValidSerialization(self, preorder: str) -> bool:
        """
        stack = []
        top = -1
        preorder = preorder.split(',')
        for s in preorder:
            stack.append(s)
            top += 1
            while self.endsWithTwoHashes(stack, top):
                h = stack.pop()
                top -= 1
                h = stack.pop()
                top -= 1
                if top < 0:
                    return False
                h = stack.pop()
                stack.append('#')

        if len(stack) == 1 and stack[0] == '#':
            return True

        return False
        """

        slots = 1
        for node in preorder.split(','):
            slots -= 1

            if slots < 0:
                return False

            if node != '#':
                slots += 2

        return slots == 0



        

