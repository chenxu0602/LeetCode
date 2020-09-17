#
# @lc app=leetcode id=855 lang=python3
#
# [855] Exam Room
#
# https://leetcode.com/problems/exam-room/description/
#
# algorithms
# Medium (43.01%)
# Likes:    614
# Dislikes: 252
# Total Accepted:    32.4K
# Total Submissions: 74.9K
# Testcase Example:  '["ExamRoom","seat","seat","seat","seat","leave","seat"]\n' + '[[10],[],[],[],[],[4],[]]'
#
# In an exam room, there are N seats in a single row, numbered 0, 1, 2, ...,
# N-1.
# 
# When a student enters the room, they must sit in the seat that maximizes the
# distance to the closest person.  If there are multiple such seats, they sit
# in the seat with the lowest number.  (Also, if no one is in the room, then
# the student sits at seat number 0.)
# 
# Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat()
# returning an int representing what seat the student sat in, and
# ExamRoom.leave(int p) representing that the student in seat number p now
# leaves the room.  It is guaranteed that any calls to ExamRoom.leave(p) have a
# student sitting in seat p.
# 
# 
# 
# Example 1:
# 
# 
# Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"],
# [[10],[],[],[],[],[4],[]]
# Output: [null,0,9,4,2,null,5]
# Explanation:
# ExamRoom(10) -> null
# seat() -> 0, no one is in the room, then the student sits at seat number 0.
# seat() -> 9, the student sits at the last seat number 9.
# seat() -> 4, the student sits at the last seat number 4.
# seat() -> 2, the student sits at the last seat number 2.
# leave(4) -> null
# seat() -> 5, the student sits at the last seat number 5.
# 
# 
# ​​​​​​​
# 
# Note:
# 
# 
# 1 <= N <= 10^9
# ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across
# all test cases.
# Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting
# in seat number p.
# 
# 
#

# @lc code=start
import bisect 

class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.students = []

    def seat(self) -> int:

        # Let's determine student, the position of the next
        # student to sit down.

        if not self.students:
            self.students = [0]
            return 0

        # Tenatively, dist is the distance to the closest student,
        # which is achieved by sitting in the position 'student'.
        # We start by considering the left-most seat.
        dist, student = self.students[0], 0
        for i, s in enumerate(self.students):
            if i:
                prev = self.students[i - 1]
                # For each pair of adjacent students in positions (prev, s),
                # d is the distance to the closest student;
                # achieved at position prev + d.
                d = (s - prev) // 2
                if d > dist:
                    dist, student = d, prev + d

            # Considering the right-most seat.
            d = self.N - 1 - self.students[-1]
            if d > dist:
                student = self.N - 1


        # Add the student to our sorted list of positions.
        bisect.insort(self.students, student)
        return student

    def leave(self, p: int) -> None:
        self.students.remove(p)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
# @lc code=end

