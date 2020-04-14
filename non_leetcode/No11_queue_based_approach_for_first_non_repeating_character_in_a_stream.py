#!/usr/bin/python
# coding=utf-8
################################################################################
'''
https://www.geeksforgeeks.org/queue-based-approach-for-first-non-repeating-character-in-a-stream/

Queue based approach for first non-repeating character in a stream
Given a stream of characters and we have to find first non repeating character
 each time a character is inserted to the stream.

Examples:

Input  : a a b c
Output : a -1 b b

Input  : a a c
Output : a -1 c
Recommended: Please solve it on “PRACTICE ” first, before moving on to the
 solution.
We have already discussed a Doubly linked list based approach in the previous
 post.





Approach-

Create a count array of size 26(assuming only lower case characters are present)
 and initialize it with zero.
Create a queue of char datatype.
Store each character in queue and increase its frequency in the hash array.
For every character of stream, we check front of the queue.
If the frequency of character at the front of queue is one, then that will be
 the first non repeating character.
Else if frequency is more than 1, then we pop that element.
If queue became empty that means there are no non repeating character so we
 will print -1.
Below is the implementation of above approach:
'''
################################################################################
from collections import deque, defaultdict
class First_Non_Repeat_Stream(object):
    # def __init__(self):
    #     self.queue = deque()
    #     self.freq = defaultdict()

    def add(self, string):
        queue = deque()
        freq = defaultdict(int)
        res = []

        for i in range(len(string)):
            queue.append(string[i])
            freq[string[i]] += 1

            candidate = None
            while len(queue) > 0:
                current = queue[0]
                if freq[current] <= 1:
                    candidate = current
                    break
                else:
                    queue.popleft()

            if candidate is not None:
                res.append(candidate)
            else:
                res.append(-1)

        return res

a = First_Non_Repeat_Stream()
print a.add('aabc')


#only first  the first one
from collections import deque, defaultdict
class First_Non_Repeat_Stream(object):
    # def __init__(self):
    #     self.queue = deque()
    #     self.freq = defaultdict()

    def first_unqiue(self, string):

        queue = deque()
        freq = defaultdict(int)
        for i in range(len(string)):
            queue.append((string[i], i))
            freq[string[i]] += 1

        while len(queue) > 0:
            current, index = queue.popleft()
            if freq[current] > 1:
                continue
            return index
        return -1


a = First_Non_Repeat_Stream()
print a.add('aabc')
