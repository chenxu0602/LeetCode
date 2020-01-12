#
# @lc app=leetcode id=641 lang=python3
#
# [641] Design Circular Deque
#
# https://leetcode.com/problems/design-circular-deque/description/
#
# algorithms
# Medium (49.58%)
# Likes:    115
# Dislikes: 30
# Total Accepted:    8K
# Total Submissions: 16.1K
# Testcase Example:  '["MyCircularDeque","insertLast","insertLast","insertFront","insertFront","getRear","isFull","deleteLast","insertFront","getFront"]\n' +
#
# Design your implementation of the circular double-ended queue (deque).
# 
# Your implementation should support following operations:
# 
# 
# MyCircularDeque(k): Constructor, set the size of the deque to be k.
# insertFront(): Adds an item at the front of Deque. Return true if the
# operation is successful.
# insertLast(): Adds an item at the rear of Deque. Return true if the operation
# is successful.
# deleteFront(): Deletes an item from the front of Deque. Return true if the
# operation is successful.
# deleteLast(): Deletes an item from the rear of Deque. Return true if the
# operation is successful.
# getFront(): Gets the front item from the Deque. If the deque is empty, return
# -1.
# getRear(): Gets the last item from Deque. If the deque is empty, return
# -1.
# isEmpty(): Checks whether Deque is empty or not. 
# isFull(): Checks whether Deque is full or not.
# 
# 
# 
# 
# Example:
# 
# 
# MyCircularDeque circularDeque = new MycircularDeque(3); // set the size to be
# 3
# circularDeque.insertLast(1);            // return true
# circularDeque.insertLast(2);            // return true
# circularDeque.insertFront(3);            // return true
# circularDeque.insertFront(4);            // return false, the queue is full
# circularDeque.getRear();              // return 2
# circularDeque.isFull();                // return true
# circularDeque.deleteLast();            // return true
# circularDeque.insertFront(4);            // return true
# circularDeque.getFront();            // return 4
# 
# 
# 
# 
# Note:
# 
# 
# All values will be in the range of [0, 1000].
# The number of operations will be in the range of [1, 1000].
# Please do not use the built-in Deque library.
# 
# 
#
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.len = k
        self.q = [None] * k
        self.front = (k - 1) % k
        self.last = 0
        

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if self.q[self.front] is None:
            self.q[self.front] = value
            self.front = (self.front - 1) % self.len
            return True
        else:
            return False
        
    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if self.q[self.last] is None:
            self.q[self.last] = value
            self.last = (self.last + 1) % self.len
            return True
        else:
            return False
        
    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if self.q[(self.front + 1) % self.len] is None:
            return False
        else:
            self.q[(self.front + 1) % self.len] = None
            self.front = (self.front + 1) % self.len
            return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if self.q[(self.last - 1) % self.len] is None:
            return False
        else:
            self.q[(self.last - 1) % self.len] = None
            self.last = (self.last - 1) % self.len
            return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        return self.q[(self.front + 1) % self.len] if self.q[(self.front + 1) % self.len] is not None else -1

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        return self.q[(self.last - 1) % self.len] if self.q[(self.last - 1) % self.len] is not None else -1 

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return (self.last - self.front) % self.len == 1 and self.q[(self.front + 1) % self.len] is None 

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """
        return (self.last - self.front) % self.len == 1 and self.q[(self.front + 1) % self.len] is not None
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()

