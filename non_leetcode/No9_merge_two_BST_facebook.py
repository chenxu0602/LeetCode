#!/usr/bin/python
# coding=utf-8
#Ebbinghaus:10/16/2019;13:20;[0,0,0,0,0,0,0,0,0]
################################################################################
'''
https://www.geeksforgeeks.org/merge-two-bsts-with-limited-extra-space/
Given two Binary Search Trees(BST), print the elements of both BSTs in sorted
form. The expected time complexity is O(m+n) where m is the number of nodes in
first tree and n is the number of nodes in second tree. Maximum allowed
auxiliary space is O(height of the first tree + height of the second tree).

Examples:

First BST
       3
    /     \
   1       5
Second BST
    4
  /   \
2       6
Output: 1 2 3 4 5 6


First BST
          8
         / \
        2   10
       /
      1
Second BST
          5
         /
        3
       /
      0
Output: 0 1 2 3 5 8 10
Source: Google interview question





Recommended: Please solve it on “PRACTICE” first, before moving on to the
solution.
A similar question has been discussed earlier. Let us first discuss already
discussed methods of the previous post which was for Balanced BSTs.
The method 1 can be applied here also, but the time complexity will be O(n^2)
in worst case. The method 2 can also be applied here, but the extra space
required will be O(n) which violates the constraint given in this question.
 Method 3 can be applied here but the step 3 of method 3 can’t be done in O(n)
 for an unbalanced BST.

Thanks to Kumar for suggesting the following solution.

The idea is to use iterative inorder traversal. We use two auxiliary stacks for
two BSTs. Since we need to print the elements in sorted form, whenever we get a
smaller element from any of the trees, we print it. If the element is greater, 
then we push it back to stack for the next iteration.

'''
################################################################################

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
build binary tree from list of value
'''
from collections import deque
class Build_Binary_Tree(object):
    def build_tree(self, nums):

        queue = deque()
        root = TreeNode(nums[0])
        queue.append((root, 0))
        while len(queue) > 0:
            current, i = queue.popleft()
            index_left = 2 * i + 1
            index_right = 2 * i + 2

            if current is None:
                continue

            if index_left < len(nums):
                if nums[index_left] is None:
                    current.left = None
                else:
                    current.left = TreeNode(nums[index_left])
                queue.append((current.left, index_left))
            if index_right < len(nums):
                if nums[index_right] is None:
                    current.right = None
                else:
                    current.right = TreeNode(nums[index_right])
                queue.append((current.right, index_right))
        return root

    def find_node_by_value(self, root, value):

        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            current = queue.popleft()
            if current.val == value:
                return current

            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return None
################################################################################
'''
Method1
Intuitive method:
(1)Inorder travesal both BST
(2)merge two sorted list
'''





'''
Method2:
probably need a stack to push the larger one into stack

'''
class Merge_BST(object):
    def merge(self, root1, root2):
        res = []
        stack = []

        return res

    def inorder_traversal(self, root1, root2, res, stack):
        pass





a = Build_Binary_Tree()
root1 = a.build_tree([8, 2, 10, 1, None,None,None])
root2 = a.build_tree([5, 3, None, 0, None,None,None])

# b = Merge_BST()
# print b.merge(root1, root2)

print 'here'













