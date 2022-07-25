#
# @lc app=leetcode id=2336 lang=python3
#
# [2336] Smallest Number in Infinite Set
#

# @lc code=start
import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.index, self.heap = 1, []

    def popSmallest(self) -> int:
        if self.heap:
            return heapq.heappop(self.heap)        

        self.index += 1
        return self.index - 1

    def addBack(self, num: int) -> None:
        if self.index > num and num not in self.heap:
            heapq.heappush(self.heap, num) 


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
# @lc code=end

