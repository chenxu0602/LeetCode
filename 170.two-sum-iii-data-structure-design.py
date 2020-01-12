#
# @lc app=leetcode id=170 lang=python3
#
# [170] Two Sum III - Data structure design
#
# https://leetcode.com/problems/two-sum-iii-data-structure-design/description/
#
# algorithms
# Easy (31.14%)
# Likes:    218
# Dislikes: 185
# Total Accepted:    67.1K
# Total Submissions: 211.2K
# Testcase Example:  '["TwoSum","add","add","add","find","find"]\n[[],[1],[3],[5],[4],[7]]'
#
# Design and implement a TwoSum class. It should support the following
# operations: add and find.
# 
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the
# value.
# 
# Example 1:
# 
# 
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false
# 
# 
# Example 2:
# 
# 
# add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false
# 
#

# @lc code=start
from collections import defaultdict

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.record = defaultdict(int)
        

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.record[number] += 1
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """

        return any(value - num in self.record and (value - num != num or self.record[num] > 1) for num in self.record)
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
# @lc code=end

