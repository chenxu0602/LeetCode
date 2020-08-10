#
# @lc app=leetcode id=346 lang=python3
#
# [346] Moving Average from Data Stream
#
# https://leetcode.com/problems/moving-average-from-data-stream/description/
#
# algorithms
# Easy (68.97%)
# Likes:    450
# Dislikes: 49
# Total Accepted:    104.1K
# Total Submissions: 150.9K
# Testcase Example:  '["MovingAverage","next","next","next","next"]\n[[3],[1],[10],[3],[5]]'
#
# Given a stream of integers and a window size, calculate the moving average of
# all integers in the sliding window.
# 
# Example:
# 
# 
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
# 
# 
# 
# 
#

# @lc code=start
from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        # Double-ended Queue
        # Time  complexity: O(1)
        # Space complexity: O(N), where N is the size of the moving window
        # self.size = size
        # self.queue = deque()
        # self.window_sum = 0
        # self.count = 0


        # Circular Queue with Array
        # tail = (head + 1) mod size
        # Time  complexity: O(1)
        # Space complexity: O(N), where N is the size of the circular queue.
        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        self.count = 0
        

    def next(self, val: int) -> float:
        # Double-ended Queue
        # Time  complexity: O(1)
        # Space complexity: O(N), where N is the size of the moving window
        # self.count += 1
        # # calculate the new sum by shifting the window
        # self.queue.append(val)
        # tail = self.queue.popleft() if self.count > self.size else 0
        # self.window_sum = self.window_sum - tail + val
        # return self.window_sum / min(self.size, self.count)
        

        # Circular Queue with Array
        # tail = (head + 1) mod size
        # Time  complexity: O(1)
        # Space complexity: O(N), where N is the size of the circular queue.
        self.count += 1
        # calculate the new sum by shifting the window
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        # move on to the next head
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
# @lc code=end

