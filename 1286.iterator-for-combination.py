#
# @lc app=leetcode id=1286 lang=python3
#
# [1286] Iterator for Combination
#
# https://leetcode.com/problems/iterator-for-combination/description/
#
# algorithms
# Medium (64.96%)
# Likes:    88
# Dislikes: 10
# Total Accepted:    4.5K
# Total Submissions: 7K
# Testcase Example:  '["CombinationIterator","next","hasNext","next","hasNext","next","hasNext"]\r' + '\n[["abc",2],[],[],[],[],[],[]]\r'
#
# Design an Iterator class, which has:
# 
# 
# A constructor that takes a string characters of sorted distinct lowercase
# English letters and a number combinationLength as arguments.
# A function next() that returns the next combination of length
# combinationLength in lexicographical order.
# A function hasNext() that returns True if and only if there exists a next
# combination.
# 
# 
# 
# 
# Example:
# 
# 
# CombinationIterator iterator = new CombinationIterator("abc", 2); // creates
# the iterator.
# 
# iterator.next(); // returns "ab"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "ac"
# iterator.hasNext(); // returns true
# iterator.next(); // returns "bc"
# iterator.hasNext(); // returns false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= combinationLength <= characters.length <= 15
# There will be at most 10^4 function calls per test.
# It's guaranteed that all calls of the function next are valid.
# 
# 
#

# @lc code=start
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        # Backtracking
        # Time  complexity: O(k x C(k, N))
        # Space compleixty: O(C(k, N))
        # self.c = characters
        # self.n = combinationLength
        # self.i = 0
        # self.ans = []
        # self.permute("", 0)

        # Bitmasking: Precomputation
        # Time  complexity: O(2^N x N) to generate 2^N bitmasks and then count a number of bits set in each bitmask in O(N) time. O(1) runtime.
        # Space complexity: O(k x C(k, N)) to keep C(k, N) combinations of length k.
        # self.combinations = []
        # n, k = len(characters), combinationLength

        # # generate bitmasks from 0..00 to 1..11  
        # for bitmask in range(1 << n):
        #     # use bitmasks with k 1-bits
        #     if bin(bitmask).count('1') == k:
        #         # convert bitmask into combination
        #         # 111 --> "abc", 000 --> ""
        #         # 110 --> "ab", 101 --> "ac", 011 --> "bc"
        #         curr = [characters[j] for j in range(n) if bitmask & (1 << n - j - 1)]
        #         self.combinations.append(''.join(curr))


        # Bitmasking: Next Combination
        # Time  complexity: O(2^N x N / C(k, N)) in average.
        # Space complexity: O(k)
        self.n = n = len(characters)
        self.k = k = combinationLength
        self.chars = characters

        # generate first bitmask 1(k)0(n - k)
        self.b = (1 << n) - (1 << n - k)


        # Algorithm L by D. E. Knuth: Lexicographic Combinations: Precomputation
        # Time  complexity: O(k x C(k, N))
        # Space complexity: O(k x C(k, N))
        # self.combinations = []
        # n, k = len(characters), combinationLength

        # # init the first combination
        # nums = list(range(k)) + [n]

        # j = 0
        # while j < k:
        #     # add current combination
        #     curr = [characters[n - 1 - nums[i]] for i in range(k - 1, -1, -1)]
        #     self.combinations.append(''.join(curr))

        #     # Generate next combination.
        #     # Find the first j such that nums[j] + 1 != nums[j + 1].
        #     # Increase nums[j] by one.
        #     j = 0
        #     while j < k and nums[j + 1] == nums[j] + 1:
        #         nums[j] = j
        #         j += 1
        #     nums[j] += 1


        # Algorithm L by D. E. Knuth: Lexicographic Combinations: Next Combination
        # Time  complexity: O(k) both for init() and next() functions. The algorithm generates a new combination from the previous one in O(k) time.
        # Space complexity: O(k)
        # self.n = len(characters)
        # self.k = k = combinationLength
        # self.chars = characters

        # # init the first combination
        # self.nums = list(range(k))
        # self.has_next = True


    def permute(self, s: str, start: int) -> None:
        # Backtracking
        # Time  complexity: O(k x C(k, N))
        # Space compleixty: O(C(k, N))
        if len(s) == self.n:
            self.ans.append(s)
            return 
        else:
            for i in range(start, len(self.c)):
                self.permute(s + self.c[i], i + 1)
        
    def next(self) -> str:
        # Backtracking
        # Time  complexity: O(k x C(k, N))
        # Space compleixty: O(C(k, N))
        # ans = self.ans[self.i]
        # self.i += 1
        # return ans
        
        # generate bitmasks from 0..00 to 1..11  
        # Time  complexity: O(2^N x N) to generate 2^N bitmasks and then count a number of bits set in each bitmask in O(N) time. O(1) runtime.
        # Space complexity: O(k x C(k, N)) to keep C(k, N) combinations of length k.
        # return self.combinations.pop()

        # Bitmasking: Next Combination
        # Time  complexity: O(2^N x N / C(k, N)) in average.
        # Space complexity: O(k)
        # convert bitmasks into combinations
        # 111 --> "abc", 000 --> ""
        # 110 --> "ab", 101 --> "ac", 011 --> "bc"
        curr = [self.chars[j] for j in range(self.n) if self.b & (1 << self.n - j - 1)]

        # generate next bitmask
        self.b -= 1
        while self.b > 0 and bin(self.b).count('1') != self.k:
            self.b -= 1

        return ''.join(curr)


        # Algorithm L by D. E. Knuth: Lexicographic Combinations: Precomputation
        # Time  complexity: O(k x C(k, N))
        # Space complexity: O(k x C(k, N))
        # return self.combinations.pop()


        # Algorithm L by D. E. Knuth: Lexicographic Combinations: Next Combination
        # Time  complexity: O(k) both for init() and next() functions. The algorithm generates a new combination from the previous one in O(k) time.
        # Space complexity: O(k)
        nums = self.nums
        n, k = self.n, self.k
        curr = [self.chars[j] for j in nums]

        # Generate next combination.
        # Find the first j such that nums[j] != n - k + j.
        # Increase nums[j] by one.
        # j = k - 1
        # while j >= 0 and nums[j] == n - k + j:
        #     j -= 1
        # nums[j] += 1

        # if j >= 0:
        #     for i in range(j + 1, k):
        #         nums[i] = nums[j] + i - j
        # else:
        #     self.has_next = False

        # return ''.join(curr)

    def hasNext(self) -> bool:
        # Backtracking
        # Time  complexity: O(k x C(k, N))
        # Space compleixty: O(C(k, N))
        # return self.i < len(self.ans)
        
        # generate bitmasks from 0..00 to 1..11  
        # Time  complexity: O(2^N x N) to generate 2^N bitmasks and then count a number of bits set in each bitmask in O(N) time. O(1) runtime.
        # Space complexity: O(k x C(k, N)) to keep C(k, N) combinations of length k.
        # return self.combinations

        # Bitmasking: Next Combination
        # Time  complexity: O(2^N x N / C(k, N)) in average.
        # Space complexity: O(k)
        return self.b > 0

        # Algorithm L by D. E. Knuth: Lexicographic Combinations: Precomputation
        # Time  complexity: O(k x C(k, N))
        # Space complexity: O(k x C(k, N))
        # return self.combinations


        # Algorithm L by D. E. Knuth: Lexicographic Combinations: Next Combination
        # Time  complexity: O(k) both for init() and next() functions. The algorithm generates a new combination from the previous one in O(k) time.
        # Space complexity: O(k)
        # return self.has_next

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# @lc code=end

