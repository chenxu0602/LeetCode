#
# @lc app=leetcode id=2502 lang=python3
#
# [2502] Design Memory Allocator
#

# @lc code=start
class Allocator:

    def __init__(self, n: int):
        self.blocks = [-1] * n
        self.n = n 

    def allocate(self, size: int, mID: int) -> int:
        available = 0
        for i in range(self.n):
            if self.blocks[i] == -1:
                available += 1
            else:
                available = 0 

            if available == size:
                for j in range(i - available + 1, i + 1):
                    self.blocks[j] = mID

                return i - available + 1

        return -1

    def free(self, mID: int) -> int:
        count = 0
        for i in range(self.n):
            if self.blocks[i] == mID:
                count += 1
                self.blocks[i] = -1
        return count
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
# @lc code=end

