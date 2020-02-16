#
# @lc app=leetcode id=622 lang=python3
#
# [622] Design Circular Queue
#
# https://leetcode.com/problems/design-circular-queue/description/
#
# algorithms
# Medium (42.01%)
# Likes:    417
# Dislikes: 66
# Total Accepted:    47.1K
# Total Submissions: 112.1K
# Testcase Example:  '["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","Rear","isFull","deQueue","enQueue","Rear"]\n' + '[[3],[1],[2],[3],[4],[],[],[],[4],[]]'
#
# Design your implementation of the circular queue. The circular queue is a
# linear data structure in which the operations are performed based on FIFO
# (First In First Out) principle and the last position is connected back to the
# first position to make a circle. It is also called "Ring Buffer".
# 
# One of the benefits of the circular queue is that we can make use of the
# spaces in front of the queue. In a normal queue, once the queue becomes full,
# we cannot insert the next element even if there is a space in front of the
# queue. But using the circular queue, we can use the space to store new
# values.
# 
# Your implementation should support following operations:
# 
# 
# MyCircularQueue(k): Constructor, set the size of the queue to be k.
# Front: Get the front item from the queue. If the queue is empty, return
# -1.
# Rear: Get the last item from the queue. If the queue is empty, return -1.
# enQueue(value): Insert an element into the circular queue. Return true if the
# operation is successful.
# deQueue(): Delete an element from the circular queue. Return true if the
# operation is successful.
# isEmpty(): Checks whether the circular queue is empty or not.
# isFull(): Checks whether the circular queue is full or not.
# 
# 
# 
# 
# Example:
# 
# 
# MyCircularQueue circularQueue = new MyCircularQueue(3); // set the size to be
# 3
# circularQueue.enQueue(1);  // return true
# circularQueue.enQueue(2);  // return true
# circularQueue.enQueue(3);  // return true
# circularQueue.enQueue(4);  // return false, the queue is full
# circularQueue.Rear();  // return 3
# circularQueue.isFull();  // return true
# circularQueue.deQueue();  // return true
# circularQueue.enQueue(4);  // return true
# circularQueue.Rear();  // return 4
# 
# 
# 
# Note:
# 
# 
# All values will be in the range of [0, 1000].
# The number of operations will be in the range of [1, 1000].
# Please do not use the built-in Queue library.
# 
# 
#

# @lc code=start
from threading import Lock

class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.queue = [0] * k
        self.headIndex = 0
        self.count = 0
        self.capacity = k
        self.queueLock = Lock()
        

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        with self.queueLock:
            if self.count == self.capacity:
                return False
            self.queue[(self.headIndex + self.count) % self.capacity] = value
            self.count += 1
        return True 

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.count == 0: return False
        self.headIndex = (self.headIndex + 1) % self.capacity
        self.count -= 1
        return True
        

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.count == 0:
            return -1
        return self.queue[self.headIndex]
        

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.count == 0:
            return -1
        return self.queue[(self.headIndex + self.count - 1) % self.capacity]
        
        

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0
        

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

