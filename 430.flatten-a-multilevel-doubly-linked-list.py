#
# @lc app=leetcode id=430 lang=python3
#
# [430] Flatten a Multilevel Doubly Linked List
#
# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/description/
#
# algorithms
# Medium (48.84%)
# Likes:    818
# Dislikes: 127
# Total Accepted:    59.2K
# Total Submissions: 120.1K
# Testcase Example:  '[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]\r'
#
# You are given a doubly linked list which in addition to the next and previous
# pointers, it could have a child pointer, which may or may not point to a
# separate doubly linked list. These child lists may have one or more children
# of their own, and so on, to produce a multilevel data structure, as shown in
# the example below.
# 
# Flatten the list so that all the nodes appear in a single-level, doubly
# linked list. You are given the head of the first level of the list.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]
# Explanation:
# 
# The multilevel linked list in the input is as follows:
# 
# 
# 
# After flattening the multilevel linked list it becomes:
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2,null,3]
# Output: [1,3,2]
# Explanation:
# 
# The input multilevel linked list is as follows:
# 
# ⁠ 1---2---NULL
# ⁠ |
# ⁠ 3---NULL
# 
# 
# Example 3:
# 
# 
# Input: head = []
# Output: []
# 
# 
# 
# 
# How multilevel linked list is represented in test case:
# 
# We use the multilevel linked list from Example 1 above:
# 
# 
# ⁠1---2---3---4---5---6--NULL
# ⁠        |
# ⁠        7---8---9---10--NULL
# ⁠            |
# ⁠            11--12--NULL
# 
# The serialization of each level is as follows:
# 
# 
# [1,2,3,4,5,6,null]
# [7,8,9,10,null]
# [11,12,null]
# 
# 
# To serialize all levels together we will add nulls in each level to signify
# no node connects to the upper node of the previous level. The serialization
# becomes:
# 
# 
# [1,2,3,4,5,6,null]
# [null,null,7,8,9,10,null]
# [null,11,12,null]
# 
# 
# Merging the serialization of each level and removing trailing nulls we
# obtain:
# 
# 
# [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# 
# 
# Constraints:
# 
# 
# Number of Nodes will not exceed 1000.
# 1 <= Node.val <= 10^5
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        # DFS by Recursion
        # Time  complexity: O(N)
        # Space complexity: O(N)
        # def flatten_dfs(prev, curr):
        #     if not curr:
        #         return prev

        #     curr.prev = prev
        #     prev.next = curr

        #     # the curr.next would be tempered in the recursive function
        #     tempNext = curr.next
        #     tail = flatten_dfs(curr, curr.child)
        #     curr.child = None
        #     return flatten_dfs(tail, tempNext)

        # if not head: return head

        # # pseudo head to ensure the `prev` pointer is never none
        # pseudoHead = Node(None, None, head, None)
        # flatten_dfs(pseudoHead, head)

        # # detach the pseudo head from the real head
        # pseudoHead.next.prev = None
        # return pseudoHead.next


        # DFS by Iteration
        # Time  complexity: O(N)
        # Space complexity: O(N)
        if not head:
            return

        pseudoHead = Node(0, None, head, None)
        prev = pseudoHead

        stack = [head,]

        while stack:
            curr = stack.pop()

            prev.next = curr
            curr.prev = prev

            if curr.next:
                stack.append(curr.next)

            if curr.child:
                stack.append(curr.child)
                # don't forget to remove all child pointers.
                curr.child = None

            prev = curr

        # detach the pseudo head node from the result.
        pseudoHead.next.prev = None
        return pseudoHead.next
        
# @lc code=end

