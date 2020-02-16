#
# @lc app=leetcode id=1265 lang=python3
#
# [1265] Print Immutable Linked List in Reverse
#
# https://leetcode.com/problems/print-immutable-linked-list-in-reverse/description/
#
# algorithms
# Medium (95.19%)
# Likes:    68
# Dislikes: 12
# Total Accepted:    3.2K
# Total Submissions: 3.3K
# Testcase Example:  '[1,2,3,4]'
#
# You are given an immutable linked list, print out all values of each node in
# reverse with the help of the following interface:
# 
# 
# ImmutableListNode: An interface of immutable linked list, you are given the
# head of the list.
# 
# 
# You need to use the following functions to access the linked list (you can't
# access the ImmutableListNode directly):
# 
# 
# ImmutableListNode.printValue(): Print value of the current node.
# ImmutableListNode.getNext(): Return the next node.
# 
# 
# The input is only given to initialize the linked list internally. You must
# solve this problem without modifying the linked list. In other words, you
# must operate the linked list using only the mentioned APIs.
# 
# 
# 
# Follow up:
# 
# Could you solve this problem in:
# 
# 
# Constant space complexity?
# Linear time complexity and less than linear space complexity?
# 
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4]
# Output: [4,3,2,1]
# 
# 
# Example 2:
# 
# 
# Input: head = [0,-4,-1,3,-5]
# Output: [-5,3,-1,-4,0]
# 
# 
# Example 3:
# 
# 
# Input: head = [-2,0,6,4,4,-6]
# Output: [-6,4,4,6,0,-2]
# 
# 
# 
# 
# 
# 
# Constraints:
# 
# 
# The length of the linked list is between [1, 1000].
# The value of each node in the linked list is between [-1000, 1000].
# 
# 
#

# @lc code=start
# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        if head is None: return
        self.printLinkedListInReverse(head.getNext())
        head.printValue()
        
# @lc code=end

