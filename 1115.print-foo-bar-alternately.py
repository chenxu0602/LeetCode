#
# @lc app=leetcode id=1115 lang=python3
#
# [1115] Print FooBar Alternately
#
# https://leetcode.com/problems/print-foobar-alternately/description/
#
# concurrency
# Medium (58.49%)
# Likes:    295
# Dislikes: 25
# Total Accepted:    29.5K
# Total Submissions: 50.2K
# Testcase Example:  '1'
#
# Suppose you are given the following code:
# 
# 
# class FooBar {
# ⁠ public void foo() {
# for (int i = 0; i < n; i++) {
# print("foo");
# }
# ⁠ }
# 
# ⁠ public void bar() {
# for (int i = 0; i < n; i++) {
# print("bar");
# }
# ⁠ }
# }
# 
# 
# The same instance of FooBar will be passed to two different threads. Thread A
# will call foo() while thread B will call bar(). Modify the given program to
# output "foobar" n times.
# 
# 
# 
# Example 1:
# 
# 
# Input: n = 1
# Output: "foobar"
# Explanation: There are two threads being fired asynchronously. One of them
# calls foo(), while the other calls bar(). "foobar" is being output 1 time.
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: "foobarfoobar"
# Explanation: "foobar" is being output 2 times.
# 
# 
#

# @lc code=start
from threading import Semaphore, Barrier, Lock

class FooBar:
    def __init__(self, n):
        self.n = n

        # self.foo_gate = Semaphore(1)
        # self.bar_gate = Semaphore(0)

        # self.barrier = Barrier(2)

        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        # for i in range(self.n):
        #     self.foo_gate.acquire()
        #     printFoo()
        #     self.bar_gate.release()

        # for i in range(self.n):
        #     printFoo()
        #     self.barrier.wait()

        for i in range(self.n):
            self.foo_lock.acquire()
            printFoo()
            self.bar_lock.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        # for i in range(self.n):
        #     self.bar_gate.acquire()   
        #     printBar()
        #     self.foo_gate.release()

        # for i in range(self.n):
        #     self.barrier.wait()
        #     printBar()

        for i in range(self.n):
            self.bar_lock.acquire()
            printBar()
            self.foo_lock.release()
# @lc code=end

