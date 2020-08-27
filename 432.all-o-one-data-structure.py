#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#
# https://leetcode.com/problems/all-oone-data-structure/description/
#
# algorithms
# Hard (32.29%)
# Likes:    636
# Dislikes: 76
# Total Accepted:    32.6K
# Total Submissions: 100.4K
# Testcase Example:  '["AllOne","getMaxKey","getMinKey"]\n[[],[],[]]'
#
# Implement a data structure supporting the following operations:
# 
# 
# 
# Inc(Key) - Inserts a new key  with value 1. Or increments an existing key by
# 1. Key is guaranteed to be a non-empty string.
# Dec(Key) - If Key's value is 1, remove it from the data structure. Otherwise
# decrements an existing key by 1. If the key does not exist, this function
# does nothing. Key is guaranteed to be a non-empty string.
# GetMaxKey() - Returns one of the keys with maximal value. If no element
# exists, return an empty string "".
# GetMinKey() - Returns one of the keys with minimal value. If no element
# exists, return an empty string "".
# 
# 
# 
# 
# Challenge: Perform all these in O(1) time complexity.
# 
#

# @lc code=start
class Node:
    def __init__(self, val):
        self.val = val
        self.keys = set()
        self.prev = self.next = None

    def __repr__(self):
        return repr(str(self.val) + ';' + str(self.keys))

    def getAnyKey(self) -> str:
        if self.keys:
            elem = self.keys.pop()
            self.keys.add(elem)
            return elem
        else:
            return ""

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(float("inf"))
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key not in self.map:
            if self.tail.prev.val == 1:
                self.tail.prev.keys.add(key)
                self.map[key] = self.tail.prev
            else:
                self.map[key] = self.insertBefore(self.tail, key)
        else:
            node = self.map[key]
            node.keys.remove(key)
            if node.val + 1 == node.prev.val:
                node.prev.keys.add(key)
                self.map[key] = node.prev
            else:
                self.map[key] = self.insertBefore(node, key)

            self.removeNodeIfEmpty(node)
        

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.map:
            return

        node = self.map[key]
        node.keys.remove(key)
        if node.val == 1:
            self.map.pop(key, None)
        else:
            if node.val - 1 == node.next.val:
                node.next.keys.add(key)
                self.map[key] = node.next
            else:
                self.map[key] = self.insertAfter(node, key)

        self.removeNodeIfEmpty(node)
        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        return self.head.next.getAnyKey()
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        return self.tail.prev.getAnyKey()
        

    def removeNodeIfEmpty(self, node: Node) -> None:
        if not node.keys:
            node.prev.next = node.next
            node.next.prev = node.prev
            del node

    def insertBefore(self, node: Node, key: str) -> Node:
        new_node = Node(node.val + 1)
        new_node.keys.add(key)
        new_node.prev = node.prev
        node.prev.next = new_node
        new_node.next = node
        node.prev = new_node
        return new_node

    def insertAfter(self, node: Node, key: str) -> Node:
        new_node = Node(node.val - 1)
        new_node.keys.add(key)
        new_node.next = node.next
        node.next.prev = new_node
        new_node.prev = node
        node.next = new_node
        return new_node

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
# @lc code=end

