#
# @lc app=leetcode id=2937 lang=python3
#
# [2937] Make Three Strings Equal
#

# @lc code=start
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:

        size = 0
        l1, l2, l3 = map(len, (s1, s2, s3))

        for a, b, c in zip(s1, s2, s3):
            if a == b == c:
                size += 1
            else:
                break

        return l1 + l2 + l3 - 3 * size if size > 0 else -1


        
# @lc code=end

