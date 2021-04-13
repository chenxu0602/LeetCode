#
# @lc app=leetcode id=1825 lang=python3
#
# [1825] Finding MK Average
#
# https://leetcode.com/problems/finding-mk-average/description/
#
# algorithms
# Hard (28.35%)
# Likes:    59
# Dislikes: 45
# Total Accepted:    2.3K
# Total Submissions: 8K
# Testcase Example:  '["MKAverage","addElement","addElement","calculateMKAverage","addElement","calculateMKAverage","addElement","addElement","addElement","calculateMKAverage"]\n' + '[[3,1],[3],[1],[],[10],[],[5],[5],[5],[]]'
#
# You are given two integers, m and k, and a stream of integers. You are tasked
# to implement a data structure that calculates the MKAverage for the stream.
# 
# The MKAverage can be calculated using these steps:
# 
# 
# If the number of the elements in the stream is less than m you should
# consider the MKAverage to be -1. Otherwise, copy the last m elements of the
# stream to a separate container.
# Remove the smallest k elements and the largest k elements from the
# container.
# Calculate the average value for the rest of the elements rounded down to the
# nearest integer.
# 
# 
# Implement the MKAverage class:
# 
# 
# MKAverage(int m, int k) Initializes the MKAverage object with an empty stream
# and the two integers m and k.
# void addElement(int num) Inserts a new element num into the stream.
# int calculateMKAverage() Calculates and returns the MKAverage for the current
# stream rounded down to the nearest integer.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MKAverage", "addElement", "addElement", "calculateMKAverage", "addElement",
# "calculateMKAverage", "addElement", "addElement", "addElement",
# "calculateMKAverage"]
# [[3, 1], [3], [1], [], [10], [], [5], [5], [5], []]
# Output
# [null, null, null, -1, null, 3, null, null, null, 5]
# 
# Explanation
# MKAverage obj = new MKAverage(3, 1); 
# obj.addElement(3);        // current elements are [3]
# obj.addElement(1);        // current elements are [3,1]
# obj.calculateMKAverage(); // return -1, because m = 3 and only 2 elements
# exist.
# obj.addElement(10);       // current elements are [3,1,10]
# obj.calculateMKAverage(); // The last 3 elements are [3,1,10].
# ⁠                         // After removing smallest and largest 1 element
# the container will be [3].
# ⁠                         // The average of [3] equals 3/1 = 3, return 3
# obj.addElement(5);        // current elements are [3,1,10,5]
# obj.addElement(5);        // current elements are [3,1,10,5,5]
# obj.addElement(5);        // current elements are [3,1,10,5,5,5]
# obj.calculateMKAverage(); // The last 3 elements are [5,5,5].
# ⁠                         // After removing smallest and largest 1 element
# the container will be [5].
# ⁠                         // The average of [5] equals 5/1 = 5, return 5
# 
# 
# 
# Constraints:
# 
# 
# 3 <= m <= 10^5
# 1 <= k*2 < m
# 1 <= num <= 10^5
# At most 10^5 calls will be made to addElement and calculateMKAverage.
# 
# 
#

# @lc code=start
import heapq

class MKAverage:

    def __init__(self, m: int, k: int):
      self.m, self.k = m, k
      self.arr = [0] * m
      self.lh1, self.rh1 = self.heap_init(m, k)
      self.lh2, self.rh2 = self.heap_init(m, m - k)
      self.score = 0

    def heap_init(self, p1, p2):
      h1 = [(0, i) for i in range(p1 - p2, p1)]
      h2 = [(0, i) for i in range(p1 - p2)]
      heapq.heapify(h1)
      heapq.heapify(h2)
      return h1, h2

    def update(self, lh, rh, m, k, num):
      score, T = 0, len(self.arr)
      if num >= rh[0][0]:
        heapq.heappush(rh, (num, T))
        if self.arr[T - m] < rh[0][0]:
          if rh[0][1] > T - m:
            score += rh[0][0]
          score -= self.arr[T - m]
          heapq.heappush(lh, (-rh[0][0], rh[0][1]))
          heapq.heappop(rh)
      else:
        heapq.heappush(lh, (-num, T))
        score += num
        if self.arr[T - m] >= rh[0][0]:
          heapq.heappush(rh, (-lh[0][0], lh[0][1]))
          q = heapq.heappop(lh)
          score += q[0]
        else:
          score -= self.arr[T - m]

      while lh and lh[0][1] <= T - m:
        heapq.heappop(lh)

      while rh and rh[0][1] <= T - m:
        heapq.heappop(rh)

      return score

    def addElement(self, num: int) -> None:
      t1 = self.update(self.lh1, self.rh1, self.m, self.k, num)
      t2 = self.update(self.lh2, self.rh2, self.m, self.m - self.k, num)
      self.arr.append(num)
      self.score += (t2 - t1)

    def calculateMKAverage(self) -> int:
      if len(self.arr) < 2 * self.m:
        return -1
      return self.score // (self.m - 2 * self.k)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()
# @lc code=end

