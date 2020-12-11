#
# @lc app=leetcode id=1675 lang=python3
#
# [1675] Minimize Deviation in Array
#
# https://leetcode.com/problems/minimize-deviation-in-array/description/
#
# algorithms
# Hard (44.46%)
# Likes:    133
# Dislikes: 7
# Total Accepted:    2.6K
# Total Submissions: 5.8K
# Testcase Example:  '[1,2,3,4]'
#
# You are given an array nums of n positive integers.
# 
# You can perform two types of operations on any element of the array any
# number of times:
# 
# 
# If the element is even, divide it by 2.
# 
# 
# For example, if the array is [1,2,3,4], then you can do this operation on the
# last element, and the array will be [1,2,3,2].
# 
# 
# If the element is odd, multiply it by 2.
# 
# For example, if the array is [1,2,3,4], then you can do this operation on the
# first element, and the array will be [2,2,3,4].
# 
# 
# 
# 
# The deviation of the array is the maximum difference between any two elements
# in the array.
# 
# Return the minimum deviation the array can have after performing some number
# of operations.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,3,4]
# Output: 1
# Explanation: You can transform the array to [1,2,3,2], then to [2,2,3,2],
# then the deviation will be 3 - 2 = 1.
# 
# 
# Example 2:
# 
# 
# Input: nums = [4,1,5,20,3]
# Output: 3
# Explanation: You can transform the array after two operations to [4,2,5,5,3],
# then the deviation will be 5 - 2 = 3.
# 
# 
# Example 3:
# 
# 
# Input: nums = [2,10,8]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length
# 2 <= n <= 10^5
# 1 <= nums[i] <= 10^9
# 
#

# @lc code=start
import heapq

class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        # Simulation + Heap
        # Time  complexity: O(K x logN) = O(N x logM x logN), where N is the length of nums, and M the largest number of nums.
        # Space complexity: O(N)
        # evens, minimum = [], float("inf")
        # for num in nums:
        #     if num % 2 == 0:
        #         evens.append(-num)
        #         minimum = min(minimum, num)
        #     else:
        #         evens.append(-num * 2)
        #         minimum = min(minimum, num * 2)

        # heapq.heapify(evens)
        # min_deviation = float("inf")
        # while evens:
        #     current_value = -heapq.heappop(evens)
        #     min_deviation = min(min_deviation, current_value - minimum)
        #     if current_value % 2 == 0:
        #         minimum = min(minimum, current_value // 2)
        #         heapq.heappush(evens, -current_value // 2)
        #     else:
        #         break
        # return min_deviation



        # Pretreatment + Sorting + Sliding Window
        # Time  complexity: O(KlogK) = O(N x logM x log(N x logM))
        # Space compleixty: O(K) = O(N x logM)
        # n = len(nums)
        # possible = []
        # for i, num in enumerate(nums):
        #     if num % 2 == 0:
        #         temp = num
        #         possible.append((temp, i))
        #         while temp % 2 == 0:
        #             temp //= 2
        #             possible.append((temp, i))
        #     else:
        #         possible.append((num, i))
        #         possible.append((num * 2, i))

        # possible.sort()
        # min_deviation = float("inf")
        # need_include = {i: 1 for i in range(n)}
        # not_included = n
        # current_start = 0

        # for current_value, current_item in possible:
        #     need_include[current_item] -= 1
        #     if need_include[current_item] == 0:
        #         not_included -= 1
        #     if not_included == 0:
        #         while need_include[possible[current_start][1]] < 0:
        #             need_include[possible[current_start][1]] += 1
        #             current_start += 1
        #         if min_deviation > current_value - possible[current_start][0]:
        #             min_deviation = current_value - possible[current_start][0]

        #         need_include[possible[current_start][1]] += 1
        #         current_start += 1
        #         not_included += 1

        # return min_deviation


        # n = len(nums)
        # possible = []
        # for i, num in enumerate(nums):
        #     if num % 2 == 0:
        #         temp = num
        #         possible.append((temp, i))
        #         while temp % 2 == 0:
        #             temp //= 2
        #             possible.append((temp, i))
        #     else:
        #         possible.append((num, i))
        #         possible.append((num * 2, i))

        # heapq.heapify(possible)
        # min_deviation = float("inf")
        # need_include = {i: 1 for i in range(n)}
        # not_included = n
        # current_start = 0
        # seen = []

        # while possible:
        #     current_value, current_item = heapq.heappop(possible)
        #     seen.append([current_value, current_item])
        #     need_include[current_item] -= 1
        #     if need_include[current_item] == 0:
        #         not_included -= 1
        #     if not_included == 0:
        #         while need_include[seen[current_start][1]] < 0:
        #             need_include[seen[current_start][1]] += 1
        #             current_start += 1
        #         if min_deviation > current_value - seen[current_start][0]:
        #             min_deviation = current_value - seen[current_start][0]

        #         need_include[seen[current_start][1]] += 1
        #         current_start += 1
        #         not_included += 1

        # return min_deviation


        # Pretreatment + Heap + Pointers
        # Time  complexity: O(K x logN) = O(N x logM x logN)
        # Space complexitY: O(N)
        possible_list = []
        for num in nums:
            candidates = []
            if num % 2 == 0:
                temp = num
                candidates.append(temp)
                while temp % 2 == 0:
                    temp //= 2
                    candidates.append(temp)
            else:
                candidates.append(2 * num)
                candidates.append(num)

            possible_list.append(candidates[::-1])

        pointers = [(candidates[0], i, 0) for i, candidates in enumerate(possible_list)]
        heapq.heapify(pointers)

        min_deviation = float("inf")
        current_end = max(candidates[0] for candidates in possible_list)

        while pointers:
            current_start, index, index_in_candidate = heapq.heappop(pointers)
            if current_end - current_start < min_deviation:
                min_deviation = current_end - current_start
            if index_in_candidate + 1 == len(possible_list[index]):
                return min_deviation

            next_value = possible_list[index][index_in_candidate + 1]
            current_end = max(current_end, next_value)
            heapq.heappush(pointers, (next_value, index, index_in_candidate + 1))


        # Pretreatment + Sorting + Sliding Window
        # Time  complexity: O(KlogK) = O(N x logM x log(N x logM))
        # Space compleixty: O(K) = O(N x logM)
        # possible_list = []
        # for num in nums:
        #     candidates = []
        #     if num % 2 == 0:
        #         temp = num
        #         candidates.append(temp)
        #         while temp % 2 == 0:
        #             temp //= 2
        #             candidates.append(temp)
        #     else:
        #         candidates.append(2 * num)
        #         candidates.append(num)

        #     possible_list.append(candidates[::-1])

        # pointers = [(candidate, index, index_in_candidate) for index,
        #             candidates in enumerate(possible_list) 
        #             for index_in_candidate, candidate in enumerate(candidates)]
        # pointers.sort()

        # min_deviation = float("inf")
        # current_end = max(candidates[0] for candidates in possible_list)

        # for current_start, index, index_in_candidates in pointers:
        #     if current_end - current_start < min_deviation:
        #         min_deviation = current_end - current_start

        #     if index_in_candidates + 1 == len(possible_list[index]):
        #         return min_deviation

        #     next_value = possible_list[index][index_in_candidates + 1]
        #     current_end = max(current_end, next_value)
            
