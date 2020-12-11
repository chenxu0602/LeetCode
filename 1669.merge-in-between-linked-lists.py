#
# @lc app=leetcode id=1669 lang=python3
#
# [1669] Merge In Between Linked Lists
#
# https://leetcode.com/problems/merge-in-between-linked-lists/description/
#
# algorithms
# Medium (83.05%)
# Likes:    87
# Dislikes: 8
# Total Accepted:    6.3K
# Total Submissions: 7.6K
# Testcase Example:  '[0,1,2,3,4,5]\n3\n4\n[1000000,1000001,1000002]'
#
# You are given two linked lists: list1 and list2 of sizes n and m
# respectively.
# 
# Remove list1's nodes from the a^th node to the b^th node, and put list2 in
# their place.
# 
# The blue edges and nodes in the following figure incidate the result:
# 
# Build the result list and return its head.
# 
# 
# Example 1:
# 
# 
# Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
# Output: [0,1,2,1000000,1000001,1000002,5]
# Explanation: We remove the nodes 3 and 4 and put the entire list2 in their
# place. The blue edges and nodes in the above figure indicate the result.
# 
# 
# Example 2:
# 
# 
# Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 =
# [1000000,1000001,1000002,1000003,1000004]
# Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
# Explanation: The blue edges and nodes in the above figure indicate the
# result.
# 
# 
# 
# Constraints:
# 
# 
# 3 <= list1.length <= 10^4
# 1 <= a <= b < list1.length - 1
# 1 <= list2.length <= 10^4
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start, end = None, list1
        for i in range(b):
            if i == a - 1:
                start = end
            end = end.next
        start.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = end.next
        end.next = None
        return list1
        
# @lc code=end

