#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (44.66%)
# Likes:    1535
# Dislikes: 79
# Total Accepted:    215.6K
# Total Submissions: 482.2K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
# 
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
# 
# Example:
# 
# 
# Given the sorted linked list: [-10,-3,0,5,9],
# 
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
# 
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        
        # Time  complexity: O(nlogn)
        # Space complexity: O(logn)
        # if not head: return None
        # if not head.next: return TreeNode(head.val)

        # slow, fast = head, head.next.next
        # while fast and fast.next:
        #     slow, fast = slow.next, fast.next.next

        # mid = slow.next
        # slow.next = None

        # root = TreeNode(mid.val)
        # root.left = self.sortedListToBST(head)
        # root.right = self.sortedListToBST(mid.next)

        # return root


        # Conversion to Array
        # Time  complexity: O(n)
        # Space complexity: O(n)
        # def mapListToValues(node):
        #     vals = []
        #     while node:
        #         vals.append(node.val)
        #         node = node.next
        #     return vals

        # values = mapListToValues(head)

        # def convertListToBst(l, r):
        #     if l > r:
        #         return None

        #     mid = (l + r) // 2
        #     node = TreeNode(values[mid])

        #     if l == r:
        #         return node

        #     node.left = convertListToBst(l, mid - 1)
        #     node.right = convertListToBst(mid + 1, r)

        #     return node

        # return convertListToBst(0, len(values) - 1)



        # Inorder Simulation
        # Time  complexity: O(n)
        # Space complexity: O(logn)
        def findSize(node):
            ptr = node
            c = 0
            while ptr:
                ptr = ptr.next
                c += 1
            return c

        size = findSize(head)

        # Recursively form a BST out of linked list from l --> r
        def convert(l, r):
            nonlocal head

            if l > r:
                return None

            mid = (l + r) // 2

            # First step of simulated inorder traversal. Recursively form the left half
            left = convert(l, mid - 1)

            # Once left half is traversed, process the current node
            node = TreeNode(head.val)
            node.left = left

            # Maintain the invariance mentioned in the algorithm
            head = head.next

            # Recurse on the right hand side and form BST out of them
            node.right = convert(mid + 1, r)

            return node

        return convert(0, size - 1)

        
# @lc code=end

