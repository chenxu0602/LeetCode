#
# @lc app=leetcode id=346 lang=python3
#
# [346] Moving Average from Data Stream
#
# https://leetcode.com/problems/moving-average-from-data-stream/description/
#
# algorithms
# Easy (66.38%)
# Likes:    298
# Dislikes: 34
# Total Accepted:    79.2K
# Total Submissions: 119K
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

from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """

        """
        self.values = []
        self.size = size
        """

        self.size = size
        self.queue = [0] * self.size
        self.head = self.window_sum = 0
        self.count = 0
        

    def next(self, val: int) -> float:

        """
        self.values.append(val)

        if len(self.values) > self.size:
            self.values.pop(0)

        return 1.0 * sum(self.values) / len(self.values)
        """

        self.count += 1
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.queue[tail] + val
        self.head = (self.head + 1) % self.size
        self.queue[self.head] = val
        return self.window_sum / min(self.size, self.count)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

