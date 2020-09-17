#
# @lc app=leetcode id=895 lang=python3
#
# [895] Maximum Frequency Stack
#
# https://leetcode.com/problems/maximum-frequency-stack/description/
#
# algorithms
# Hard (60.56%)
# Likes:    1068
# Dislikes: 19
# Total Accepted:    39.1K
# Total Submissions: 63.6K
# Testcase Example:  '["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"]\n' + '[[],[5],[7],[5],[7],[4],[5],[],[],[],[]]'
#
# Implement FreqStack, a class which simulates the operation of a stack-like
# data structure.
# 
# FreqStack has two functions:
# 
# 
# push(int x), which pushes an integer x onto the stack.
# pop(), which removes and returns the most frequent element in the
# stack.
# 
# If there is a tie for most frequent element, the element closest to the top
# of the stack is removed and returned.
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: 
# 
# ["FreqStack","push","push","push","push","push","push","pop","pop","pop","pop"],
# [[],[5],[7],[5],[7],[4],[5],[],[],[],[]]
# Output: [null,null,null,null,null,null,null,5,7,5,4]
# Explanation:
# After making six .push operations, the stack is [5,7,5,7,4,5] from bottom to
# top.  Then:
# 
# pop() -> returns 5, as 5 is the most frequent.
# The stack becomes [5,7,5,7,4].
# 
# pop() -> returns 7, as 5 and 7 is the most frequent, but 7 is closest to the
# top.
# The stack becomes [5,7,5,4].
# 
# pop() -> returns 5.
# The stack becomes [5,7,4].
# 
# pop() -> returns 4.
# The stack becomes [5,7].
# 
# 
# 
# 
# Note:
# 
# 
# Calls to FreqStack.push(int x) will be such that 0 <= x <= 10^9.
# It is guaranteed that FreqStack.pop() won't be called if the stack has zero
# elements.
# The total number of FreqStack.push calls will not exceed 10000 in a single
# test case.
# The total number of FreqStack.pop calls will not exceed 10000 in a single
# test case.
# The total number of FreqStack.push and FreqStack.pop calls will not exceed
# 150000 across all test cases.
# 
# 
# 
# 
# 
# 
#

# @lc code=start
import heapq 
from collections import defaultdict, Counter

class FreqStack:

    def __init__(self):
       # Stack of Stacks    
       # Time  complexity: O(1) for both push and pop operations.
       # Space complexity: O(N), where N is the number of elements in the FreqStack.
       self.freq = Counter()
       self.group = defaultdict(list)
       self.maxfreq = 0

      # self.mem = {}
      # self.pq = []
      # self.count = 0
        
    def push(self, x: int) -> None:
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

      #   self.count += 1
      #   self.mem[x] = self.mem.get(x, 0) + 1
      #   heapq.heappush(self.pq, (-self.mem[x], -self.count, x))
        
    def pop(self) -> int:
        x = self.group[self.maxfreq].pop()   
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x
        
      #   _, _, val = heapq.heappop(self.pq)
      #   self.mem[val] -= 1
      #   return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
# @lc code=end

