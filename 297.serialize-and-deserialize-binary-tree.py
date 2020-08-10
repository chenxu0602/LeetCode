#
# @lc app=leetcode id=297 lang=python3
#
# [297] Serialize and Deserialize Binary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
#
# algorithms
# Hard (44.87%)
# Likes:    2372
# Dislikes: 118
# Total Accepted:    264.3K
# Total Submissions: 588.6K
# Testcase Example:  '[1,2,3,null,null,4,5]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that a binary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
# 
# Example: 
# 
# 
# You may serialize the following tree:
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠    / \
# ⁠   4   5
# 
# as "[1,2,3,null,null,4,5]"
# 
# 
# Clarification: The above format is the same as how LeetCode serializes a
# binary tree. You do not necessarily need to follow this format, so please be
# creative and come up with different approaches yourself.
# 
# Note: Do not use class member/global/static variables to store states. Your
# serialize and deserialize algorithms should be stateless.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Codec:

    # O(N) / O(N)

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # if not root:
        #     return ""
        
        # queue = deque([root,])
        # res = []
        # while queue:
        #     node = queue.popleft()
        #     if node:
        #         queue.append(node.left)
        #         queue.append(node.right)
        #     res.append(str(node.val) if node else '#')

        # return ','.join(res)



        self.s = []

        def dfs(node):
            if not node:
                self.s.append('#')
            else:
                self.s.append(str(node.val))
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return ','.join(self.s)


    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # if not data:
        #     return None

        # vals = iter(data.split(','))
        # root = TreeNode(next(vals))
        # queue = deque([root,])

        # while queue:
        #     node = queue.popleft()
        #     val = next(vals)
        #     if val != '#':
        #         node.left = TreeNode(int(val))
        #         queue.append(node.left)

        #     val = next(vals)
        #     if val != '#':
        #         node.right = TreeNode(int(val))
        #         queue.append(node.right)

        # return root



        def dfs():
            val = next(vals)
            if val == '#':
                return None 

            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node

        vals = iter(data.split(','))
        return dfs()

        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

