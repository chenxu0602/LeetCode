#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (38.78%)
# Likes:    745
# Dislikes: 276
# Total Accepted:    163.1K
# Total Submissions: 420K
# Testcase Example:  '"AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"'
#
# All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
# for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to
# identify repeated sequences within the DNA.
# 
# Write a function to find all the 10-letter-long sequences (substrings) that
# occur more than once in a DNA molecule.
# 
# Example:
# 
# 
# Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
# 
# Output: ["AAAAACCCCC", "CCCCCAAAAA"]
# 
# 
#

# @lc code=start
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        # Linear-time Slice Using Substring + HashSet
        # Time  complexity: O((N-L)L)
        # Space complexity: O((N-L)L)
        # L, n = 10, len(s)
        # seen, output = set(), set()

        # for start in range(n - L + 1):
        #     tmp = s[start:start + L]
        #     if tmp in seen:
        #         output.add(tmp[:])
        #     seen.add(tmp)
        # return output

        # Rabin-Karp : Constant-time Slice Using Rolling Hash
        # Time  complexity: O((N-L))
        # Space complexity: O((N-L))
        # L, n = 10, len(s)
        # if n <= L:
        #     return []

        # a = 4
        # aL = pow(a, L)

        # to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        # nums = [to_int.get(s[i]) for i in range(n)]

        # h = 0
        # seen, output = set(), set()

        # for start in range(n - L + 1):
        #     # compute hash of the current sequence in O(1) time
        #     if start != 0:
        #         h = h * a - nums[start - 1] * aL + nums[start + L - 1]
        #     else:
        #         for i in range(L):
        #             h = h * a + nums[i]
        #     if h in seen:
        #         output.add(s[start:start + L])
        #     seen.add(h)
        # return output

        # Bit Manipulation : Constant-time Slice Using Bitmask
        # Time  complexity: O((N-L))
        # Space complexity: O((N-L))
        L, n = 10, len(s)
        if n <= L:
            return []

        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int.get(s[i]) for i in range(n)]

        bitmask = 0
        seen, output = set(), set()

        for start in range(n - L + 1):
            if start != 0:
                # left shift to free the last 2 bit
                bitmask <<= 2
                # add a new 2-bits number in the last two bits
                bitmask |= nums[start + L - 1]
                # unset first two bits: 2L-bit and (2L + 1)-bit
                bitmask &= ~(3 << 2 * L)
            else:
                for i in range(L):
                    bitmask <<= 2
                    bitmask |= nums[i]
            if bitmask in seen:
                output.add(s[start:start + L])
            seen.add(bitmask)
        return output
        

        
# @lc code=end

