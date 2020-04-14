#!/usr/bin/python
# coding=utf-8
################################################################################
'''
Suppose we have very large sparse vectors (most of the elements in vector are zeros)

Find a data structure to store them
Compute the Dot Product.
Follow-up:
What if one of the vectors is very small?
'''
################################################################################

'''
[(index, value)] only save the element without 0 value.
a = [(1,2),(2,3),(100,5)]
b = [(0,5),(1,1),(100,6)]

i = 0; j = 0
result = 0
while i < len(a) and j < len(b):
    if a[i][0] == b[j][0]:
        result += a[i][1] * b[j][1]
        i += 1
        j += 1
    elif a[i][0] < b[j][0]:
        i += 1
    else:
        j += 1
print(result)
'''

class Solution(object):
    #only save the element without 0 value
    #[(index, value)], not right below. need to change
    def compress_array_zero(self, array):
        res = []

        start = 0
        while start < len(array):
            current = array[start]
            end = start
            count = 1
            while end + 1 < len(array) and array[end] == array[end + 1]:
                end += 1
                count += 1

            if current != 0:
                res.append([count, current])
            start = end + 1
        return res

    def sparse_matrix_vector_dot_production(self, array1, array2):
        compress1 = self.compress_array_zero(array1)
        compress2 = self.compress_array_zero(array2)

        res = 0
        index1, index2 = 0, 0
        while index1 < len(compress1) and index2 < len(compress2):
            if compress1[index1][0] == compress2[index2][0]:
                res += compress1[index1][1] * compress2[index2][1]
            elif compress1[index1][0] < compress2[index2][0]:
                index1 += 1
            else:
                index2 += 1
        return res
