#
# @lc app=leetcode id=187 lang=python3
#
# [187] Repeated DNA Sequences
#
# https://leetcode.com/problems/repeated-dna-sequences/description/
#
# algorithms
# Medium (36.64%)
# Likes:    524
# Dislikes: 211
# Total Accepted:    138.4K
# Total Submissions: 372.8K
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

        """
        record, r, n = set(), set(), len(s)

        for i in range(n-9):
            substring = s[i:i+10]
            [record, r][substring in record].add(substring)

        return list(r)
        """

        """
        L, n = 10, len(s)
        if n <= L:
            return []

        a = 4
        aL = pow(a, L)

        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int.get(s[i]) for i in range(n)]

        h = 0
        seen, output = set(), set()

        for start in range(n-L+1):
            if start != 0:
                h = h * a - nums[start-1] * aL + nums[start+L-1]
            else:
                for i in range(L):
                    h = h * a + nums[i]

            if h in seen:
                output.add(s[start:start+L])
            seen.add(h)

        return output
        """

        L, n = 10, len(s)
        if n <= L:
            return []

        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int.get(s[i]) for i in range(n)]

        bitmask = 0
        seen, output = set(), set()

        for start in range(n-L+1):
            if start != 0:
                bitmask <<= 2
                bitmask |= nums[start+L-1]
                bitmask &= ~(3 << 2 * L)
            else:
                for i in range(L):
                    bitmask <<= 2
                    bitmask |= nums[i]

            if bitmask in seen:
                output.add(s[start:start+L])
            seen.add(bitmask)

        return output


        
# @lc code=end

