#
# @lc app=leetcode id=1597 lang=python3
#
# [1597] Build Binary Expression Tree From Infix Expression
#
# https://leetcode.com/problems/build-binary-expression-tree-from-infix-expression/description/
#
# algorithms
# Hard (65.64%)
# Likes:    32
# Dislikes: 13
# Total Accepted:    804
# Total Submissions: 1.2K
# Testcase Example:  '"2-3/(5*2)+1"'
#
# A binary expression tree is a kind of binary tree used to represent
# arithmetic expressions. Each node of a binary expression tree has either zero
# or two children. Leaf nodes (nodes with 0 children) correspond to operands
# (numbers), and internal nodes (nodes with 2 children) correspond to the
# operators '+' (addition), '-' (subtraction), '*' (multiplication), and '/'
# (division).
# 
# For each internal node with operator o, the infix expression that it
# represents is (A o B), where A is the expression the left subtree represents
# and B is the expression the right subtree represents.
# 
# You are given a string s, an infix expression containing operands, the
# operators described above, and parentheses '(' and ')'.
# 
# Return any valid binary expression tree, which its in-order traversal
# reproduces s after omitting the parenthesis from it (see examples below).
# 
# Please note that order of operations applies in s. That is, expressions in
# parentheses are evaluated first, and multiplication and division happen
# before addition and subtraction.
# 
# Operands must also appear in the same order in both s and the in-order
# traversal of the tree.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: s = "2-3/(5*2)+1"
# Output: [+,-,1,2,/,null,null,null,null,3,*,null,null,5,2]
# Explanation: The inorder traversal of the tree above is 2-3/5*2+1 which is
# the same as s without the parenthesis. The tree also produces the correct
# result and its operands are in the same order as they appear in s.
# The tree below is also a valid binary expression tree with the same inorder
# traversal as s:
# 
# The third tree below however is not valid. Although it produces the same
# result and is equivalent to the above trees, its inorder traversal doesn't
# produce s and its operands are not in the same order as s.
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: s = "3*4-2*5"
# Output: [-,*,*,3,4,2,5]
# Explanation: The tree above is the only valid tree whose inorder traversal
# produces s.
# 
# 
# Example 3:
# 
# 
# Input: s = "1+2+3+4+5"
# Output: [+,+,5,+,4,null,null,+,3,null,null,1,2]
# Explanation: The tree [+,+,5,+,+,null,null,1,2,3,4] is also one of many other
# valid trees.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of digits and the characters '+', '-', '*', '/', '(', and ')'.
# Operands in s are exactly 1 digit.
# It is guaranteed that s is a valid expression.
# 
# 
#

# @lc code=start
# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    # Standard parser implementation based on this BNF
    #   s := expression
    #   expression := term | term { [+,-] term] }
    #   term := factor | factor { [*,/] factor] }
    #   factor :== digit | '(' expression ')'
    #   digit := [0..9]
    def expTree(self, s: str) -> 'Node':
        tokens = deque(list(s))
        return self.parse_expression(tokens)

    def parse_expression(self, tokens):
        lhs = self.parse_term(tokens)
        while len(tokens) > 0 and tokens[0] in ('+', '-'):
            op = tokens.popleft()
            rhs = self.parse_term(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
        return lhs

    def parse_term(self, tokens):
        lhs = self.parse_factor(tokens)
        while len(tokens) > 0 and tokens[0] in ('*', '/'):
            op = tokens.popleft()
            rhs = self.parse_factor(tokens)
            lhs = Node(val=op, left=lhs, right=rhs)
        return lhs

    def parse_factor(self, tokens):
        if tokens[0] == '(':
            tokens.popleft()
            node = self.parse_expression(tokens)
            tokens.popleft()
            return node
        else:
            token = tokens.popleft()
            return Node(val=token)

        
# @lc code=end

