#
# @lc app=leetcode id=473 lang=python3
#
# [473] Matchsticks to Square
#
# https://leetcode.com/problems/matchsticks-to-square/description/
#
# algorithms
# Medium (37.59%)
# Likes:    596
# Dislikes: 61
# Total Accepted:    37K
# Total Submissions: 98.1K
# Testcase Example:  '[1,1,2,2,2]'
#
# Remember the story of Little Match Girl? By now, you know exactly what
# matchsticks the little match girl has, please find out a way you can make one
# square by using up all those matchsticks. You should not break any stick, but
# you can link them up, and each matchstick must be used exactly one time.
# 
# ⁠Your input will be several matchsticks the girl has, represented with their
# stick length. Your output will either be true or false, to represent whether
# you could make one square using all the matchsticks the little match girl
# has.
# 
# Example 1:
# 
# Input: [1,1,2,2,2]
# Output: true
# 
# Explanation: You can form a square with length 2, one side of the square came
# two sticks with length 1.
# 
# 
# 
# Example 2:
# 
# Input: [3,3,3,3,4]
# Output: false
# 
# Explanation: You cannot find a way to form a square with all the
# matchsticks.
# 
# 
# 
# Note:
# 
# The length sum of the given matchsticks is in the range of 0 to 10^9.
# The length of the given matchstick array will not exceed 15.
# 
# 
#

# @lc code=start
class Solution:
    def makesquare(self, nums: List[int]) -> bool:
        # Depth First Search
        # Time  complexity: O(4^N) because we have a total of NN sticks and for each one of those matchsticks, we have 44 different possibilities for the subsets they might belong to or the side of the square they might be a part of.
        # Space complexity: O(N). For recursive solutions, the space complexity is the stack space occupied by all the recursive calls. The deepest recursive call here would be of size NN and hence the space complexity is O(N). There is no additional space other than the recursion stack in this solution.
        # if not nums:
        #     return False

        # L = len(nums)

        # perimeter = sum(nums)

        # possible_side = perimeter // 4

        # if possible_side * 4 != perimeter:
        #     return False

        # nums.sort(reverse=True)

        # sums = [0] * 4

        # def dfs(index):
        #     if index == L:
        #         return sums[0] == sums[1] == sums[2] == possible_side

        #     for i in range(4):
        #         # If this matchstick can fir in the space left for the current side
        #         if sums[i] + nums[index] <= possible_side:
        #             # Recurse
        #             sums[i] += nums[index]
        #             if dfs(index + 1):
        #                 return True

        #             # Revert the effects of recursion because we no longer need them for other recursions.
        #             sums[i] -= nums[index]

        #     return False

        # return dfs(0)


        # Dynamic Programming
        # Time  complexity: O(N x 2^N). At max 2^N unique bit masks are possible and during every recursive call, we iterate our original matchsticks array to sum up the values of matchsticks used to update the sides_formed variable.
        # Space complexity: O(N + 2^N) because NN is the stack space taken up by recursion and 4 x 2^N = O(2^N) is the max possible size of our cache for memoization.
        if not nums:
            return False

        L = len(nums)

        perimeter = sum(nums)

        # Possible side of our square from the given matchsticks
        possible_side = perimeter // 4

        # If the perimeter isn't equally divisible among 4 sides, return False.
        if possible_side * 4 != perimeter:
            return False

        # Memoization cache for the dynamic programming solution.
        memo = {}

        # mask and the sides_done define the state of our recursion.
        def recurse(mask, sides_done):
            # This will calculate the total sum of matchsticks used till now using the bits of the mask.
            total = 0
            for i in range(L - 1, -1, -1):
                if not (mask & (1 << i)):
                    total += nums[L - 1 - i]

            # If some of the matchsticks have been used and the sum is divisible by our square's side, then we increment the number of sides completed.
            if total > 0 and total % possible_side == 0:
                sides_done += 1

            # If we were successfully able to form 3 sides, return True
            if sides_done == 3:
                return True

            # If this recursion state has already been calculated, just return the stored value.
            if (mask, sides_done) in memo:
                return memo[(mask, sides_done)]

            # Common variable to store answer from all possible further recursions from this step.
            ans = False

            # rem stores available space in the current side (incomplete).
            c = total // possible_side
            rem = possible_side * (c + 1) - total

            # Iterate over all the matchsticks
            for i in range(L - 1, -1, -1):
                # If the current one can fit in the remaining space of the side and it hasn't already been taken, then try it out
                if nums[L - 1 - i] <= rem and mask & (1 << i):
                    # If the recursion after considering this matchstick gives a True result, just break. No need to look any further.
                    # mask ^ (1 << i) makes the i^th from the right, 0 making it unavailable in future recursions.
                    if recurse(mask ^ (1 << i), sides_done):
                        ans = True
                        break

            # cache the result for the current recursion state.   
            memo[(mask, sides_done)] = ans
            return ans

        # recurse with the initial mask with all matchsticks available.
        return recurse((1 << L) - 1, 0)
            
        
# @lc code=end

