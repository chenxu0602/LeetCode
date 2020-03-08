#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#
# https://leetcode.com/problems/copy-list-with-random-pointer/description/
#
# algorithms
# Medium (32.17%)
# Likes:    2473
# Dislikes: 570
# Total Accepted:    341.4K
# Total Submissions: 1.1M
# Testcase Example:  '[[7,null],[13,0],[11,4],[10,2],[1,0]]\r'
#
# A linked list is given such that each node contains an additional random
# pointer which could point to any node in the list or null.
# 
# Return a deep copy of the list.
# 
# The Linked List is represented in the input/output as a list of n nodes. Each
# node is represented as a pair of [val, random_index] where:
# 
# 
# val: an integer representing Node.val
# random_index: the index of the node (range from 0 to n-1) where random
# pointer points to, or null if it does not point to any node.
# 
# 
# 
# Example 1:
# 
# 
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# 
# 
# Example 2:
# 
# 
# Input: head = [[1,1],[2,1]]
# Output: [[1,1],[2,1]]
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: head = [[3,null],[3,0],[3,null]]
# Output: [[3,null],[3,0],[3,null]]
# 
# 
# Example 4:
# 
# 
# Input: head = []
# Output: []
# Explanation: Given linked list is empty (null pointer), so return null.
# 
# 
# 
# Constraints:
# 
# 
# -10000 <= Node.val <= 10000
# Node.random is null or pointing to a node in the linked list.
# Number of Nodes will not exceed 1000.
# 
# 
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def __init__(self):
        self.visited = {}

    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None: return None

        if head in self.visited: 
            return self.visited[head]

        node = Node(head.val, None, None)
        self.visited[head] = node
        
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node
        


        # def getClonedNode(node):
        #     if node:
        #         if node in self.visited:
        #             return self.visited[node]
        #         else:
        #             self.visited[node] = Node(node.val, None, Node)
        #             return self.visited[node]
        #     return None

        # if not head: return head
        # old_node = head
        # new_node = Node(old_node.val, None, None)
        # self.visited[old_node] = new_node

        # while old_node:
        #     new_node.random = getClonedNode(old_node.random)
        #     new_node.next = getClonedNode(old_node.next)

        #     old_node = old_node.next
        #     new_node = new_node.next

        # return self.visited[head]


        
# @lc code=end

