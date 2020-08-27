#
# @lc app=leetcode id=431 lang=python3
#
# [431] Encode N-ary Tree to Binary Tree
#
# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/description/
#
# algorithms
# Hard (70.69%)
# Likes:    183
# Dislikes: 14
# Total Accepted:    6.5K
# Total Submissions: 9.2K
# Testcase Example:  '[1,null,3,2,4,null,5,6]'
#
# Design an algorithm to encode an N-ary tree into a binary tree and decode the
# binary tree to get the original N-ary tree. An N-ary tree is a rooted tree in
# which each node has no more than N children. Similarly, a binary tree is a
# rooted tree in which each node has no more than 2 children. There is no
# restriction on how your encode/decode algorithm should work. You just need to
# ensure that an N-ary tree can be encoded to a binary tree and this binary
# tree can be decoded to the original N-nary tree structure.
# 
# Nary-Tree input serialization is represented in their level order traversal,
# each group of children is separated by the null value (See following
# example).
# 
# For example, you may encode the following 3-ary tree to a binary tree in this
# way:
# 
# 
# 
# 
# Input: root = [1,null,3,2,4,null,5,6]
# 
# 
# Note that the above is just an example which might or might not work. You do
# not necessarily need to follow this format, so please be creative and come up
# with different approaches yourself.
# 
# 
# 
# 
# 
# Constraints:
# 
# 
# The height of the n-ary tree is less than or equal to 1000
# The total number of nodes is between [0, 10^4]
# Do not use class member/global/static variables to store states. Your encode
# and decode algorithms should be stateless.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
from collections import deque

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Node') -> TreeNode:
        # BFS (Breadth-First Search) Traversal
        # Time  complexity: O(N)
        # Space complexity: O(L) where L is the maximum number of nodes that reside at the same level.
        # if not root:
        #     return None

        # rootNode = TreeNode(root.val)
        # queue = deque([(rootNode, root)])

        # while queue:
        #     parent, curr = queue.popleft()
        #     prevBNode, headBNode = None, None
        #     # traverse each child one by one
        #     for child in curr.children:
        #         newBNode = TreeNode(child.val)
        #         if prevBNode:
        #             prevBNode.right = newBNode
        #         else:
        #             headBNode = newBNode
        #         prevBNode = newBNode
        #         queue.append((newBNode, child))

        #     # use the first child in the left node of parent
        #     parent.left = headBNode

        # return rootNode


        # DFS (Depth-First Search) Traversal
        # At the beginning of the encode(node) function, we create a binary tree node to contain the value of the current node.
        # Then we put the first child of the N-ary tree node as the left node of the newly-created binary tree node. We call the encoding function recursively to encode the first child node as well.
        # For the rest of the children nodes of the N-ary tree node, we chain them up with the right pointer of the binary tree node. And again, we call recursively the encoding function to encode each of the child node.
        # Time  complexity: O(N)
        # Space complexity: O(D) where D is the depth of the N-ary tree.
        if not root:
            return None

        rootNode = TreeNode(root.val)
        if len(root.children) > 0:
            firstChild = root.children[0]
            rootNode.left = self.encode(firstChild)

        # the parent for the rest of the children
        curr = rootNode.left

        # encode the rest of the children
        for i in range(1, len(root.children)):
            curr.right = self.encode(root.children[i])
            curr = curr.right

        return rootNode
        
	
	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> 'Node':
        # BFS (Breadth-First Search) Traversal
        # Time  complexity: O(N)
        # Space complexity: O(L) where L is the maximum number of nodes that reside at the same level.
        # if not data:
        #     return None

        # # should set the default value to [] rather than None,
        # # otherwise it wont pass the test cases.
        # rootNode = Node(data.val, [])

        # queue = deque([(rootNode, data)])

        # while queue:
        #     parent, curr = queue.popleft()

        #     firstChild = curr.left
        #     sibling = firstChild

        #     while sibling:
        #         # Note: the initial value of the children list should not be None, which is assumed by the online judge.
        #         newNode = Node(sibling.val, [])
        #         parent.children.append(newNode)
        #         queue.append((newNode, sibling))
        #         sibling = sibling.right

        # return rootNode
        

        # DFS (Depth-First Search) Traversal
        # At the beginning of the encode(node) function, we create a binary tree node to contain the value of the current node.
        # Then we put the first child of the N-ary tree node as the left node of the newly-created binary tree node. We call the encoding function recursively to encode the first child node as well.
        # For the rest of the children nodes of the N-ary tree node, we chain them up with the right pointer of the binary tree node. And again, we call recursively the encoding function to encode each of the child node.
        # Time  complexity: O(N)
        # Space complexity: O(D) where D is the depth of the N-ary tree.
        if not data:
            return None

        rootNode = Node(data.val, [])

        curr = data.left
        while curr:
            rootNode.children.append(self.decode(curr))
            curr = curr.right

        return rootNode

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
# @lc code=end

