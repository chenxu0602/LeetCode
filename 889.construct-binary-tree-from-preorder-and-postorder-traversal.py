#
# @lc app=leetcode id=889 lang=python3
#
# [889] Construct Binary Tree from Preorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/description/
#
# algorithms
# Medium (64.33%)
# Likes:    645
# Dislikes: 42
# Total Accepted:    30.1K
# Total Submissions: 46.6K
# Testcase Example:  '[1,2,4,5,3,6,7]\n[4,5,2,6,7,3,1]'
#
# Return any binary tree that matches the given preorder and postorder
# traversals.
# 
# Values in the traversals pre and post are distinct positive integers.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= pre.length == post.length <= 30
# pre[] and post[] are both permutations of 1, 2, ..., pre.length.
# It is guaranteed an answer exists. If there exists multiple answers, you can
# return any of them.
# 
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
    preIndex, postIndex = 0, 0

    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        # Recursion
        # Time  complexity: O(N^2), where N is the number of nodes.
        # Space complexity: O(N^2)
        # if not pre: return None
        # root = TreeNode(pre[0])
        # if len(pre) == 1: return root

        # L = post.index(pre[1]) + 1
        # root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        # root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        # return root


        # Recursion (Space Saving Variant)
        # (i0, i1, N) refers to pre[i0:i0+N], post[i1:i1+N].
        # Time  complexity: O(N), where N is the number of nodes.
        # Space complexity: O(N)
        # def make(i0, i1, N):
        #     if N == 0: return None
        #     root = TreeNode(pre[i0])
        #     if N == 1: return root

        #     L = index[pre[i0 + 1]] - i1 + 1

        #     root.left = make(i0 + 1, i1, L)
        #     root.right = make(i0 + L + 1, i1 + L, N - 1 - L)
        #     return root

        # index = {v: i for i, v in enumerate(post)}
        # return make(0, 0, len(pre))


        # Recursion
        # Becasue root node will be lastly iterated in post order,
        # if root.val == post[posIndex], it means we have constructed the whole tree.
        # Time  complexity: O(N)
        # Space complexity: O(H)
        root = TreeNode(pre[self.preIndex])
        self.preIndex += 1
        if root.val != post[self.postIndex]:
            root.left = self.constructFromPrePost(pre, post)
        if root.val != post[self.postIndex]:
            root.right = self.constructFromPrePost(pre, post)
        self.postIndex += 1

        return root


        # Iteration
        # Iterate on pre array and construct node one by one.
        # stack save the current path of tree.
        # node = new TreeNode(pre[i]), if not left child, add node to the left. otherwise add it to the right.
        # If we meet a same value in the pre and post, it means we complete the construction for current subtree. We pop it from stack.
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # stack = [TreeNode(pre[0])]
        # j = 0
        # for v in pre[1:]:
        #     node = TreeNode(v)
        #     while stack[-1].val == post[j]:
        #         stack.pop()
        #         j += 1
        #     if not stack[-1].left:
        #         stack[-1].left = node
        #     else:
        #         stack[-1].right = node
        #     stack.append(node)
        # return stack[0]

        
# @lc code=end

