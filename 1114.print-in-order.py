#
# @lc app=leetcode id=1114 lang=python3
#
# [1114] Print in Order
#
# https://leetcode.com/problems/print-in-order/description/
#
# concurrency
# Easy (65.64%)
# Likes:    576
# Dislikes: 103
# Total Accepted:    60.6K
# Total Submissions: 91.4K
# Testcase Example:  '[1,2,3]'
#
# Suppose we have a class:
# 
# 
# public class Foo {
# public void first() { print("first"); }
# public void second() { print("second"); }
# public void third() { print("third"); }
# }
# 
# 
# The same instance of Foo will be passed to three different threads. Thread A
# will call first(), thread B will call second(), and thread C will call
# third(). Design a mechanism and modify the program to ensure that second() is
# executed after first(), and third() is executed after second().
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: "firstsecondthird"
# Explanation: There are three threads being fired asynchronously. The input
# [1,2,3] means thread A calls first(), thread B calls second(), and thread C
# calls third(). "firstsecondthird" is the correct output.
# 
# 
# Example 2:
# 
# 
# Input: [1,3,2]
# Output: "firstsecondthird"
# Explanation: The input [1,3,2] means thread A calls first(), thread B calls
# third(), and thread C calls second(). "firstsecondthird" is the correct
# output.
# 
# 
# 
# Note:
# 
# We do not know how the threads will be scheduled in the operating system,
# even though the numbers in the input seems to imply the ordering. The input
# format you see is mainly to ensure our tests' comprehensiveness.
# 
#

# @lc code=start
from threading import Lock, Semaphore

class Foo:
    def __init__(self):
        # self.firstJobDone = Lock()
        # self.secondJobDone = Lock()
        # self.firstJobDone.acquire()
        # self.secondJobDone.acquire()

        self.two = Semaphore(0)
        self.three = Semaphore(0)

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.

        # printFirst()
        # self.firstJobDone.release()

        printFirst()
        self.two.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.

        # with self.firstJobDone:
        #     printSecond()
        #     self.secondJobDone.release()

        with self.two:
            printSecond()
            self.three.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.

        # with self.secondJobDone:
        #     printThird()

        with self.three:
            printThird()
# @lc code=end

