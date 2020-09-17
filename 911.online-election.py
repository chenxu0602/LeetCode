#
# @lc app=leetcode id=911 lang=python3
#
# [911] Online Election
#
# https://leetcode.com/problems/online-election/description/
#
# algorithms
# Medium (50.34%)
# Likes:    374
# Dislikes: 327
# Total Accepted:    24.6K
# Total Submissions: 48.6K
# Testcase Example:  '["TopVotedCandidate","q","q","q","q","q","q"]\n' + '[[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]'
#
# In an election, the i-th vote was cast for persons[i] at time times[i].
# 
# Now, we would like to implement the following query function:
# TopVotedCandidate.q(int t) will return the number of the person that was
# leading the election at time t.  
# 
# Votes cast at time t will count towards our query.  In the case of a tie, the
# most recent vote (among tied candidates) wins.
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: ["TopVotedCandidate","q","q","q","q","q","q"],
# [[[0,1,1,0,0,1,0],[0,5,10,15,20,25,30]],[3],[12],[25],[15],[24],[8]]
# Output: [null,0,1,1,0,0,1]
# Explanation: 
# At time 3, the votes are [0], and 0 is leading.
# At time 12, the votes are [0,1,1], and 1 is leading.
# At time 25, the votes are [0,1,1,0,0,1], and 1 is leading (as ties go to the
# most recent vote.)
# This continues for 3 more queries at time 15, 24, and 8.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= persons.length = times.length <= 5000
# 0 <= persons[i] <= persons.length
# times is a strictly increasing array with all elements in [0, 10^9].
# TopVotedCandidate.q is called at most 10000 times per test case.
# TopVotedCandidate.q(int t) is always called with t >= times[0].
# 
# 
# 
#

# @lc code=start
from collections import Counter
import bisect

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        # List of Lists + Binary Search
        # Time  complexity: O(N + Q x (logN)^2), where N is the number of votes,
        # and Q is the number of queries.
        # Space complexity: O(N)
        # self.A = []
        # self.count = Counter()
        # for p, t in zip(persons, times):
        #     self.count[p] = c = self.count[p] + 1
        #     while len(self.A) <= c:
        #         self.A.append([])
        #     self.A[c].append((t, p))


        # Precomputed Answer + Binary Search
        # Time  complexity: O(N + Q x logN), where N is the number of votes,
        # and Q is the number of queries.
        # Space complexity: O(N)
        self.A = []
        count = Counter()
        leader, m = None, 0 # leader, num votes for leader

        for p, t in zip(persons, times):
            count[p] = c = count[p] + 1
            if c >= m:
                if p != leader:
                    leader = p
                    self.A.append((t, leader))
        
                if c > m:
                    m = c

    def q(self, t: int) -> int:
        # List of Lists + Binary Search
        # Time  complexity: O(N + Q x (logN)^2), where N is the number of votes,
        # and Q is the number of queries.
        # Space complexity: O(N)
        # lo, hi = 1, len(self.A)
        # while lo < hi:
        #     mi = (lo + hi) // 2
        #     if self.A[mi][0][0] <= t:
        #         lo = mi + 1
        #     else:
        #         hi = mi

        # i = lo - 1
        # j = bisect.bisect_right(self.A[i], (t, float("inf")))
        # return self.A[i][j - 1][1]

        
        # Precomputed Answer + Binary Search
        # Time  complexity: O(N + Q x logN), where N is the number of votes,
        # and Q is the number of queries.
        # Space complexity: O(N)
        i = bisect.bisect_right(self.A, (t, float("inf")), 1)
        return self.A[i - 1][1]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
# @lc code=end

