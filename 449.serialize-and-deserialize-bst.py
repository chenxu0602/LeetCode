#
# @lc app=leetcode id=449 lang=python3
#
# [449] Serialize and Deserialize BST
#
# https://leetcode.com/problems/serialize-and-deserialize-bst/description/
#
# algorithms
# Medium (51.82%)
# Likes:    1349
# Dislikes: 70
# Total Accepted:    106.4K
# Total Submissions: 204.2K
# Testcase Example:  '[2,1,3]'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# 
# Design an algorithm to serialize and deserialize a binary search tree. There
# is no restriction on how your serialization/deserialization algorithm should
# work. You just need to ensure that a binary search tree can be serialized to
# a string and this string can be deserialized to the original tree structure.
# 
# The encoded string should be as compact as possible.
# 
# Note: Do not use class member/global/static variables to store states. Your
# serialize and deserialize algorithms should be stateless.
# 
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        # Time  complexity: O(N)
        # Space complexity: O(N)
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []
        return ' '.join(map(str, postorder(root)))

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        # Time  complexity: O(N)
        # Space complexity: O(N)
        def helper(lower=float("-inf"), upper=float("inf")):
            if not data or data[-1] < lower or data[-1] > upper:
                return None

            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root

        data = [int(x) for x in data.split(' ') if x]
        return helper()
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# @lc code=end

