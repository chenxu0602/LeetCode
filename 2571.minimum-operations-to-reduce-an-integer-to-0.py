#
# @lc app=leetcode id=2571 lang=python3
#
# [2571] Minimum Operations to Reduce an Integer to 0
#

# @lc code=start
class Solution:
    def minOperations(self, n: int) -> int:

        # return (n ^ (n * 3)).bit_count()


        # If there is an alone 1, like ..00001,
        # it takes at leat one operation to remove.
        # and we can remove it in one operation.
        # So we do res++ and n >>= 2,
        # remove two last bits.

        # If there are multiple 1s, like ..0000111,
        # we can't remove them in one single operation,
        # so it takes at least two operation to remove,
        # For example of ..0000111
        # we can add 1 and then remove 1000.
        # So we do n++ and remove the last bit 0.

        res = 0
        while n > 0:
            if n % 2 == 0:
                n >>= 1
            elif (n & 2) > 0:
                n += 1
                res += 1
            else:
                res += 1
                n >>= 2

        return res

        
# @lc code=end

