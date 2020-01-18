#
# @lc app=leetcode id=352 lang=python3
#
# [352] Data Stream as Disjoint Intervals
#
# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
#
# algorithms
# Hard (43.53%)
# Likes:    185
# Dislikes: 57
# Total Accepted:    24.4K
# Total Submissions: 56K
# Testcase Example:  '["SummaryRanges","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals","addNum","getIntervals"]\n' +
#
# Given a data stream input of non-negative integers a1, a2, ..., an, ...,
# summarize the numbers seen so far as a list of disjoint intervals.
# 
# For example, suppose the integers from the data stream are 1, 3, 7, 2, 6,
# ..., then the summary will be:
# 
# 
# [1, 1]
# [1, 1], [3, 3]
# [1, 1], [3, 3], [7, 7]
# [1, 3], [7, 7]
# [1, 3], [6, 7]
# 
# 
# Follow up:
# What if there are lots of merges and the number of disjoint intervals are
# small compared to the data stream's size?
# 
# NOTE: input types have been changed on April 15, 2019. Please reset to
# default code definition to get new method signature.
# 
#
import bisect


class SummaryRanges:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.intervals = []

    def addNum(self, val: int) -> None:
        pos = bisect.bisect_right([i[0] for i in self.intervals], val) - 1
        if 0 <= pos < len(self.intervals) and self.intervals[pos][0] <= val <= self.intervals[pos][1]:
            return

        pos += 1
        self.intervals.insert(pos, [val, val])

        if pos + 1 < len(self.intervals) and self.intervals[pos+1][0] == val + 1:
            self.intervals[pos][1] = self.intervals[pos+1][1]
            self.intervals.pop(pos+1)

        if pos - 1 >= 0 and self.intervals[pos-1][1] == val - 1:
            self.intervals[pos-1][1] = self.intervals[pos][1]
            self.intervals.pop(pos)


    def getIntervals(self):

        return self.intervals


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()

