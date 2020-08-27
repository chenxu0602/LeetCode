#
# @lc app=leetcode id=460 lang=python3
#
# [460] LFU Cache
#
# https://leetcode.com/problems/lfu-cache/description/
#
# algorithms
# Hard (34.05%)
# Likes:    1418
# Dislikes: 125
# Total Accepted:    77.4K
# Total Submissions: 225.8K
# Testcase Example:  '["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n' + '[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for Least Frequently Used (LFU) cache.
# It should support the following operations: get and put.
# 
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reaches its capacity, it should invalidate the least
# frequently used item before inserting a new item. For the purpose of this
# problem, when there is a tie (i.e., two or more keys that have the same
# frequency), the least recently used key would be evicted.
# 
# Note that the number of times an item is used is the number of calls to the
# get and put functions for that item since it was inserted. This number is set
# to zero when the item is removed.
# 
# 
# 
# Follow up:
# Could you do both operations in O(1) time complexity?
# 
# 
# 
# Example:
# 
# 
# LFUCache cache = new LFUCache( 2 /* capacity */ );
# 
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.get(3);       // returns 3.
# cache.put(4, 4);    // evicts key 1.
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DLinkedList:
    def __init__(self):
        self._sentinel = Node(None, None)
        self._sentinel.next = self._sentinel.prev = self._sentinel
        self._size = 0
        
    def __len__(self):
        return self._size
    
    def append(self, node):
        node.next = self._sentinel.next
        node.prev = self._sentinel
        node.next.prev = node
        self._sentinel.next = node
        self._size += 1
        
    def pop(self, node=None):
        if self._size == 0:
            return
        
        if not node:
            node = self._sentinel.prev
            
        node.prev.next = node.next
        node.next.prev = node.prev
        self._size -= 1
        
        return node


class LFUCache:

    def __init__(self, capacity: int):
        self._size = 0
        self._capacity = capacity
        
        self._node = dict()
        self._freq = defaultdict(DLinkedList)
        self._minfreq = 0

    def _update(self, node):
        freq = node.freq
        self._freq[freq].pop(node)
        if self._minfreq == freq and not self._freq[freq]:
            self._minfreq += 1
            
        node.freq += 1
        freq = node.freq
        self._freq[freq].append(node)
        

    def get(self, key: int) -> int:
        if key not in self._node:
            return -1
        
        node = self._node[key]
        self._update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return
        
        if key in self._node:
            node = self._node[key]
            self._update(node)
            node.val = value
        else:
            if self._size == self._capacity:
                node = self._freq[self._minfreq].pop()
                del self._node[node.key]
                self._size -= 1
                
            node = Node(key, value)
            self._node[key] = node
            self._freq[1].append(node)
            self._minfreq = 1
            self._size += 1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

