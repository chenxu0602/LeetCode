#
# @lc app=leetcode id=1490 lang=python3
#
# [1490] Clone N-ary Tree
#
# https://leetcode.com/problems/clone-n-ary-tree/description/
#
# algorithms
# Medium (83.63%)
# Likes:    98
# Dislikes: 5
# Total Accepted:    5.8K
# Total Submissions: 6.9K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# Given a root of an N-ary tree, return a deep copy (clone) of the tree.
# 
# Each node in the n-ary tree contains a val (int) and a list (List[Node]) of
# its children.
# 
# 
# class Node {
# ⁠   public int val;
# ⁠   public List<Node> children;
# }
# 
# 
# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See examples).
# 
# Follow up: Can your solution work for the graph problem?
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: root = [1,null,3,2,4,null,5,6]
# Output: [1,null,3,2,4,null,5,6]
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: root =
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
# Output:
# [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
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
    def cloneTree(self, root: 'Node') -> 'Node':
        # O(n)

        # if not root: return None

        # node = Node(root.val)

        # if root.children:
        #     for child in root.children:
        #         node.children.append(self.cloneTree(child))

        # return node


        return Node(root.val, [self.cloneTree(child) for child in root.children]) if root else None
# @lc code=end

