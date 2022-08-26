#
# @lc app=leetcode id=2349 lang=python3
#
# [2349] Design a Number Container System
#

# @lc code=start
from collections import defaultdict
from sortedcontainers import SortedList

class NumberContainers:

    def __init__(self):
        self.num_to_indices = defaultdict(SortedList)
        self.idx_to_num = {}

    def change(self, index: int, number: int) -> None:
        if index in self.idx_to_num:
            old = self.idx_to_num[index]
            self.num_to_indices[old].discard(index) 
            if not self.num_to_indices[old]:
                del self.num_to_indices[old]
        self.num_to_indices[number].add(index)
        self.idx_to_num[index] = number

    def find(self, number: int) -> int:
        if number in self.num_to_indices:
            return self.num_to_indices[number][0]        
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
# @lc code=end

