#
# @lc app=leetcode id=251 lang=python3
#
# [251] Flatten 2D Vector
#
# https://leetcode.com/problems/flatten-2d-vector/description/
#
# algorithms
# Medium (44.99%)
# Likes:    319
# Dislikes: 168
# Total Accepted:    69.4K
# Total Submissions: 154.3K
# Testcase Example:  '["Vector2D","next","next","next","hasNext","hasNext","next","hasNext"]\n' + '[[[[1,2],[3],[4]]],[null],[null],[null],[null],[null],[null],[null]]'
#
# Design and implement an iterator to flatten a 2d vector. It should support
# the following operations: next and hasNext.
# 
# 
# 
# Example:
# 
# 
# Vector2D iterator = new Vector2D([[1,2],[3],[4]]);
# 
# iterator.next(); // return 1
# iterator.next(); // return 2
# iterator.next(); // return 3
# iterator.hasNext(); // return true
# iterator.hasNext(); // return true
# iterator.next(); // return 4
# iterator.hasNext(); // return false
# 
# 
# 
# 
# Notes:
# 
# 
# Please remember to RESET your class variables declared in Vector2D, as
# static/class variables are persisted across multiple test cases. Please see
# here for more details.
# You may assume that next() call will always be valid, that is, there will be
# at least a next element in the 2d vector when next() is called.
# 
# 
# 
# 
# Follow up:
# 
# As an added challenge, try to code it using only iterators in C++ or
# iterators in Java.
# 
#

# @lc code=start
class Vector2D:

    def __init__(self, v: List[List[int]]):
        # O(N + V)
        # O(N)
        # self.nums = []
        # for inner_list in v:
        #     for num in inner_list:
        #         self.nums.append(num)
        # self.position = -1
        

        # O(1)
        self.vector = v
        self.inner = 0
        self.outer = 0

    # If the current outer and inner point to an integer, this method does nothing.
    # Otherwise, inner and outer are advanced until they point to an integer.
    # If there are no more integers, then outer will be equal to vector.length
    # when this method terminates.
    def advance_to_next(self):
        # While outer is still within the vector, but inner is over the 
        # end of the inner list pointed to by outer, we want to move
        # forward to the start of the next inner vector.
        # O(V/N)
        while self.outer < len(self.vector) and self.inner == len(self.vector[self.outer]):
            self.outer += 1
            self.inner = 0
        

    def next(self) -> int:
        # self.position += 1
        # return self.nums[self.position]


        # Ensure the position pointers are moved such they point to an integer,
        # or put outer = vector.length.
        # O(V/N) or O(1)
        self.advance_to_next()
        # Return current element and move inner so that is after the current
        # element.
        result = self.vector[self.outer][self.inner]
        self.inner += 1
        return result
        

    def hasNext(self) -> bool:
        # return self.position + 1 < len(self.nums)

        
        # Ensure the position pointers are moved such they point to an integer,
        # or put outer = vector.length.
        # O(V/N) or O(1)
        self.advance_to_next()
        # If outer = vector.length then there are no integers left, otherwise
        # we've stopped at an integer and so there's an integer left.
        return self.outer < len(self.vector)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

