#
# @lc app=leetcode id=2952 lang=python3
#
# [2952] Minimum Number of Coins to be Added
#

# @lc code=start
class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:

        # The key to this problem is realizing that if you can make every single
        # number in a range [0,n] using an array of numbers, you can add any number from 1 to n + 1 and extend this range by the number you add.

        res = num = i = 0
        coins.sort()

        while num < target:
            if i < len(coins) and coins[i] <= num + 1:
                num += coins[i]
                i += 1
            else:
                res += 1
                num += num + 1

        return res

        
# @lc code=end

