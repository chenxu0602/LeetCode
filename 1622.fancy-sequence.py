#
# @lc app=leetcode id=1622 lang=python3
#
# [1622] Fancy Sequence
#
# https://leetcode.com/problems/fancy-sequence/description/
#
# algorithms
# Hard (15.96%)
# Likes:    126
# Dislikes: 28
# Total Accepted:    2.3K
# Total Submissions: 14.5K
# Testcase Example:  '["Fancy","append","addAll","append","multAll","getIndex","addAll","append","multAll","getIndex","getIndex","getIndex"]\n' + '[[],[2],[3],[7],[2],[0],[3],[10],[2],[0],[1],[2]]'
#
# Write an API that generates fancy sequences using the append, addAll, and
# multAll operations.
# 
# Implement the Fancy class:
# 
# 
# Fancy() Initializes the object with an empty sequence.
# void append(val) Appends an integer val to the end of the sequence.
# void addAll(inc) Increments all existing values in the sequence by an integer
# inc.
# void multAll(m) Multiplies all existing values in the sequence by an integer
# m.
# int getIndex(idx) Gets the current value at index idx (0-indexed) of the
# sequence modulo 10^9 + 7. If the index is greater or equal than the length of
# the sequence, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["Fancy", "append", "addAll", "append", "multAll", "getIndex", "addAll",
# "append", "multAll", "getIndex", "getIndex", "getIndex"]
# [[], [2], [3], [7], [2], [0], [3], [10], [2], [0], [1], [2]]
# Output
# [null, null, null, null, null, 10, null, null, null, 26, 34, 20]
# 
# Explanation
# Fancy fancy = new Fancy();
# fancy.append(2);   // fancy sequence: [2]
# fancy.addAll(3);   // fancy sequence: [2+3] -> [5]
# fancy.append(7);   // fancy sequence: [5, 7]
# fancy.multAll(2);  // fancy sequence: [5*2, 7*2] -> [10, 14]
# fancy.getIndex(0); // return 10
# fancy.addAll(3);   // fancy sequence: [10+3, 14+3] -> [13, 17]
# fancy.append(10);  // fancy sequence: [13, 17, 10]
# fancy.multAll(2);  // fancy sequence: [13*2, 17*2, 10*2] -> [26, 34, 20]
# fancy.getIndex(0); // return 26
# fancy.getIndex(1); // return 34
# fancy.getIndex(2); // return 20
# 
# 
# 
# Constraints:
# 
# 
# 1 <= val, inc, m <= 100
# 0 <= idx <= 10^5
# At most 10^5 calls total will be made to append, addAll, multAll, and
# getIndex.
# 
# 
#

# @lc code=start
class Fancy:
    # The solution to this problem to compute the value only when requested to.
    # we keep track of the changes using two variables increment and mult
    # so the final calculation will be A[i] * mult +increment

    # So what happens if there is a addAll?
    # we just do increment+=val

    # What happens on multAll?
    # assume the value before multiplication is org
    # org = A[i] * mult +increment
    # we are multiplying by m, hence it will be
    # org = A[i] * (mult * m) + (increment * m)
    # comparing with our lazy formula, we see that we can just do mult*=m and increment*=m and continue

    # What if there is an append?
    # Now we cant just ignore this operation because the new value cannot be subject to the orginal formula. One way to solve it would be to just compute the values at this point and reset increment and mult but this would lead to a TLE. So we need a way to negate the final formula
    # so first we do newval - =increment and then newval/=mult. But as these are in modulo arthematic, the division changes to newval *= moduloInverse(mult)

    # How to calculate Modulo Inverse?
    # We know that 10^9+7 is prime and hence we can use Fermat's theorem to calculate inverse
    # a^(m-1) ≡ 1 (mod m)
    # If we multiply both sides with a^(-1), we get
    # a^(-1) ≡ a^(m-2) (mod m)
    # so we just need to calculate modPower(a, m-2)    

    def __init__(self):
        # Time  complexity: O(1)
        # Space complexity: O(N)
        self.A = []
        self.add = [0]
        self.mul = [1]

    def append(self, val: int) -> None:
        self.A.append(val)    
        self.add.append(self.add[-1])
        self.mul.append(self.mul[-1])

    def addAll(self, inc: int) -> None:
        self.add[-1] += inc        

    def multAll(self, m: int) -> None:
        self.add[-1] = self.add[-1] * m % (10**9 + 7) 
        self.mul[-1] = self.mul[-1] * m % (10**9 + 7) 

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.A): return -1   
        MOD = 10**9 + 7
        m = self.mul[-1] * pow(self.mul[idx], MOD - 2, MOD)
        inc = self.add[-1] - self.add[idx] * m
        return (self.A[idx] * m + inc) % MOD
        


# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
# @lc code=end

