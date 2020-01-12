#
# @lc app=leetcode id=604 lang=python3
#
# [604] Design Compressed String Iterator
#
# https://leetcode.com/problems/design-compressed-string-iterator/description/
#
# algorithms
# Easy (34.99%)
# Likes:    174
# Dislikes: 76
# Total Accepted:    13.2K
# Total Submissions: 37.8K
# Testcase Example:  '["StringIterator","next","next","next","next","next","next","hasNext","next","hasNext"]\n' +
#
# 
# Design and implement a data structure for a compressed string iterator. It
# should support the following operations: next and hasNext.
# 
# 
# 
# The given compressed string will be in the form of each letter followed by a
# positive integer representing the number of this letter existing in the
# original uncompressed string.
# 
# 
# 
# next() - if the original string still has uncompressed characters, return the
# next letter; Otherwise return a white space.
# hasNext() - Judge whether there is any letter needs to be uncompressed.
# 
# 
# 
# Note:
# Please remember to RESET your class variables declared in StringIterator, as
# static/class variables are persisted across multiple test cases. Please see
# here for more details.
# 
# 
# 
# Example:
# 
# StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");
# 
# iterator.next(); // return 'L'
# iterator.next(); // return 'e'
# iterator.next(); // return 'e'
# iterator.next(); // return 't'
# iterator.next(); // return 'C'
# iterator.next(); // return 'o'
# iterator.next(); // return 'd'
# iterator.hasNext(); // return true
# iterator.next(); // return 'e'
# iterator.hasNext(); // return false
# iterator.next(); // return ' '
# 
# 
#
import re 

class StringIterator:

    def __init__(self, compressedString: str):
        self.__data = re.findall(r"([a-zA-Z])(\d+)", compressedString)
        self.__index, self.__count = -1, 0

    def next(self) -> str:
        if self.hasNext():
            self.__count -= 1
            return self.__data[self.__index][0]
        else:
            return ' '

        

    def hasNext(self) -> bool:
        if self.__count == 0 and self.__index + 1 < len(self.__data):
            self.__index += 1
            self.__count = int(self.__data[self.__index][1])
        return self.__count > 0
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()

