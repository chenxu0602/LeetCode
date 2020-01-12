#
# @lc app=leetcode id=716 lang=python3
#
# [716] Max Stack
#
# https://leetcode.com/problems/max-stack/description/
#
# algorithms
# Easy (40.28%)
# Likes:    384
# Dislikes: 67
# Total Accepted:    28.8K
# Total Submissions: 71.1K
# Testcase Example:  '["MaxStack","push","push","push","top","popMax","top","peekMax","pop","top"]\n' +
#
# Design a max stack that supports push, pop, top, peekMax and popMax.
# 
# 
# 
# push(x) -- Push element x onto stack.
# pop() -- Remove the element on top of the stack and return it.
# top() -- Get the element on the top.
# peekMax() -- Retrieve the maximum element in the stack.
# popMax() -- Retrieve the maximum element in the stack, and remove it. If you
# find more than one maximum elements, only remove the top-most one.
# 
# 
# 
# Example 1:
# 
# MaxStack stack = new MaxStack();
# stack.push(5); 
# stack.push(1);
# stack.push(5);
# stack.top(); -> 5
# stack.popMax(); -> 5
# stack.top(); -> 1
# stack.peekMax(); -> 5
# stack.pop(); -> 1
# stack.top(); -> 5
# 
# 
# 
# Note:
# 
# -1e7 
# Number of operations won't exceed 10000.
# The last four operations won't be called when stack is empty.
# 
# 
#

class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.maxstack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.maxstack:
            self.maxstack.append(x)
        else:
            self.maxstack.append(max(x, self.maxstack[-1]))
        

    def pop(self) -> int:
        if self.stack:
            self.maxstack.pop()
            return self.stack.pop()
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
    def peekMax(self) -> int:
        if self.maxstack:
            return self.maxstack[-1]
        

    def popMax(self) -> int:
        m = self.peekMax()

        tmp = []
        while m != self.stack[-1]:
            tmp.append(self.pop())
        
        ret = self.stack.pop()
        self.maxstack.pop()

        for i in range(len(tmp) - 1, -1, -1):
            self.push(tmp[i])

        return ret


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

