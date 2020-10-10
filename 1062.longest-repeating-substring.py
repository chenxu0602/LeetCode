#
# @lc app=leetcode id=1062 lang=python3
#
# [1062] Longest Repeating Substring
#
# https://leetcode.com/problems/longest-repeating-substring/description/
#
# algorithms
# Medium (57.02%)
# Likes:    311
# Dislikes: 19
# Total Accepted:    14.7K
# Total Submissions: 25.5K
# Testcase Example:  '"abcd"'
#
# Given a string S, find out the length of the longest repeating substring(s).
# Return 0 if no repeating substring exists.
# 
# 
# Example 1:
# 
# 
# Input: S = "abcd"
# Output: 0
# Explanation: There is no repeating substring.
# 
# 
# Example 2:
# 
# 
# Input: S = "abbaba"
# Output: 2
# Explanation: The longest repeating substrings are "ab" and "ba", each of
# which occurs twice.
# 
# 
# Example 3:
# 
# 
# Input: S = "aabcaabdaab"
# Output: 3
# Explanation: The longest repeating substring is "aab", which occurs 3
# times.
# 
# 
# Example 4:
# 
# 
# Input: S = "aaaaa"
# Output: 4
# Explanation: The longest repeating substring is "aaaa", which occurs
# twice.
# 
# 
# 
# Constraints:
# 
# 
# The string S consists of only lowercase English letters from 'a' - 'z'.
# 1 <= S.length <= 1500
# 
# 
#

# @lc code=start
class Solution:
    def longestRepeatingSubstring(self, S: str) -> int:
        # Binary Search + Hashset of Already Seen Strings
        # Time  complexity: O(NlogN) in the average case and O(N^2) in the worst case.
        # Space complexity: O(N^2)
        # def search(L: int, n: int, S: str) -> str:
        #     # Search a substring of given length
        #     # that occurs at least 2 times.
        #     # @return start position if the substring exits and -1 otherwise.
        #     seen = set()
        #     for start in range(0, n - L + 1):
        #         tmp = S[start:start + L]
        #         if tmp in seen:
        #             return start
        #         seen.add(tmp)
        #     return -1

        # n = len(S)
        # left, right = 1, n
        # while left <= right:
        #     L = left + (right - left) // 2
        #     if search(L, n, S) != -1:
        #         left = L + 1
        #     else:
        #         right = L - 1
            
        # return left - 1


        # Binary Search + Rabin-Karp
        # Time  complexity: O(NlogN). O(logN) for the binary search and O(N) for Rabin-Karp algorithm.
        # Space complexity: O(N) to keep the hashset.
        # def search(L: int, a: int, modulus: int, n: int, nums: List[int]) -> str:
        #     # Rabin-Karp with polynomial rolling hash.
        #     # Search a substring of given length
        #     # that occurs at least 2 times.
        #     # @return start position if the substring exits and -1 otherwise.
        #     # compute the hash of string S[:L]
        #     h = 0
        #     for i in range(L):
        #         h = (h * a + nums[i]) % modulus

        #     # already seen hashes of strings of length L
        #     seen = {h}
        #     # const value to be used often : a**L % modulus
        #     aL = pow(a, L, modulus)
        #     for start in range(1, n - L + 1):
        #         # compute rolling hash in O(1) time
        #         h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
        #         if h in seen:
        #             return start
        #         seen.add(h)
        #     return -1

        # n = len(S)
        # # convert string to array of integers
        # # to implement constant time slice
        # nums = [ord(S[i]) - ord('a') for i in range(n)]
        # a = 26
        # # modulus value for the rolling hash function to avoid overflow
        # modulus = 2**24

        # # binary search, L = repeating string length
        # left, right = 1, n
        # while left <= right:
        #     L = left + (right - left) // 2
        #     if search(L, a, modulus, n, nums) != -1:
        #         left = L + 1
        #     else:
        #         right = L - 1

        # return left - 1
        


        ans = 0
        for i in range(1, len(S)):
            if ans >= len(S) - i:
                break

            tmp = 0
            for x, y in zip(S[i:], S[:-i]):
                if x == y:
                    tmp += 1
                    ans = max(ans, tmp)
                else:
                    tmp = 0

        return ans
# @lc code=end

