#
# @lc app=leetcode id=432 lang=python3
#
# [432] All O`one Data Structure
#
# https://leetcode.com/problems/all-oone-data-structure/description/
#
# algorithms
# Hard (29.77%)
# Likes:    350
# Dislikes: 53
# Total Accepted:    19.2K
# Total Submissions: 64.3K
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

class Block(object):
    def __init__(self, val=0):
        self.val = val
        self.keys = set()
        self.before = None
        self.after = None

    def remove(self):
        self.before.after = self.after
        self.after.before = self.before
        self.before, self.after = None, None

    def insert_after(self, new_block):
        old_after =self.after
        self.after = new_block
        new_block.before = self
        new_block.after = old_after
        old_after.before = new_block

class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.begin = Block()
        self.end = Block()
        self.begin.after = self.end
        self.end.before = self.begin
        self.mapping = {}
        

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """

        if not key in self.mapping:
            current_block = self.begin
        else:
            current_block = self.mapping[key]
            current_block.keys.remove(key)

        if current_block.val + 1 != current_block.after.val:
            new_block = Block(current_block.val + 1)
            current_block.insert_after(new_block)
        else:
            new_block = current_block.after

        new_block.keys.add(key)
        self.mapping[key] = new_block

        if not current_block.keys and current_block.val != 0:
            current_block.remove()


    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """

        if not key in self.mapping:
            return

        current_block = self.mapping[key]
        del self.mapping[key]
        current_block.keys.remove(key)

        if current_block.val != 1:
            if current_block.val - 1 != current_block.before.val:
                new_block = Block(current_block.val - 1)
                current_block.before.insert_after(new_block)
            else:
                new_block = current_block.before
            new_block.keys.add(key)
            self.mapping[key] = new_block

        if not current_block.keys:
            current_block.remove()

        

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """

        if self.end.before.val == 0:
            return ""

        key = self.end.before.keys.pop()
        self.end.before.keys.add(key)
        return key
        

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        if self.begin.after.val == 0:
            return ""

        key = self.begin.after.keys.pop()
        self.begin.after.keys.add(key)
        return key
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

