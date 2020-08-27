#
# @lc app=leetcode id=514 lang=python3
#
# [514] Freedom Trail
#
# https://leetcode.com/problems/freedom-trail/description/
#
# algorithms
# Hard (42.86%)
# Likes:    429
# Dislikes: 24
# Total Accepted:    18.6K
# Total Submissions: 43.2K
# Testcase Example:  '"godding"\n"gd"'
#
# In the video game Fallout 4, the quest "Road to Freedom" requires players to
# reach a metal dial called the "Freedom Trail Ring", and use the dial to spell
# a specific keyword in order to open the door.
# 
# Given a string ring, which represents the code engraved on the outer ring and
# another string key, which represents the keyword needs to be spelled. You
# need to find the minimum number of steps in order to spell all the characters
# in the keyword.
# 
# Initially, the first character of the ring is aligned at 12:00 direction. You
# need to spell all the characters in the string key one by one by rotating the
# ring clockwise or anticlockwise to make each character of the string key
# aligned at 12:00 direction and then by pressing the center button.
# 
# At the stage of rotating the ring to spell the key character key[i]:
# 
# 
# You can rotate the ring clockwise or anticlockwise one place, which counts as
# 1 step. The final purpose of the rotation is to align one of the string
# ring's characters at the 12:00 direction, where this character must equal to
# the character key[i].
# If the character key[i] has been aligned at the 12:00 direction, you need to
# press the center button to spell, which also counts as 1 step. After the
# pressing, you could begin to spell the next character in the key (next
# stage), otherwise, you've finished all the spelling.
# 
# 
# Example:
# 
# 
# 
# 
# 
# Input: ring = "godding", key = "gd"
# Output: 4
# Explanation:
# For the first key character 'g', since it is already in place, we just need 1
# step to spell this character. 
# For the second key character 'd', we need to rotate the ring "godding"
# anticlockwise by two steps to make it become "ddinggo".
# Also, we need 1 more step for spelling.
# So the final output is 4.
# 
# 
# Note:
# 
# 
# Length of both ring and key will be in range 1 to 100.
# There are only lowercase letters in both strings and might be some duplcate
# characters in both strings.
# It's guaranteed that string key could always be spelled by rotating the
# string ring.
# 
# 
#

# @lc code=start
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # m, n = len(key), len(ring)
        # dp = [[0] * n for _ in range(m + 1)]

        # for i in range(m-1, -1, -1):
        #     for j in range(n):
        #         dp[i][j] = float("inf")
        #         for k in range(n):
        #             if ring[k] == key[i]:
        #                 diff = abs(j - k)
        #                 step = min(diff, n - diff)
        #                 dp[i][j] = min(dp[i][j], step + dp[i+1][k])

        # return dp[0][0] + m


        # O(MNN) while N is the most occurrence of the same character on the ring.
        def dist(i, j): return min(abs(i - j), len(ring) - abs(i - j))

        pos = {}
        for i, c in enumerate(ring):
            if c in pos:
                pos[c].append(i)
            else:
                pos[c] = [i]

        state = {0: 0}
        for c in key:
            next_state = {}
            for j in pos[c]:
                next_state[j] = float("inf")
                for i in state:
                    next_state[j] = min(next_state[j], dist(i, j) + state[i])

            state = next_state

        return min(state.values()) + len(key)


        # stepsmap = {0: 0}

        # for target in key:
        #     cur = {}
        #     for idx in stepsmap:
        #         for i, c in enumerate(ring):
        #             if c == target:
        #                 steps = min(abs(idx - i), len(ring) - abs(idx - i))
        #                 cur[i] = steps + stepsmap[idx] if i not in cur else min(cur[i], 
        #                     steps + stepsmap[idx])

        #     stepsmap = cur

        # return min(stepsmap.values()) + len(key)


        
# @lc code=end

