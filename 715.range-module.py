#
# @lc app=leetcode id=715 lang=python3
#
# [715] Range Module
#
# https://leetcode.com/problems/range-module/description/
#
# algorithms
# Hard (35.85%)
# Likes:    303
# Dislikes: 25
# Total Accepted:    12.5K
# Total Submissions: 34.8K
# Testcase Example:  '["RangeModule","addRange","removeRange","queryRange","queryRange","queryRange"]\n' +
#
# A Range Module is a module that tracks ranges of numbers. Your task is to
# design and implement the following interfaces in an efficient manner.
# 
# addRange(int left, int right) Adds the half-open interval [left, right),
# tracking every real number in that interval.  Adding an interval that
# partially overlaps with currently tracked numbers should add any numbers in
# the interval [left, right) that are not already tracked.
# 
# queryRange(int left, int right) Returns true if and only if every real number
# in the interval [left, right)
# ⁠is currently being tracked.
# 
# removeRange(int left, int right) Stops tracking every real number currently
# being tracked in the interval [left, right).
# 
# Example 1:
# 
# addRange(10, 20): null
# removeRange(14, 16): null
# queryRange(10, 14): true (Every number in [10, 14) is being tracked)
# queryRange(13, 15): false (Numbers like 14, 14.03, 14.17 in [13, 15) are not
# being tracked)
# queryRange(16, 17): true (The number 16 in [16, 17) is still being tracked,
# despite the remove operation)
# 
# 
# 
# Note:
# A half open interval [left, right) denotes all real numbers left .
# 
# 0 < left < right < 10^9 in all calls to addRange, queryRange, removeRange.
# The total number of calls to addRange in a single test case is at most 1000.
# The total number of calls to queryRange in a single test case is at most
# 5000.
# The total number of calls to removeRange in a single test case is at most
# 1000.
# 
#
import bisect 

class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
#        The assumption is that the elements in self._X means [in, out, in, out, ...]
#        For example, if the elements in self._X is [1,2,3,4], then it represents the intervals [1, 2) \union [3, 4).
#        Thus by computing i % 2 we will know whether the new element falls in an existing interval or not.
#        (for example, if i % 2 == 0, then it falls out of an existing interval)

        i, j = bisect.bisect_left(self.ranges, left), bisect.bisect_right(self.ranges, right)
        self.ranges[i:j] = [left] * (i % 2 == 0) + [right] * (j % 2 == 0)
        

    def queryRange(self, left: int, right: int) -> bool:
        i, j = bisect.bisect_right(self.ranges, left), bisect.bisect_left(self.ranges, right)
        return i == j and i % 2 == 1
        

    def removeRange(self, left: int, right: int) -> None:
        i, j = bisect.bisect_left(self.ranges, left), bisect.bisect_right(self.ranges, right)
        self.ranges[i:j] = [left] * (i % 2 == 1) + [right] * (j % 2 == 1)
        


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)

