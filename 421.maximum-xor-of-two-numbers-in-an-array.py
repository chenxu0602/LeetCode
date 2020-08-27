#
# @lc app=leetcode id=421 lang=python3
#
# [421] Maximum XOR of Two Numbers in an Array
#
# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/description/
#
# algorithms
# Medium (51.21%)
# Likes:    711
# Dislikes: 147
# Total Accepted:    38K
# Total Submissions: 74.2K
# Testcase Example:  '[3,10,5,25,2,8]'
#
# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai <
# 2^31.
# 
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
# 
# Could you do this in O(n) runtime?
# 
# Example:
# 
# 
# Input: [3, 10, 5, 25, 2, 8]
# 
# Output: 28
# 
# Explanation: The maximum result is 5 ^ 25 = 28.
# 
# 
# 
# 
#
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:


        """
        Build the answer bit by bit from left to right. 
        Let's say we already know the largest first seven bits we can create. 
        How to find the largest first eight bits we can create? 
        Well it's that maximal seven-bits prefix followed by 0 or 1. 
        Append 0 and then try to create the 1 one 
        (i.e., answer ^ 1) from two eight-bits prefixes from nums. 
        If we can, then change that 0 to 1.
        """

        # Bitwise Prefixes in HashSet
        # p1 ^ p2 ^ p2 = p1
        # Time  complexity: O(N)
        # Space complexity: O(1)
        # length of max number in a binary representation
        L = len(bin(max(nums))) - 2
        max_xor = 0
        for i in range(L)[::-1]:
            # go to the next bit by the left shift
            max_xor <<= 1
            # set 1 in the smallest bit
            curr_xor = max_xor | 1
            # compute all existing prefixes 
            # of length (L - i) in binary representation
            prefixes = {num >> i for num in nums}
            # Update max_xor, if two of these prefixes could result in curr_xor.
            # Check if p1^p2 == curr_xor, i.e. p1 == curr_xor^p2
            max_xor |= any(curr_xor ^ p in prefixes for p in prefixes)

        return max_xor

        # answer = 0
        # for i in range(32)[::-1]:
        #     answer <<= 1
        #     prefixes = {num >> i for num in nums}
        #     answer += any(answer ^ 1 ^ p in prefixes for p in prefixes)
        # return answer




        # Bitwise Trie
        # Time  complexity: O(N)
        # Space complexity: O(1)
        # Compute length L of max number in a binary representation
        L = len(bin(max(nums))) - 2
        # zero left-padding to ensure L bits for each number
        nums = [[(x >> i) & 1 for i in range(L)][::-1] for x in nums]

        max_xor = 0
        trie = {}
        for num in nums:
            node = trie
            xor_node = trie
            curr_xor = 0
            for bit in nums:
                # insert new number in trie
                if not bit in node:
                    node[bit] = {}
                node = node[bit]

                # to compute max xor of that new number 
                # with all previously inserted
                toggled_bit = 1 - bit
                if toggled_bit in xor_node:
                    curr_xor = (curr_xor << 1) | 1
                    xor_node = xor_node[toggled_bit]
                else:
                    curr_xor = curr_xor << 1
                    xor_node = xor_node[bit]

            max_xor = max(max_xor, curr_xor)

        return max_xor

        

