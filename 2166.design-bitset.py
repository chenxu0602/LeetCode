#
# @lc app=leetcode id=2166 lang=python3
#
# [2166] Design Bitset
#

# @lc code=start
class Bitset:

    def __init__(self, size: int):
        self.a = 0
        self.size = size
        self.cnt = 0
        

    def fix(self, idx: int) -> None:
        if self.a & (1 << idx) == 0:
            self.a |= 1 << idx
            self.cnt += 1
        

    def unfix(self, idx: int) -> None:
        if self.a & (1 << idx):
            self.a ^= 1 << idx
            self.cnt -= 1
        

    def flip(self) -> None:
        self.a ^= (1 << self.size) - 1
        self.cnt = self.size - self.cnt
        

    def all(self) -> bool:
        return self.cnt == self.size
        

    def one(self) -> bool:
        return self.a > 0
        

    def count(self) -> int:
        return self.cnt
        

    def toString(self) -> str:
        a = bin(self.a)[2:]
        return a[::-1] + '0' * (self.size - len(a))
        


# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()
# @lc code=end

