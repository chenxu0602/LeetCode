#
# @lc app=leetcode id=731 lang=python3
#
# [731] My Calendar II
#
# https://leetcode.com/problems/my-calendar-ii/description/
#
# algorithms
# Medium (45.16%)
# Likes:    396
# Dislikes: 62
# Total Accepted:    26.5K
# Total Submissions: 58.1K
# Testcase Example:  '["MyCalendarTwo","book","book","book","book","book","book"]\n' +
#
# Implement a MyCalendarTwo class to store your events. A new event can be
# added if adding the event will not cause a triple booking.
# 
# Your class will have one method, book(int start, int end). Formally, this
# represents a booking on the half open interval [start, end), the range of
# real numbers x such that start <= x < end.
# 
# A triple booking happens when three events have some non-empty intersection
# (ie., there is some time that is common to all 3 events.)
# 
# For each call to the method MyCalendar.book, return true if the event can be
# added to the calendar successfully without causing a triple booking.
# Otherwise, return false and do not add the event to the calendar.
# Your class will be called like this: MyCalendar cal = new MyCalendar();
# MyCalendar.book(start, end)
# 
# Example 1:
# 
# 
# MyCalendar();
# MyCalendar.book(10, 20); // returns true
# MyCalendar.book(50, 60); // returns true
# MyCalendar.book(10, 40); // returns true
# MyCalendar.book(5, 15); // returns false
# MyCalendar.book(5, 10); // returns true
# MyCalendar.book(25, 55); // returns true
# Explanation: 
# The first two events can be booked.  The third event can be double booked.
# The fourth event (5, 15) can't be booked, because it would result in a triple
# booking.
# The fifth event (5, 10) can be booked, as it does not use time 10 which is
# already double booked.
# The sixth event (25, 55) can be booked, as the time in [25, 40) will be
# double booked with the third event;
# the time [40, 50) will be single booked, and the time [50, 55) will be double
# booked with the second event.
# 
# 
# 
# 
# Note:
# 
# 
# The number of calls to MyCalendar.book per test case will be at most
# 1000.
# In calls to MyCalendar.book(start, end), start and end are integers in the
# range [0, 10^9].
# 
# 
# 
#
import bisect

class MyCalendarTwo:

    def __init__(self):
        self.one = []
        self.two = []

    def is_valid(self, start, end):
        if end <= start:
            return -1

        i = bisect.bisect_right(self.two, start)
        if i % 2:
            return -1

        j = bisect.bisect_left(self.two, end)
        if i != j:
            return -1

        return i
        

    def book(self, start: int, end: int) -> bool:

        """
        t = self.is_valid(start, end)
        if t == -1:
            return False

        i = bisect.bisect_right(self.one, start)
        j = bisect.bisect_left(self.one, end)

        if i % 2:
            if j % 2:
                self.two[t:t] = [start] + self.one[i:j] + [end]
                self.one[i:j] = []
            else:
                self.two[t:t] = [start] + self.one[i:j]
                self.one[i:j] = [end]
        else:
            if j % 2:
                self.two[t:t] = self.one[i:j] + [end]
                self.one[i:j] = [start]
            else:
                self.two[t:t] = self.one[i:j]
                self.one[i:j] = [start, end]

        return True
        """

        for i, j in self.two:
            if start < j and end > i:
                return False
        for i, j in self.one:
            if start < j and end > i:
                self.two.append((max(start, i), min(end, j)))
        self.one.append((start, end))
        return True


        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)

