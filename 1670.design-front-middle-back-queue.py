#
# @lc app=leetcode id=1670 lang=python3
#
# [1670] Design Front Middle Back Queue
#
# https://leetcode.com/problems/design-front-middle-back-queue/description/
#
# algorithms
# Medium (54.03%)
# Likes:    86
# Dislikes: 21
# Total Accepted:    4K
# Total Submissions: 7.4K
# Testcase Example:  '["FrontMiddleBackQueue","pushFront","pushBack","pushMiddle","pushMiddle","popFront","popMiddle","popMiddle","popBack","popFront"]\n' + '[[],[1],[2],[3],[4],[],[],[],[],[]]'
#
# Design a queue that supports push and pop operations in the front, middle,
# and back.
# 
# Implement the FrontMiddleBack class:
# 
# 
# FrontMiddleBack() Initializes the queue.
# void pushFront(int val) Adds val to the front of the queue.
# void pushMiddle(int val) Adds val to the middle of the queue.
# void pushBack(int val) Adds val to the back of the queue.
# int popFront() Removes the front element of the queue and returns it. If the
# queue is empty, return -1.
# int popMiddle() Removes the middle element of the queue and returns it. If
# the queue is empty, return -1.
# int popBack() Removes the back element of the queue and returns it. If the
# queue is empty, return -1.
# 
# 
# Notice that when there are two middle position choices, the operation is
# performed on the frontmost middle position choice. For example:
# 
# 
# Pushing 6 into the middle of [1, 2, 3, 4, 5] results in [1, 2, 6, 3, 4,
# 5].
# Popping the middle from [1, 2, 3, 4, 5, 6] returns 3 and results in [1, 2, 4,
# 5, 6].
# 
# 
# 
# Example 1:
# 
# 
# Input:
# ["FrontMiddleBackQueue", "pushFront", "pushBack", "pushMiddle", "pushMiddle",
# "popFront", "popMiddle", "popMiddle", "popBack", "popFront"]
# [[], [1], [2], [3], [4], [], [], [], [], []]
# Output:
# [null, null, null, null, null, 1, 3, 4, 2, -1]
# 
# Explanation:
# FrontMiddleBackQueue q = new FrontMiddleBackQueue();
# q.pushFront(1);   // [1]
# q.pushBack(2);    // [1, 2]
# q.pushMiddle(3);  // [1, 3, 2]
# q.pushMiddle(4);  // [1, 4, 3, 2]
# q.popFront();     // return 1 -> [4, 3, 2]
# q.popMiddle();    // return 3 -> [4, 2]
# q.popMiddle();    // return 4 -> [2]
# q.popBack();      // return 2 -> []
# q.popFront();     // return -1 -> [] (The queue is empty)
# 
# 
# 
# Constraints:
# 
# 
# 1 <= val <= 10^9
# At most 1000 calls will be made to pushFront, pushMiddle, pushBack, popFront,
# popMiddle, and popBack.
# 
# 
#

# @lc code=start
from collections import deque

class FrontMiddleBackQueue:

    def __init__(self):
        self.A, self.B = deque(), deque() 

    def pushFront(self, val: int) -> None:
        self.A.appendleft(val) 
        self.balance()

    def pushMiddle(self, val: int) -> None:
        if len(self.A) > len(self.B):
              self.B.appendleft(self.A.pop()) 
        self.A.append(val)

    def pushBack(self, val: int) -> None:
        self.B.append(val) 
        self.balance()

    def popFront(self) -> int:
        val = self.A.popleft() if self.A else -1 
        self.balance()
        return val

    def popMiddle(self) -> int:
        val = (self.A or [-1]).pop() 
        self.balance()
        return val

    def popBack(self) -> int:
        val = (self.B or self.A or [-1]).pop()   
        self.balance()
        return val
        
    def balance(self):
        if len(self.A) > len(self.B) + 1:
            self.B.appendleft(self.A.pop())    
        if len(self.A) < len(self.B):
            self.A.append(self.B.popleft())
        

# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
# @lc code=end

