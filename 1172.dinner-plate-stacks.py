#
# @lc app=leetcode id=1172 lang=python3
#
# [1172] Dinner Plate Stacks
#
# https://leetcode.com/problems/dinner-plate-stacks/description/
#
# algorithms
# Hard (39.30%)
# Likes:    91
# Dislikes: 11
# Total Accepted:    4.5K
# Total Submissions: 11.4K
# Testcase Example:  '["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]\n' + '[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]'
#
# You have an infinite number of stacks arranged in a row and numbered (left to
# right) from 0, each of the stacks has the same maximum capacity.
# 
# Implement the DinnerPlates class:
# 
# 
# DinnerPlates(int capacity) Initializes the object with the maximum capacity
# of the stacks.
# void push(int val) pushes the given positive integer val into the leftmost
# stack with size less than capacity.
# int pop() returns the value at the top of the rightmost non-empty stack and
# removes it from that stack, and returns -1 if all stacks are empty.
# int popAtStack(int index) returns the value at the top of the stack with the
# given index and removes it from that stack, and returns -1 if the stack with
# that given index is empty.
# 
# 
# Example:
# 
# 
# Input: 
# 
# ["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
# [[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]
# Output: 
# [null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]
# 
# Explanation: 
# DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
# D.push(1);
# D.push(2);
# D.push(3);
# D.push(4);
# D.push(5);         // The stacks are now:  2
# 4
# 1  3  5
# ⁠                                          ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 2.  The stacks are now:     4
# ⁠                                                      1  3  5
# ⁠                                                      ﹈ ﹈ ﹈
# D.push(20);        // The stacks are now: 20
# 4
# 1  3  5
# ⁠                                          ﹈ ﹈ ﹈
# D.push(21);        // The stacks are now: 20  4
# 21
# 1  3  5
# ⁠                                          ﹈ ﹈ ﹈
# D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
# ⁠                                                       1  3  5
# ⁠                                                       ﹈ ﹈ ﹈
# D.popAtStack(2);   // Returns 21.  The stacks are now:     4
# ⁠                                                       1  3  5
# ⁠                                                       ﹈ ﹈ ﹈ 
# D.pop()            // Returns 5.  The stacks are now:      4
# ⁠                                                       1  3 
# ⁠                                                       ﹈ ﹈  
# D.pop()            // Returns 4.  The stacks are now:   1  3 
# ⁠                                                       ﹈ ﹈   
# D.pop()            // Returns 3.  The stacks are now:   1 
# ⁠                                                       ﹈   
# D.pop()            // Returns 1.  There are no stacks.
# D.pop()            // Returns -1.  There are still no stacks.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= capacity <= 20000
# 1 <= val <= 20000
# 0 <= index <= 100000
# At most 200000 calls will be made to push, pop, and popAtStack.
# 
# 
#

# @lc code=start
import heapq

class DinnerPlates:

    def __init__(self, capacity: int):
        self.c = capacity        
        self.q = [] # record the available stack, will use heap to quickly find the smallest available stack
        self.stacks = []

    def push(self, val: int) -> None:
        while self.q and self.q[0] < len(self.stacks) and len(self.stacks[self.q[0]]) == self.c:
            heapq.heappop(self.q)

        if not self.q:
            heapq.heappush(self.q, len(self.stacks))

        if self.q[0] == len(self.stacks):
            self.stacks.append([])

        self.stacks[self.q[0]].append(val)

    def pop(self) -> int:
        while self.stacks and not self.stacks[-1]:
            self.stacks.pop()
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index: int) -> int:
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            heapq.heappush(self.q, index)
            return self.stacks[index].pop()
        return -1


# Your DinnerPlates object will be instantiated and called as such:
# obj = DinnerPlates(capacity)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAtStack(index)
# @lc code=end

