#
# @lc app=leetcode id=362 lang=python3
#
# [362] Design Hit Counter
#
# https://leetcode.com/problems/design-hit-counter/description/
#
# algorithms
# Medium (63.52%)
# Likes:    759
# Dislikes: 78
# Total Accepted:    88.3K
# Total Submissions: 138.7K
# Testcase Example:  '["HitCounter","hit","hit","hit","getHits","hit","getHits","getHits"]\n' + '[[],[1],[2],[3],[4],[300],[300],[301]]'
#
# Design a hit counter which counts the number of hits received in the past 5
# minutes.
# 
# Each function accepts a timestamp parameter (in seconds granularity) and you
# may assume that calls are being made to the system in chronological order
# (ie, the timestamp is monotonically increasing). You may assume that the
# earliest timestamp starts at 1.
# 
# It is possible that several hits arrive roughly at the same time.
# 
# Example:
# 
# 
# HitCounter counter = new HitCounter();
# 
# // hit at timestamp 1.
# counter.hit(1);
# 
# // hit at timestamp 2.
# counter.hit(2);
# 
# // hit at timestamp 3.
# counter.hit(3);
# 
# // get hits at timestamp 4, should return 3.
# counter.getHits(4);
# 
# // hit at timestamp 300.
# counter.hit(300);
# 
# // get hits at timestamp 300, should return 4.
# counter.getHits(300);
# 
# // get hits at timestamp 301, should return 3.
# counter.getHits(301); 
# 
# 
# Follow up:
# What if the number of hits per second could be very large? Does your design
# scale?
#

# @lc code=start
from collections import deque 

class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_of_hits = 0
        self.time_hits = deque()
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        if not self.num_of_hits or self.time_hits[-1][0] != timestamp:
            self.time_hits.append([timestamp, 1])
        else:
            self.time_hits[-1][1] += 1

        self.num_of_hits += 1
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.num_of_hits and self.time_hits[0][0] <= timestamp - 300:
            self.num_of_hits -= self.time_hits.popleft()[1]

        return self.num_of_hits
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
# @lc code=end

