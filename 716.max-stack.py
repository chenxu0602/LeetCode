#
# @lc app=leetcode id=716 lang=python3
#
# [716] Max Stack
#
# https://leetcode.com/problems/max-stack/description/
#
# algorithms
# Easy (42.58%)
# Likes:    742
# Dislikes: 164
# Total Accepted:    57K
# Total Submissions: 133.9K
# Testcase Example:  '["MaxStack","push","push","push","top","popMax","top","peekMax","pop","top"]\n' + '[[],[5],[1],[5],[],[],[],[],[],[]]'
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

# @lc code=start
import heapq

class MaxStack:
    # O(logn)

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ls, self.hp = [], []
        self.lsd, self.hpd = set(), set()
        self.id = 0

    def push(self, x: int) -> None:
        self.ls.append((self.id, x))
        heapq.heappush(self.hp, (-x, -self.id))
        self.id += 1

    def pop(self) -> int:
        x = self.top()
        self.hpd.add(self.ls[-1][0])
        self.ls.pop()
        return x

    def top(self) -> int:
        while self.ls[-1][0] in self.lsd:
            self.lsd.remove(self.ls[-1][0])
            self.ls.pop()
        return self.ls[-1][1]

    def peekMax(self) -> int:
        while -self.hp[0][1] in self.hpd:
            self.hpd.remove(-self.hp[0][1])
            heapq.heappop(self.hp)
        return -self.hp[0][0]
        
    def popMax(self) -> int:
        x = self.peekMax()
        _, nid = heapq.heappop(self.hp)
        self.lsd.add(-nid)
        return x
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
# @lc code=end

