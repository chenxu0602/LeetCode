def longest_palindromic_subsequence(s):
    # Initializing a lookup table of dimensions len(s) x len(s)
    lookup_table = [[0 for x in range(len(s))] for x in range(len(s))]

    # Every sequence with one element is a palindrome of length 1
    for i in range(len(s)):
        lookup_table[i][i] = 1

    for start_index in reversed(range(len(s))):
        for end_index in range(start_index + 1, len(s)):

            # case 1: elements at the beginning and the end are the same
            if s[start_index] == s[end_index]:
                lookup_table[start_index][end_index] = 2 + lookup_table[start_index + 1][end_index - 1]

            # case 2: skip one element either from the beginning or the end
            else:
                lookup_table[start_index][end_index] = max(lookup_table[start_index + 1][end_index],
                                                           lookup_table[start_index][end_index - 1])

    return lookup_table[0][len(s) - 1]


def find_lps_length(s):
    # initializing a lookup table of dimensions len(s) * len(s)
    dp = [[0 for x in range(len(s))] for x in range(len(s))]

    # every string with one character is always a palindrome
    for i in range(len(s)):
        dp[i][i] = 1

    for start in reversed(range(len(s)-1)):
        for end in range(start + 1, len(s)):
            # the characters at the start and end indexes match
            if s[start] == s[end]:
                substring_length = end - start + 1

                # if the substring length is 2 or the remaining substring is a palindrome
                if substring_length == 2 or substring_length - 2 == dp[start + 1][end - 1]:
                    dp[start][end] = substring_length
                else:
                    # skip one element either from the beginning or end and select the maximum resultant value
                    dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])
            else:
                # skip one element either from the beginning or end and select the maximum resultant value
                dp[start][end] = max(dp[start + 1][end], dp[start][end - 1])

    return dp[0][len(s) - 1]


def count_palindromic_substring(str1):
  n = len(str1)
  # Declare a lookup table 2-D table which that
  # the answers of the tabulation
  lookup_table = [[False for _ in range(n)] for _ in range(n)]
  ps_count=0

  # start filling the lookup table with the results of the
  # palindromic substrings
  for i in range(n - 1, -1, -1):
    for j in range(i, n):
      # start checking substrings from i to j
      # if they are palindrome or not
      if str1[i] == str1[j]:
        # if the substring is palindrome set the
        # value in table as True if we have not checked it before
        if i+1 >= j:
          lookup_table[i][j] = True
        # otherwise fill it with the previously stored value
        else:
          lookup_table[i][j] = lookup_table[i+1][j-1]
      # if the substring is a palindrome increment the count of
      # the palindromic substrings by 1
      if lookup_table[i][j]:
        ps_count += 1

  return ps_count


def min_cuts_helper(s, palindrome_table, dp):

    n = len(s)

    # Filling the palindrome table
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                # If the string consists of two characters or if the remaining string, str[i + 1 : j - 1]
                # is a palindrome, str[i : j] must also be a palindrome
                if j - i == 1 or palindrome_table[i + 1][j - 1]:
                    palindrome_table[i][j] = 1

    # Traversing the dp table in reverse order
    for i in range(n - 1, -1, -1):

        # If str[i : n - 1] is a palindrome, no cuts need to be performed,
        # so dp[i] = 0
        if palindrome_table[i][n - 1] == 1:
            dp[i] = 0

        # Otherwise, we traverse the remaining string to check if it contains
        # a palindrome and perform the minimum number of cuts on it to update
        # dp[i]
        else:
            for j in range(n - 2, i - 1, -1):
                if palindrome_table[i][j] == 1:
                    dp[i] = min(dp[i], 1 + dp[j + 1])

    # We return dp[0], as it contains the minimum number of cuts over the
    # entire string
    return dp[0]


def minimum_partition_array_sum_difference(nums):

    # Calculating the sum of the original array
    sum_array = sum(nums)

    # Calculating the number of rows and columns in the 2-D array
    rows = len(nums)
    cols = (sum_array // 2) + 1

    # Initializing the 2-D array
    dp = [[-1 for x in range(cols)] for y in range(rows)]

    # The first column will be initialized to all 1s, since a sum s = 0
    # will always be true if no elements are added to the subset
    for i in range(rows):
        dp[i][0] = 1

    # For the first row, each entry will be 1 if the sum s is equal to the
    # first element, and 0 otherwise
    for s in range(1, cols):
        dp[0][s] = nums[0] == s

    # Iterating and filling the dp array
    for i in range(1, rows):
        for s in range(1, cols):
            # Check if sum s can be obtained without nums[i] in the array
            if dp[i - 1][s]:
                dp[i][s] = dp[i - 1][s]

            # Check if sum s can be obtained with nums[i] in the array
            elif s >= nums[i]:
                dp[i][s] = dp[i - 1][s - nums[i]]

            # If neither of the above two conditions is true, sum s can not be
            # obtained with nums[i] included in the array
            else:
                dp[i][s] = 0

    # Find the largest index in the last row which is 1 and return the absolute
    # difference between the two sums
    for s in range(cols - 1, -1, -1):
        if dp[rows - 1][s] == 1:
            sum1 = s
            sum2 = sum_array - sum1
            return abs(sum2 - sum1)


def min_refuel_stops(target, start_fuel, stations):
        n = len(stations)
        # creating an array to store the maximum distances
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        i = 0
        # fill up the first column of the table with the start fuel.
        while (i <= n):
            dp[i][0] = start_fuel
            i += 1
        i = 1
        # iterating over all the stations from i = 1 to n
        while (i <= n):
            j = 1
            # checking fueling stops from j = 1 to j = i
            while (j <= i):
                # refuel at current station
                if (dp[i - 1][j - 1] >= stations[i - 1][0]):
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + stations[i - 1][1])
                # not refuel at current station
                else:
                    dp[i][j] = dp[i - 1][j]
                j += 1
            i += 1
        i = 0
        # After visiting all the stations, find minimum `j`
        while (i <= n):
            if (dp[n][i] >= target) :
                return i
            i += 1
        return -1

def can_partition_array(nums):
    array_sum = sum(nums)

    # if 'array_sum' is an odd number, we can't have 
    # two subarrays with equal sum
    if array_sum % 2 != 0:
        return False
    else:
    # We are trying to find a subarray of given numbers 
    # that has a total sum of 's/2'.
        target_sum = int(array_sum / 2)

    nums_len = len(nums)
    
    # Making a 2-D table.
    dp = [[0 for x in range(target_sum + 1)] for y in range(nums_len + 1)]
    
    # Intializng the first row with False and first column with True.
    for i in range(nums_len + 1):
        for j in range(target_sum + 1):
            if i == 0 and j == 0:
                dp[i][j] = True

            elif j == 0:
                dp[i][j] = True

            elif i == 0:
                dp[i][j] = False
    
    # Process all subarrays for all sums
    for i in range(1, nums_len + 1):
        for j in range(1, target_sum + 1):
            # if we can find a subset to get the remaining sum
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - nums[i - 1]] or dp[i - 1][j]
            # else we can get the sum 'j' without the number at index 'i'
            else:
                dp[i][j] = dp[i - 1][j]

    # Return the answer
    return dp[nums_len][target_sum]


def count_squares(matrix):
	# if the matrix is empty, return 0
	if len(matrix) == 0 or len(matrix[0]) == 0:
		return 0

	# create lookup table to store number of squares
	lookup_table = [[0 for x in range(len(matrix[0]))] for x in range(len(matrix))]
	result = 0

	# copy first row and column of input matrix to lookup table
	for i in range(len(matrix)):
	    lookup_table[i][0] = matrix[i][0]
	for i in range(len(matrix[0])):
	    lookup_table[0][i] = matrix[0][i]

	# iterate over the matrix and store the count od squares in lookup_table
	for i in range(1, len(matrix)):
		for j in range(1, len(matrix[0])):
			# If matrix[i][j] is equal to 0
			if (matrix[i][j] == 0):
				continue

			# there is at least one square submatrix at this location, hence the + 1
			# in addition, find the minimum number of square submatrices
			# whose bottom-right corner is one of the neighbours of this location.
			lookup_table[i][j] = 1 + min(lookup_table[i - 1][j], lookup_table[i][j - 1], lookup_table[i - 1][j - 1])

	# sum up the values in the lookup_table to get the count of square submatrices
	for i in range(0, len(lookup_table)):
		for j in range(0, len(lookup_table[0])):
			result += lookup_table[i][j]

	return result


def unbounded_knapsack(weights, values, n, capacity):
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]

    # Base case
    for i in range(weights[0], capacity+1):
        dp[0][i] = (i//weights[0]) * values[0]

    for i in range(1,n):
        for j in range(0,capacity+1):

            # Check if the weight of the nth item is less than capacity
            # If it is, we have two choices
            # 1) Include the item
            # 2) Don't include the item
            if (weights[i] <= j):
                taken = values[i]+ dp[i][j-weights[i]]
                not_taken = 0 + dp[i-1][j]
                dp[i][j] = max(taken, not_taken)

            # If weight of the nth item is greater than the capacity
            # Don't include the item
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n-1][capacity]


def rod_cutting(lengths, prices, n):
    lengthsCount = len(lengths)
    pricesCount = len(prices)

    # base cases
    if n == 0 or pricesCount == 0 or pricesCount != lengthsCount:
        return 0

    # Creating a lookup table of size len(lengths) x (n + 1)
    dp = [[0 for _ in range(n+1)] for _ in range(lengthsCount)]

    # process all rod lengths for all given lengths
    for curr in range(lengthsCount):
        for rod_length in range(1, n + 1):
            # Fetch the maximum revenue obtained by selling the rod
            # of size rod_length - lengths[curr]
            revenue1 = revenue2 = 0
            if lengths[curr] <= rod_length:
                revenue1 = prices[curr] + dp[curr][rod_length - lengths[curr]]

            # Fetch the maximum revenue obtained without cutting the rod
            if curr > 0:
                revenue2 = dp[curr - 1][rod_length]

            # store the result in the table
            dp[curr][rod_length] = max(revenue1, revenue2)

    # maximum revenue will be at the bottom-right corner.
    return dp[lengthsCount - 1][n]

def coin_change(coins, total):
    if total < 1:
        return 0
    return calculate_minimum_coins(coins, total)

def calculate_minimum_coins(coins, rem):
    # Helper function that calculates amount left to be calculated
    # and tells what its value can be.
    dp = [rem+1] * (rem+1)
    dp[0] = 0

    for i in range(1, rem+1):
      for c in coins:
        if i-c >= 0:
          dp[i] = min(dp[i], 1 + dp[i-c])

    if dp[rem] != (rem+1):
        return dp[rem]
    else:
        return -1


def find_unique_path(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    # If the starting cell has an obstacle, then return 0 
    # as there would be no paths to the destination.
    if matrix[0][0] == 1:
        return 0

    # Number of ways of reaching the starting cell = 1.
    matrix[0][0] = 1

    # Fill the values for the first column
    for i in range(1, rows):
        matrix[i][0] = int(matrix[i][0] == 0 and matrix[i-1][0] == 1)

    # Fill the values for the first row        
    for j in range(1, cols):
        matrix[0][j] = int(matrix[0][j] == 0 and matrix[0][j-1] == 1)

    # Start from matrix[1][1], we fill up the values.
	# The number of ways of reaching matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
            else:
                matrix[i][j] = 0

    # Return value stored in rightmost bottommost cell. 
	# That is the destination.
    return matrix[rows - 1][cols - 1]


def min_multiplications(dims):

    # Table for tabulation
    dp = [[0 for _ in range(len(dims))] for _ in range(len(dims))]

    # Iterating to fill table
    for l in range(2,len(dims)):
        for i in range(1,len(dims)-l+1):
            j = i+l-1
            dp[i][j] = math.inf
            for k in range(i, j):
                temp = dp[i][k]+ dp[k+1][j] + dims[i-1]*dims[k]*dims[j]
                if temp < dp[i][j]:
                    dp[i][j] = temp # Storing the minimum value
    return dp[1][-1]


def lcs_length(s1, s2):
  n = len(s1)   # length of s1
  m = len(s2)   # length of s2

  dp = [[0 for j in range(m+1)] for i in range(n+1)]  # table for tabulation of size m x n
  max_length = 0   # to keep track of longest substring seen 

  for i in range(1, n+1):           # iterating to fill table
    for j in range(1, m+1):
      if s1[i-1] == s2[j-1]:    # if characters at this position match, 
        dp[i][j] = dp[i-1][j-1] + 1 # add 1 to the previous diagonal and store it in this diagonal
        max_length = max(max_length, dp[i][j])  # if this substring is longer, update max_length
      else:
        dp[i][j] = 0 # if character don't match, common substring size is 0
  return max_length


def longest_common_subsequence(str1, str2):
    n = len(str1)   # length of str1
    m = len(str2)   # length of str2

    rows = n + 1
    cols = m + 1

    # Initializing the 2-D table, filling the first row and column with all 0s
    dp = [[0 if (i == 0 or j == 0) else -1 for i in range(cols)] for j in range(rows)]

    # Iterating to fill the table
    for i in range(1, rows):           
        # calculate new row (based on previous row i.e. dp)
        for j in range(1, cols):
            # if characters at this position match, 
            if str1[i-1] == str2[j-1]:    
                # add 1 to the previous diagonal and store it in this diagonal
                dp[i][j] = dp[i-1][j-1] + 1 
            else:
                # If the characters don't match, fill this entry with the max of the
                # left and top elements
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]) 
    return dp[n][m]


def shortest_common_supersequence(str1, str2):
    # lookup table of size (m+1)*(n+1)
    lookup_table = [[0 for x in range(len(str2) + 1)] for x in range(len(str1) + 1)]

    # filling the additional row and column with constants
    for i in range(len(str1) + 1):
        lookup_table[i][0] = i

    for j in range(len(str2) + 1):
        lookup_table[0][j] = j

    # iterate through both the strings
    for i1 in range(1, len(str1) + 1):
        for i2 in range(1, len(str2) + 1):
            # if the characters match or not
            if str1[i1 - 1] == str2[i2 - 1]:
                lookup_table[i1][i2] = 1 + lookup_table[i1 - 1][i2 - 1]
            else:
                lookup_table[i1][i2] = 1 + min(lookup_table[i1 - 1][i2], lookup_table[i1][i2 - 1])

    # return the last value of the lookup table
    return lookup_table[len(str1)][len(str2)]


def find_max_matching_subseq(str1, str2):
    m = len(str1)   # length of str1
    n = len(str2)   # length of str2

    # Initializing the 2-D table
    lookup_table = [[-1 for x in range(n+1)] for y in range(m+1)]

    # Initializing the first row with 0s
    for j in range(n+1):
        lookup_table[0][j] = 0

    # Initializing the first column with 0s
    for i in range(m+1):
        lookup_table[i][0] = 0

    # Iterating to fill the table
    for i in range(1, m+1):
        # calculate new row (based on previous row i.e. lookup_table)
        for j in range(1, n+1):
            # if characters at this position match,
            if str1[i-1] == str2[j-1]:
                # add 1 to the previous diagonal and store it in this diagonal
                lookup_table[i][j] = lookup_table[i-1][j-1] + 1
            else:
                # If the characters don't match, fill this entry with the max of the
                # left and top elements
                lookup_table[i][j] = max(lookup_table[i][j-1], lookup_table[i-1][j])
    return lookup_table[m][n]


def min_edit_dist_iterative(str1, str2, m, n):

    # Create a table to store results of sub-problems
    lookup_table = [[-1 for i in range(n + 1)] for i in range(m + 1)]

    # Fill lookup_table [][] in bottom up manner
    for i in range(m+1):
        # If second string is empty, only option is to
        # remove all characters of first string
        lookup_table[i][0] = i # Min. operations = i

    for j in range(n+1):
        # If first string is empty, only option is to
        # insert all characters of second string
        lookup_table[0][j] = j # Min. operations = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # If last characters are same, ignore last char
            # and recur for remaining string
            if str1[i - 1] == str2[j - 1]:
                lookup_table[i][j] = lookup_table[i - 1][j - 1]

            # If the last character is different, consider all
            # possibilities and find the minimum
            # adding '1' because every operation has cost of '1'
            else:
                lookup_table[i][j] = 1 + min(lookup_table[i][j - 1],  # Insert
                                             lookup_table[i - 1][j],  # Remove
                                             lookup_table[i - 1][j - 1])  # Replace

    return lookup_table[m][n]

ef find_LRS(str):
    size = len(str)
    # Create a table to hold intermediate values
    lookup_table = [[0 for x in range(size + 1)] for y in range((size + 1))]

    # Starting from second row, filling the lookup table bottom-up wise
    for i in range(1, size + 1):
        for k in range(1, size + 1):
            # Characters are same but indexes are different
            if str[i - 1] == str[k - 1] and i != k:
                lookup_table[i][k] = lookup_table[i - 1][k - 1] + 1
            # Check if the characters at both indexes don't match
            else:
                lookup_table[i][k] = max(lookup_table[i - 1][k], lookup_table[i][k - 1])

    # Returning the longest repeating subsequence length
    return lookup_table[size][size]


def number_of_subsequences(str1, str2):
    # initializing variables
    m = len(str1)
    n = len(str2)
    lookup_table = [[0 for x in range(0, n + 1)] for x in range(0, m + 1)]

    # filling the last row with 0s
    for i in range(0, n + 1):
        lookup_table[m][i] = 0

    # filling the last column with 1s
    for i in range(0, m + 1):
        lookup_table[i][n] = 1

    # iterating over the lookup table starting from m-1 and n-1
    for i1 in range(m - 1, -1, -1):
        for i2 in range(n - 1, -1, -1):
            # if both the characters are same
            if str1[i1] == str2[i2]:
                lookup_table[i1][i2] += lookup_table[i1 + 1][i2 + 1] + lookup_table[i1 + 1][i2]
            # if the two characters are different
            else:
                lookup_table[i1][i2] = lookup_table[i1 + 1][i2]

    # returning the result stored in lookup_table[0][0]
    return lookup_table[0][0]


def is_interleaving(s1, s2, s3):
    # For the empty pattern, we have one matching
    if len(s1) + len(s2) != len(s3):
        return False

    # Create a table with an extra row and column to separate the base cases.
    lookup_table = [[False for i in range(len(s2) + 1)] for i in range(len(s1) + 1)]

    for s1_index in range(len(s1) + 1):
        for s2_index in range(len(s2) + 1):

            # If 's1' and 's2' are empty, then 's3' must have been empty too.
            if s1_index == 0 and s2_index == 0:
                lookup_table[s1_index][s2_index] = True
            # Checking the interleaving with 's2' only
            elif s1_index == 0 and s2[s2_index - 1] == s3[s1_index + s2_index - 1]:
                lookup_table[s1_index][s2_index] = lookup_table[s1_index][s2_index - 1]
            # Checking the interleaving with 's1' only
            elif s2_index == 0 and s1[s1_index - 1] == s3[s1_index + s2_index - 1]:
                lookup_table[s1_index][s2_index] = lookup_table[s1_index - 1][s2_index]
            else:
                # If the letter of 's1' and 's3' match, we take whatever is matched till s1_index-1
                if s1_index > 0 and s1[s1_index - 1] == s3[s1_index + s2_index - 1]:
                    lookup_table[s1_index][s2_index] = lookup_table[s1_index - 1][s2_index]

                # If the letter of 's2' and 's3' match, we take whatever is matched till s2_index-1 too
                # note the '|=', this is required when we have common letters
                if s2_index > 0 and s2[s2_index - 1] == s3[s1_index + s2_index - 1]:
                    lookup_table[s1_index][s2_index] |= lookup_table[s1_index][s2_index - 1]

    return lookup_table[len(s1)][len(s2)]


def word_break(s, word_dict):

    # Initializing a table of size s.length + 1
    dp_solutions = [[]] * (len(s)+1)

    # Setting base case
    dp_solutions[0] = [""]

    # For each substring in the input string, repeat the process.
    for i in range(1, len(s)+1):

        # An array to store the results of the current substring being checked.
        temp = []

        # Iterate over the current substring and break it down into all possible prefixes.
        for j in range(0, i):
            prefix = s[j:i]

            # Check if the current prefix exists in word_dict. If it does, we know that it is a valid word
            # and can be used as part of the solution.
            if prefix in word_dict:

                # Check if any part of the current substring already exists in the dp_solutions array.
                for substrings in dp_solutions[j]:
                    # Merge the prefix with the already calculated results
                    temp.append((substrings + " " + prefix).strip())

        dp_solutions[i] = temp

    # Returning all the sentences formed using a complete string s.
    return dp_solutions[len(s)]


def LIS_length(nums):
    size = len(nums)
    # we created a table here
    dp = [[0]*(size+1) for i in range(size+1)]

    for curr in range(size-1, -1, -1):
        for prev in range(curr-1, -2, -1):
            length = dp[curr+1][prev+1]
            # if 'prev' is negative or previous value is less than the next value
            # we will take it
            if prev < 0 or nums[prev] < nums[curr]:
                length = max(length, 1+dp[curr+1][curr+1])
            dp[curr][prev+1] = length
    return dp[0][0]


def lbs_length(nums):

    n = len(nums)
    lis_forward= [1] * n
    lis_backward = [1] * n
    result = 1

    # Populating the lis_forward array
    for i in range(n):
        for j in range(i):
            if(nums[i] > nums[j] and lis_forward[i] < 1 + lis_forward[j]):
                lis_forward[i] = 1 + lis_forward[j]

    # Populating the lis_backward array
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n, 1):
            if(nums[i] > nums[j] and lis_backward[i] < 1 + lis_backward[j]):
                lis_backward[i] = 1 + lis_backward[j]

    # Calculating the length of the bitonic subsequence at every index and
    # selecting the maximum one
    for i in range(n):
        length = lis_forward[i] + lis_backward[i] - 1
        result = max(result, length)


    return result


def LAS(nums):

    n = len(nums)
    if n == 0:
        return 0

    # initialize dp with 1s as any sequence of length one is always the LAS
    dp =[[1 for _ in range(n)] for _ in range(2)]

    # iterate over all elements of nums
    for current in range(1, n):
        previous = current-1;

        # if the current element is greater than the previous element
        if nums[current] > nums[previous]:
            # current element can contribute to an ascending ordering
            # the ascending dp row value is updated by adding 1 to the length of the
            # longest descending subsequence till previous index
            dp[0][current] = 1 + dp[1][previous]
            # length of the longest descending subsequence is carried forward as it is
            dp[1][current] = dp[1][previous]

        # if the current element is less than the previous element
        elif nums[current] < nums[previous]:
            # current element can contribute to a descending ordering
            # the descending dp row value is updated by adding 1 to the length of the
            # longest ascending subsequence till previous index
            dp[1][current] =  1 + dp[0][previous]
            # length of the longest ascending subsequence is carried forward as it is
            dp[0][current] = dp[0][previous]

        # if the current and previous elements are equal
        else:
            # carry forward the previous values
            dp[1][current] = dp[1][previous]
            dp[0][current] = dp[0][previous]

    # return maximum of the two final values
    return max(dp[1][n-1], dp[0][n-1])


def max_bridges_count(north, south):
    n = len(north)
    # Making pairs by joining the north and south array
    pairs = list(zip(north, south))
    # sorting the pairs according to the southern values
    pairs.sort(key = lambda x:(x[1], x[0]))
    # Since southern values are sorted, we will extract the northern values
    memo_north = [pairs[i][0] for i in range(n)]
    size = len(memo_north)

    # 2-D table for tabulation of size (n x n)
    dp = [[0 for j in range(n + 1)] for i in range(n + 1)]

    for i in range(0, size + 1):
        dp[size][i] = 0

    for curr in range(size - 1, -1, -1):
        for prev in range(i - 1, -2, -1):
            length = dp[curr + 1][prev + 1]
            # if previous value is negative or is less than the
            # current value, then we will include it
            if prev < 0 or memo_north[prev] < memo_north[curr]:
                length = max(length, 1 + dp[curr + 1][curr + 1])

            dp[curr][prev + 1] = length

    return dp[curr][prev + 1]

ef min_cuts_helper(s, palindrome_table, dp):

    n = len(s)

    # Filling the palindrome table
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                # If the string consists of two characters or if the remaining string, str[i + 1 : j - 1]
                # is a palindrome, str[i : j] must also be a palindrome
                if j - i == 1 or palindrome_table[i + 1][j - 1]:
                    palindrome_table[i][j] = 1

    # Traversing the dp table in reverse order
    for i in range(n - 1, -1, -1):

        # If str[i : n - 1] is a palindrome, no cuts need to be performed,
        # so dp[i] = 0
        if palindrome_table[i][n - 1] == 1:
            dp[i] = 0

        # Otherwise, we traverse the remaining string to check if it contains
        # a palindrome and perform the minimum number of cuts on it to update
        # dp[i]
        else:
            for j in range(n - 2, i - 1, -1):
                if palindrome_table[i][j] == 1:
                    dp[i] = min(dp[i], 1 + dp[j + 1])

    # We return dp[0], as it contains the minimum number of cuts over the
    # entire string
    return dp[0]



def find_sum_of_three(nums, target):
    nums.sort()

    for i in range(0, len(nums)-2):
        low = i + 1
        high = len(nums) - 1

        while low < high:
            triplet = nums[i] + nums[low] + nums[high]

            if triplet == target:
                return True

            elif triplet < target:
                low += 1

            else:
                high -= 1

    return False


def remove_nth_last_node(head, n):
    right = head
    left = head

    for i in range(n):
        right = right.next

    if not right:
        return head.next

    while right.next:
        right = right.next
        left = left.next

    left.next = left.next.next

    return head

def sort_colors(colors):
    red, white, blue = 0, 0, len(colors) - 1

    while white <= blue:
        if colors[white] == 0:
            if colors[red] != 0:
                colors[red], colors[white] = colors[white], colors[red]

            white += 1
            red += 1

        elif colors[white] == 1:
            white += 1

        else:
            if colors[blue] != 2:
                colors[white], colors[blue] = colors[blue], colors[white]

            blue -= 1

    return colors

def reverse_words(sentence):
   sentence = re.sub(' +',' ',sentence.strip())

   sentence = list(sentence)
   str_len = len(sentence)

   str_rev(sentence, 0, str_len - 1)

   start = 0
   end = 0

   while (start < str_len):
    while end < str_len and sentence[end] != ' ':
        end += 1
    str_rev(sentence, start, end - 1)
    start = end + 1;
    end += 1

   return ''.join(sentence)

def str_rev(_str, start_rev, end_rev):
   while start_rev < end_rev:
       temp = _str[start_rev]       
       _str[start_rev] = _str[end_rev] 
       _str[end_rev] = temp           

       start_rev += 1       
       end_rev -= 1    


def is_happy_number(n):

    # Helper function that calculates the sum of squared digits.
    def sum_of_squared_digits(number):
        total_sum = 0
        while number > 0:
            number, digit = divmod(number, 10)
            total_sum += digit ** 2
        return total_sum

    slow_pointer = n 
    fast_pointer = sum_of_squared_digits(n)  

    while fast_pointer != 1 and slow_pointer != fast_pointer: 
        slow_pointer = sum_of_squared_digits(slow_pointer)
        fast_pointer = sum_of_squared_digits(sum_of_squared_digits(fast_pointer))

    if(fast_pointer == 1):
        return True
    return False

def detect_cycle(head):
    if head is None:
        return False

    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

def get_middle_node(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def circular_array_loop(nums):
    size = len(nums)

    for i in range(size):
        slow = fast = i
        forward = nums[i] > 0

        while True:
            slow = next_step(slow, nums[slow], size)
            if is_not_cycle(nums, forward, slow):
                break

            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break

            fast = next_step(fast, nums[fast], size)
            if is_not_cycle(nums, forward, fast):
                break

            if slow == fast:
                return True

    return False

def next_step(pointer, value, size):
    result = (pointer + value) % size
    if result < 0:
        result += size
    return result

def is_not_cycle(nums, prev_direction, pointer):
    curr_direction = nums[pointer] >= 0
    if (prev_direction != curr_direction) or (abs(nums[pointer] % len(nums)) == 0):
        return True
    else:
        return False


def find_duplicate(nums):
    fast = slow = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return fast

def palindrome(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    revert_data = reverse_linked_list(slow)
    check = compare_two_halves(head, revert_data)

    revert_data = reverse_linked_list(revert_data)

    if check:
        return True
    return False

def compare_two_halves(first_half, second_half):
    while first_half and second_half:
        if first_half.data != second_half.data:
            return False
        else:
            first_half = first_half.next
            second_half = second_half.next
    return True


def find_repeated_sequences(s, k):
    window_size = k
    if len(s) <= window_size:
        return set()
    base = 4
    hi_place_value = pow(base, window_size - 1)
    mapping = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    numbers = []
    for i in range(len(s)):
        numbers.append(mapping.get(s[i]))
    hashing = 0
    substring_hashes, output = set(), set()
    for start in range(len(s) - window_size + 1):
        if start != 0:
            hashing = (hashing - numbers[start - 1] * hi_place_value) * base \
                + numbers[start + window_size - 1]
        else:
            for end in range(window_size):
                hashing = hashing * base + numbers[end]
        if hashing in substring_hashes:
            output.add(s[start:start + window_size])
        substring_hashes.add(hashing)
    return output


# function to clean up the deque
def clean_up(i, current_window, nums):
    while current_window and nums[i] >= nums[current_window[-1]]:
        current_window.pop()

# function to find the maximum in all possible windows
def find_max_sliding_window(nums, w):
    if len(nums) == 0:
        return []
    output = []
    current_window = deque()
    if w > len(nums):
        w = len(nums)
    for i in range(w):
        clean_up(i, current_window, nums)
        current_window.append(i)
    output.append(nums[current_window[0]])
    for i in range(w, len(nums)):
        clean_up(i, current_window, nums)
        if current_window and current_window[0] <= (i - w):
            current_window.popleft()
        current_window.append(i)
        output.append(nums[current_window[0]])
    return output


def min_window(str1, str2):
    size_str1, size_str2 = len(str1), len(str2)
    min_sub_len = float('inf')
    index_s1, index_s2 = 0, 0
    min_subsequence = ""
    while index_s1 < size_str1:
        if str1[index_s1] == str2[index_s2]:
            index_s2 += 1
            if index_s2 == size_str2:
                start, end = index_s1, index_s1
                index_s2 -= 1
                while index_s2 >= 0:
                    if str1[start] == str2[index_s2]:
                        index_s2 -= 1
                    start -= 1
                start += 1
                if end - start < min_sub_len:
                    min_sub_len = end - start
                    min_subsequence = str1[start:end+1]
                index_s1 = start
                index_s2 = 0
        index_s1 += 1
    return min_subsequence


def longest_repeating_character_replacement(s, k):
    string_length = len(s)
    length_of_max_substring = 0
    start = 0
    char_freq = {}
    most_freq_char = 0

    for end in range(string_length):
        if s[end] not in char_freq:
            char_freq[s[end]] = 1
        else:
            char_freq[s[end]] += 1

        most_freq_char = max(most_freq_char, char_freq[s[end]])

        if end - start + 1 - most_freq_char > k:
            char_freq[s[start]] -= 1
            start += 1

        length_of_max_substring = max(end - start + 1, length_of_max_substring)

    return length_of_max_substring

def min_window(s, t):
    if t == "":
        return ""

    req_count = {}
    window = {}

    for c in t:
        req_count[c] = 1 + req_count.get(c, 0)

    for c in t:
        window[c] = 0

    current, required = 0, len(req_count)

    res, res_len = [-1, -1], float("infinity")

    left = 0
    for right in range(len(s)):
        c = s[right]

        if c in t:
            window[c] = 1 + window.get(c, 0)

        if c in req_count and window[c] == req_count[c]:
            current += 1

        while current == required:
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = (right - left + 1)

            if s[left] in t:
                window[s[left]] -= 1

            if s[left] in req_count and window[s[left]] < req_count[s[left]]:
                current -= 1
            left += 1
    left, right = res

    return s[left:right+1] if res_len != float("infinity") else ""


def find_longest_substring(input_str):
    if len(input_str) == 0:
        return 0

    window_start, longest, window_length = 0, 0, 0

    last_seen_at = {}

    for index, val in enumerate(input_str):
        if val not in last_seen_at:
            last_seen_at[val] = index
        else:
            if last_seen_at[val] >= window_start:
                window_length = index - window_start
                if longest < window_length:
                    longest = window_length
                window_start = last_seen_at[val] + 1

            last_seen_at[val] = index

    index += 1

    if longest < index - window_start:
        longest = index - window_start

    return longest


def min_sub_array_len(target, nums):
    window_size = float('inf')
    start = 0
    sum = 0
    for end in range(len(nums)):
        sum += nums[end]
        while sum >= target:
            curr_subarr_size = (end + 1) - start
            window_size = min(window_size, curr_subarr_size)
            sum -= nums[start]
            start += 1

    if window_size != float('inf'):
        return window_size

    return 0


def insert_interval(existing_intervals, new_interval):
    new_start, new_end = new_interval.start, new_interval.end
    i = 0
    n = len(existing_intervals)
    output = []
    while i < n and existing_intervals[i].start < new_start:
        output.append(existing_intervals[i])
        i = i + 1
    if not output or output[-1].end < new_start:
        output.append(new_interval)
    else:
        output[-1].end = max(output[-1].end, new_end)
    while i < n:
        ei = existing_intervals[i]
        start, end = ei.start, ei.end
        if output[-1].end < start:
            output.append(ei)
        else:
            output[-1].end = max(output[-1].end, end)
        i += 1
    return output


def intervals_intersection(interval_list_a, interval_list_b):
    intersections = []
    i = j = 0

    while i < len(interval_list_a) and j < len(interval_list_b):
        start = max(interval_list_a[i].start, interval_list_b[j].start)
        end = min(interval_list_a[i].end, interval_list_b[j].end)

        if start <= end:
            intersections.append(Interval(start, end))

        if interval_list_a[i].end < interval_list_b[j].end:
            i += 1
        else:
            j += 1

    return intersections


ef employee_free_time(schedule):
    heap = []

    for i in range(len(schedule)):
        heap.append((schedule[i][0].start, i, 0))

    heapq.heapify(heap)

    result = []
    previous = schedule[heap[0][1]][heap[0][2]].start

    while heap:
        _, i, j = heapq.heappop(heap)
        interval = schedule[i][j]

        if interval.start > previous:
            result.append(Interval(previous, interval.start))

        previous = max(previous, interval.end)

        if j + 1 < len(schedule[i]):
            heapq.heappush(heap, (schedule[i][j+1].start, i, j+1))

    return result


def least_time(tasks, n):
    frequencies = {}

    for t in tasks:
        frequencies[t] = frequencies.get(t,0) + 1

    frequencies = dict(sorted(frequencies.items(), key=lambda x:x[1]))
    max_freq = frequencies.popitem()[1]
    idle_time = (max_freq - 1) * n

    while frequencies and idle_time > 0:
        idle_time -= min(max_freq - 1, frequencies.popitem()[1])
    idle_time = max(0, idle_time)

    return len(tasks) + idle_time

def reverse(head):
    prev, next = None, None
    curr = head

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    head = prev
    return head


def reorder_list(head):
    if not head:
        return head
    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev, curr = None, slow

    while curr:
        curr.next, prev, curr = prev, curr, curr.next
    first, second = head, prev

    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next

    return head

def swap_nodes(head, k):
    count = 0
    front, end = None, None
    curr = head

    while curr:
        count += 1
        if end is not None:
            end = end.next

        if count == k:
            front = curr
            end = head
        curr = curr.next

    swap(front, end)
    return head


def reverse_even_length_groups(head):
    prev = head
    l = 2

    while prev.next:
        node = prev
        n = 0
        for i in range(l):
            if not node.next:
                break
            n += 1
            node = node.next
        if n % 2:
            prev = node
        else:
            reverse = node.next
            curr = prev.next
            for j in range(n):
                curr_next = curr.next
                curr.next = reverse
                reverse = curr
                curr = curr_next
            prev_next = prev.next
            prev.next = node
            prev = prev_next
        l += 1

    return head

def maximum_capital(c, k, capitals, profits):
    current_capital = c
    capitals_min_heap = []
    profits_max_heap = []

    for x in range(0, len(capitals)):
        heappush(capitals_min_heap, (capitals[x], x))

    for _ in range(k):

        while capitals_min_heap and capitals_min_heap[0][0] <= current_capital:
            c, i = heappop(capitals_min_heap)
            heappush(profits_max_heap, (-profits[i], i))
        
        if not profits_max_heap:
            break

        j = -heappop(profits_max_heap)[0]
        current_capital = current_capital + j

    return current_capital


def merge_sorted(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    x = 0
    for p in range(n + m - 1, -1, -1):
        if p2 < 0:
            break
        x += 1
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
    return nums1


def k_smallest_number(lists, k):
    list_length = len(lists)
    kth_smallest = []

    for index in range(list_length):
        if len(lists[index]) == 0:
            continue
        else:
            heappush(kth_smallest, (lists[index][0], index, 0))

    numbers_checked, smallest_number = 0, 0
    while kth_smallest:  
        smallest_number, list_index, num_index = heappop(kth_smallest)
        numbers_checked += 1

        if numbers_checked == k:
            break

        if num_index + 1 < len(lists[list_index]):
            heappush(
                kth_smallest, (lists[list_index][num_index + 1], list_index, num_index + 1))

    return smallest_number


def k_smallest_pairs(list1, list2, k):
    list_length = len(list1)
    min_heap = []
    pairs = []

    for i in range(min(k, list_length)):
        heappush(min_heap, (list1[i] + list2[0], i, 0))

    counter = 1

    while min_heap and counter <= k:
        sum_of_pairs, i, j = heappop(min_heap)
        pairs.append([list1[i], list2[j]])

        next_element = j + 1

        if len(list2) > next_element:
            heappush(min_heap,
                     (list1[i] + list2[next_element], i, next_element))

        counter += 1

    return pairs


def kth_smallest_element(matrix, k):
    row_count = len(matrix)
    min_numbers = []

    for index in range(row_count):
        heappush(min_numbers, (matrix[index][0], index, 0))

    numbers_checked, smallest_element = 0, 0

    while min_numbers:
        smallest_element, row_index, col_index = heappop(min_numbers)
        numbers_checked += 1
        if numbers_checked == k:
            break
        if col_index + 1 < len(matrix[row_index]):
            heappush(min_numbers, (matrix[row_index][col_index + 1], row_index, col_index + 1))

    return smallest_element


def reorganize_string(str):

    char_counter = Counter(str)
    most_freq_chars = []

    for char, count in char_counter.items():
        most_freq_chars.append([-count, char])

    heapq.heapify(most_freq_chars)

    previous = None
    result = ""

    while len(most_freq_chars) > 0 or previous:

        if previous and len(most_freq_chars) == 0:
            return ""

        count, char = heapq.heappop(most_freq_chars)
        result = result + char
        count = count + 1

        if previous:
            heapq.heappush(most_freq_chars, previous)
            previous = None

        if count != 0:
            previous = [count, char]

    return result


def k_closest(points, k):
    points_max_heap = []

    for i in range(k):
        heapq.heappush(points_max_heap, points[i])

    for i in range(k, len(points)):
        if points[i].distance_from_origin() \
         < points_max_heap[0].distance_from_origin():
            heapq.heappop(points_max_heap)
            heapq.heappush(points_max_heap, points[i])

    return list(points_max_heap)


def binary_search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = low + ((high - low) // 2)
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            high = mid - 1
        elif target > nums[mid]:
            low = mid + 1

    return -1


def binary_search_rotated(nums, target):
    low = 0
    high = len(nums) - 1

    if low > high:
        return -1

    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid

        if nums[low] <= nums[mid]:
            if nums[low] <= target and target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] < target and target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


def first_bad_version(n):
    first = 1
    last = n
    calls = 0
    while first < last:
        mid = first + (last - first) // 2;
        if is_bad_version(mid):
            last = mid
        else:
            first = mid + 1
        calls += 1
    return first, calls


def single_non_duplicate(nums):
    l = 0
    r = len(nums) - 1

    while l != r:
        mid = l + (r - l) // 2

        if mid % 2 == 1:
            mid -= 1

        if nums[mid] == nums[mid + 1]:
            l = mid + 2
        else :
            r = mid

    return nums[l]


def rescue_boats(people, limit):

    people.sort()

    left = 0
    right = len(people) - 1

    boats = 0

    while left <= right:

        if people[left] + people[right] <= limit:
            left += 1

        right -= 1

        boats += 1
    return boats


def gas_station_journey(gas, cost):

    if sum(cost) > sum(gas):
        return -1

    current_gas, starting_index = 0, 0

    for i in range(len(gas)):

        current_gas = current_gas + (gas[i] - cost[i])

        if current_gas < 0:
            current_gas = 0
            starting_index = i + 1

    return starting_index


def two_city_scheduling(costs):
    total_cost = 0
    costs.sort(key = lambda x : x[0] - x[1])
    cost_length = len(costs)

    for i in range(cost_length//2):
        total_cost = total_cost + costs[i][0] + costs[cost_length-i-1][1];

    return total_cost


def min_refuel_stops(target, start_fuel, stations):
    if start_fuel >= target:
        return 0

    max_heap = []
    i, n = 0, len(stations)
    stops = 0
    max_distance = start_fuel

    while max_distance < target:
        if i < n and stations[i][0] <= max_distance:
            heapq.heappush(max_heap, -stations[i][1])
            i += 1
        elif not max_heap:
            return -1
        else:
            max_distance += -heapq.heappop(max_heap)
            stops += 1

    return stops


def jump_game_two(nums):
    current, furthest, jumps = 0, 0, 0

    for i, v in enumerate(nums):
        furthest = max(furthest, i + v)
        if i == current and i < len(nums) - 1:
            jumps += 1
            current = furthest

    return jumps


# This method determines if a queen can be placed at proposed_row, proposed_col
# with current solution i.e. this move is valid only if no queen in current
# solution may attack the square at proposed_row and proposed_col
def is_valid_move(proposed_row, proposed_col, solution):
    for i in range(0, proposed_row):
        old_row = i
        old_col = solution[i]
        diagonal_offset = proposed_row - old_row
        if (old_col == proposed_col or
            old_col == proposed_col - diagonal_offset or
                old_col == proposed_col + diagonal_offset):
            return False

    return True

# Recursive worker function
def solve_n_queens_rec(n, solution, row, results):
    if row == n:
        results.append(solution[:])
        return

    for i in range(0, n):
        valid = is_valid_move(row, i, solution)
        if valid:
            solution[row] = i
            solve_n_queens_rec(n, solution, row + 1, results)

# Function to solve N-Queens problem
def solve_n_queens(n):
    results = []
    solution = [-1] * n
    solve_n_queens_rec(n, solution, 0, results)
    return len(results)


def word_search(grid, word):
    n = len(grid)
    m = len(grid[0])
    for row in range(n):
        for col in range(m):
            if depth_first_search(row, col, word, grid):
                return True
    return False

# Apply backtracking on every element to search the required word
def depth_first_search(row, col, word, grid):
    if len(word) == 0:
        return True

    if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]) \
            or grid[row][col].lower() != word[0].lower():
        return False

    grid[row][col] = '*'

    for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        if depth_first_search(row + rowOffset, col + colOffset, word[1:], grid):
            return True

    grid[row][col] = word[0]

    return False


def flood_fill(grid, sr, sc, target):
    if grid[sr][sc] == target:
        return grid
    else:
        old_target = grid[sr][sc]
        grid[sr][sc] = target
        dfs(grid, sr, sc, old_target, target)

        return grid


def dfs(grid, row, col, old_target, new_target):
    adjacent_cells = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    grid_length = len(grid)
    total_cells = len(grid[0])

    for cell_value in adjacent_cells:
        i = row + cell_value[0]
        j = col + cell_value[1]

        if i < grid_length and i >= 0 and j < total_cells and j >= 0 and grid[i][j] == old_target:
            grid[i][j] = new_target
            dfs(grid, i, j, old_target, new_target)


def find_max_knapsack_profit(capacity, weights, values):
    # Create a table to hold intermediate values
    n = len(weights)
    dp = [[0 for i in range(capacity + 1)] for j in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, capacity + 1):

            # Check if the weight of the current item is less than the current capacity
            if weights[i-1] <= j:
                dp[i][j] = max(values[i-1] + dp[i-1][j-weights[i-1]], 
                              dp[i-1][j])
                            
            # We don't include the item if its weight is greater than the current capacity
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1] #[n][capacity]


def find_max_knapsack_profit(capacity, weights, values):
    n = len(weights)
    dp = [0] * (capacity + 1)

    for i in range(n):
        for j in range(capacity, weights[i] - 1, -1):
            dp[j] = max(values[i] + dp[j - weights[i]], dp[j])

    return dp[capacity]


def find_tribonacci(n):
    if n < 3:
        return 1 if n else 0

    first_num, second_num, third_num = 0, 1, 1
    for _ in range(n - 2):
        first_num, second_num, third_num = second_num, third_num, \
          first_num + second_num + third_num
    return third_num


def can_partition_array(nums):

    array_sum = sum(nums)

    if array_sum % 2 != 0:
        return False

    subset_sum = array_sum//2

    dp = [[False for i in range(len(nums)+1)] for j in range(subset_sum + 1)]

    for i in range(0, len(nums) + 1):
        dp[0][i] = True

    for i in range(1, subset_sum + 1):
        for j in range(1, len(nums)+1):
            if nums[j - 1] > i:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = dp[i - nums[j - 1]
                                      ][j - 1] or dp[i][j - 1]

    return dp[subset_sum][len(nums)]


def counting_bits(n):
    result = [0] * (n + 1)

    if n == 0:
        return result

    result[0] = 0
    result[1] = 1

    for x in range(2, n + 1):
        if x % 2 == 0:
            result[x] = result[x // 2]
        else:
            result[x] = result[x // 2] + 1

    return result


def update_matrix(mat):
    m, n = len(mat), len(mat[0])

    for r in range(m):
        for c in range(n):

            if mat[r][c] > 0:

                above = mat[r - 1][c] if r > 0 else math.inf

                left = mat[r][c - 1] if c > 0 else math.inf

                mat[r][c] = min(above, left) + 1

    for r in range(m - 1, -1, -1):
        for c in range(n - 1, -1, -1):

            if mat[r][c] > 0:

                below = mat[r + 1][c] if r < m - 1 else math.inf

                right = mat[r][c + 1] if c < n - 1 else math.inf

                mat[r][c] = min(mat[r][c], below + 1, right + 1)
    return mat


def max_product(nums):
    if len(nums) == 0:
        return 0

    max_so_far = nums[0]
    min_so_far = nums[0]
    result = max_so_far

    for i in range(1, len(nums)):
        curr = nums[i]

        temp_max_so_far = max(curr, max_so_far * curr, min_so_far * curr)
        min_so_far = min(curr, max_so_far * curr, min_so_far * curr)
        max_so_far = temp_max_so_far

        result = max(max_so_far, result)

    return result


def combination_sum(nums, target):
    dp = [[] for _ in range(target + 1)]
    dp[0].append([])

    for i in range(1, target + 1):
        for j in range(len(nums)):
            if nums[j] <= i:

                for prev in dp[i - nums[j]]:
                    temp = prev + [nums[j]]
                    temp.sort()
                    if temp not in dp[i]:
                        dp[i].append(temp)
    return dp[target]


def count_palindromic_substrings(s):
    count = 0

    dp = [[False for i in range(len(s))] for i in range(len(s))]

    for i in range(len(s)):
        dp[i][i] = True
        count += 1

    for i in range(len(s)-1):
        dp[i][i + 1] = (s[i] == s[i + 1])
        count += dp[i][i + 1]

    for length in range(3, len(s)+1):
        i = 0
        for j in range(length - 1, len(s)):
            dp[i][j] = dp[i + 1][j - 1] and (s[i] == s[j])
            count += dp[i][j]
            i += 1

    return count


def word_break(s, word_dict):
    dp = [[]] * (len(s) + 1)
    dp[0] = [""]

    for i in range(1, len(s) + 1):

        prefix = s[:i]

        temp = []

        for j in range(0, i):
            suffix = prefix[j:]

            if suffix in word_dict:

                for substring in dp[j]:
                    temp.append((substring + " " + suffix).strip())

        dp[i] = temp

    return dp[len(s)]


def find_missing_number(nums):
    len_nums = len(nums)
    index = 0

    while index < len_nums:
        value = nums[index]

        if value < len_nums and value != nums[value]:
            nums[index], nums[value] = nums[value], nums[index]

        elif value >= len_nums:
            index+=1

        else:
            index += 1

    for x in range(len_nums):
        if x != nums[x]:
            return x
    return len_nums


def find_corrupt_pair(nums):
    missing = None
    duplicated = None

    def swap(arr, first, second):
        arr[first], arr[second] = arr[second], arr[first]

    i = 0
    while i < len(nums):
        correct = nums[i] - 1
        if nums[i] != nums[correct]:
            swap(nums, i, correct)
        else:
            i += 1

    for j in range(len(nums)):
        if nums[j] != j + 1:
            duplicated = nums[j]
            missing = j + 1

    return missing, duplicated


def find_compilation_order(dependencies):
    sorted_order = []
    graph = {}
    inDegree = {}
    for x in dependencies:
        parent, child = x[1], x[0]
        graph[parent], graph[child] = [], []
        inDegree[parent], inDegree[child] = 0, 0
    if len(graph) <= 0:
        return sorted_order


    for dependency in dependencies:
        parent, child = dependency[1], dependency[0]
        graph[parent].append(child)
        inDegree[child] += 1

    sources = deque()
    for key in inDegree:
        if inDegree[key] == 0:
            sources.append(key)

    while sources:
        vertex = sources.popleft()
        sorted_order.append(vertex)
        for child in graph[vertex]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    if len(sorted_order) != len(graph):
        return []
    return sorted_order


def alien_order(words):
    adj_list = defaultdict(set)
    counts = Counter({c: 0 for word in words for c in word})
    outer = 0
    for word1, word2 in zip(words, words[1:]):
        outer += 1
        inner = 0
        for c, d in zip(word1, word2):
            inner += 1
            if c != d:
                if d not in adj_list[c]:
                    adj_list[c].add(d)
                    counts[d] += 1
                break

        else:
            if len(word2) < len(word1):
                return ""


    result = []
    sources_queue = deque([c for c in counts if counts[c] == 0])
    while sources_queue:
        c = sources_queue.popleft()
        result.append(c)

        for d in adj_list[c]:
            counts[d] -= 1
            if counts[d] == 0:
                sources_queue.append(d)

    if len(result) < len(counts):
        return ""
    return "".join(result)


def set_matrix_zeros(mat):
	rows = len(mat)
	cols = len(mat[0])
	fcol = False
	frow = False

	for i in range(rows):
		if mat[i][0] == 0:
			fcol = True

	for i in range(cols):
		if mat[0][i] == 0:
			frow = True

	for i in range(1, rows):
		for j in range(1, cols):
			if mat[i][j] == 0:
				mat[0][j] = mat[i][0] = 0

	for i in range(1, rows):
		if mat[i][0] == 0:
			for j in range(1, cols):
				mat[i][j] = 0

	for j in range(1, cols):
		if mat[0][j] == 0:
			for i in range(1, rows):
				mat[i][j] = 0

	if fcol:
		for i in range(rows):
			mat[i][0] = 0

	if frow:
		for j in range(cols):
			mat[0][j] = 0
	return mat


def rotate_image(matrix):
    n = len(matrix)
    for row in range(n // 2):
        for col in range(row, n - row - 1):
            matrix[row][col], matrix[col][n - 1 - row] = matrix[col][n - 1 - row], matrix[row][col]
            matrix[row][col], matrix[n - 1 - row][n - 1 - col] = matrix[n - 1 - row][n - 1 - col], matrix[row][col]
            matrix[row][col], matrix[n - 1 - col][row] = matrix[n - 1 - col][row], matrix[row][col]
    return matrix


def find_exit_column(grid):
    result = [-1]*len(grid[0])

    for col in range(len(grid[0])):
        current_col = col;

        for row in range(len(grid)):
            next_col = current_col + grid[row][current_col]

            if next_col < 0 or next_col > len(grid[0])-1 or grid[row][current_col] != grid[row][next_col]:
                break

            if row == len(grid)-1:
                result[col] = next_col
            current_col = next_col
    return result


def remove_duplicates(string):
    stack = []
    for char in string:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


def min_remove_parentheses(s):
    stack = []
    s_list = list(s)

    for i, val in enumerate(s):
        if len(stack) > 0 and stack[-1][0] == '(' and val == ')':
            stack.pop()

        elif val == '(' or val == ')':
            stack.append([val, i])

    for p in stack:
        s_list[p[1]] = ""

    result = ''.join(s_list)

    return result


def exclusive_time(n, logs):
    logs_stack = []
    result = [0]*n

    for content in logs:
        logs = Log(content)
        if logs.is_start:
            logs_stack.append(logs)
        else:
            top = logs_stack.pop()
            result[top.id] += (logs.time - top.time + 1)
            if logs_stack:
                result[logs_stack[-1].id] -= (logs.time - top.time + 1)
    return result


class NestedIterator:

    # NestedIterator constructor initializes the stack using the
    # given nested_list list
    def __init__(self, nested_list):
        self.nested_list_stack = list(reversed(nested_list))

    # has_next() will return True if there are still some integers in the
    # stack (that has nested_list elements) and, otherwise, will return False.
    def has_next(self):
        while len(self.nested_list_stack) > 0:
            top = self.nested_list_stack[-1]
            if top.is_integer():
                return True

            top_list = self.nested_list_stack.pop().get_list()

            i = len(top_list) - 1
            while i >= 0:
                self.nested_list_stack.append(top_list[i])
                i -= 1
        return False

    # next will return the integer from the nested_list
    def next(self):
        if self.has_next():
            return self.nested_list_stack.pop().get_integer()
        return None


def network_delay_time(times, n, k):
    adjacency = defaultdict(list)
    for src, dst, t in times:
        adjacency[src].append((dst, t)) 

    pq = PriorityQueue()
    pq.put((0, k)) 
    visited = set() 
    delays = 0   
      
    while not pq.empty():
        time, node = pq.get()
      
        if node in visited:
            continue
          
        visited.add(node)  
        delays = max(delays, time) 
        neighbours = adjacency[node]

        for neighbour in neighbours:
            neighbour_node, neighbour_time = neighbour
            if neighbour_node not in visited:
                new_time =  time + neighbour_time
                pq.put((new_time, neighbour_node))
  
    if len(visited) == n:
        return delays

    return -1


def number_of_paths(n, corridors):
    neighbours = defaultdict(set)
    cycles = 0

    for room1, room2 in corridors:
        neighbours[room1].add(room2)
        neighbours[room2].add(room1)
        cycles += len(neighbours[room1].intersection(neighbours[room2]))

    return cycles


def clone_helper(root, nodes_completed):
    if root == None:
      return None

    cloned_node = Node(root.data)
    nodes_completed[root] = cloned_node

    for p in root.neighbors:
      x = nodes_completed.get(p)
      if not x:
        cloned_node.neighbors += [clone_helper(p, nodes_completed)]
      else:
        cloned_node.neighbors += [x]
    return cloned_node

def clone(root):
    nodes_completed = {}
    return clone_helper(root, nodes_completed)


def valid_tree(n, edges):
    if (len(edges) != (n - 1)):
      return False

    adjacency = []
    for i in range(n):
        adjacency.append([])

    for x, y in edges:
        adjacency[x].append(y)
        adjacency[y].append(x)

    visited = {0}
    stack = [0]

    while stack:
        node = stack.pop()
        for neighbor in adjacency[node]:
            if neighbor in visited:
                continue

            visited.add(neighbor)
            stack.append(neighbor)

    if len(visited) == n:
        return True

    return False


def minimum_buses(routes, src, dest):

  adj_list = {}
  for i, stations in enumerate(routes):
    for station in stations:
      if station not in adj_list:
        adj_list[station] = []
      adj_list[station].append(i)

  queue = deque()
  queue.append([src,0])
  visited_buses = set()

  while queue:
    station, buses_taken = queue.popleft()
    if station == dest:
      return buses_taken

    if station in adj_list:
      for bus in adj_list[station]:
        if bus not in visited_buses:
          for s in routes[bus]:
            queue.append([s, buses_taken+1])
          visited_buses.add(bus)

  return -1


def flatten_tree(root):
    if not root:
        return
    
    current = root
    while current:

        if current.left:
            last = current.left

            while last.right:
                last = last.right
            
            last.right = current.right
            current.right = current.left
            current.left = None

        current = current.right
    return root


def build_tree_helper(p_order, i_order, left, right, mapping, p_index):
    if left > right:
        return None

    curr = p_order[p_index[0]]
    p_index[0] += 1
    root = TreeNode(curr)

    if left == right:
        return root

    in_index = mapping[curr]

    root.left = build_tree_helper(p_order, i_order, left, in_index - 1, mapping, p_index)
    root.right = build_tree_helper(p_order, i_order, in_index + 1, right, mapping, p_index)

    return root

def build_tree(p_order, i_order):
    p_index = [0]
    mapping = {}

    for i in range(len(p_order)):
        mapping[i_order[i]] = i

    return build_tree_helper(p_order, i_order, 0, len(p_order) - 1, mapping, p_index)


def populate_next_pointers(root):
    if not root:
        return root

    mostleft = root

    while mostleft.left:

        current = mostleft

        while current:

            current.left.next = current.right

            if current.next:

                current.right.next = current.next.left

            current = current.next

        mostleft = mostleft.left

    return root


def word_ladder(src, dest, words):
    myset = set(words)

    if dest not in myset:
        return 0

    q = []
    q.append(src)
    length = 0

    while q:
        length += 1
        size = len(q)

        for _ in range(size):
            curr = q.pop(0)

            for i in range(len(curr)):
                alpha = "abcdefghijklmnopqrstuvwxyz"

                for c in alpha:
                    temp = list(curr)
                    temp[i] = c
                    temp = "".join(temp)

                    if temp == dest:
                        return length + 1

                    if temp in myset:
                        q.append(temp)
                        myset.remove(temp)
    return 0


def replace_words(sentence, dictionary):
    trie = Trie()

    for prefix in dictionary:
        trie.insert(prefix)

    new_list = sentence.split()

    for i in range(len(new_list)):

        new_list[i] = trie.replace(new_list[i])

    return " ".join(new_list)


class RequestLogger:

    # initailization of requests hash map
    def __init__(self, time_limit):
        self.requests = {}
        self.limit = time_limit

    # function to accept and deny message requests
    def message_request_decision(self, timestamp, request):

        if request not in self.requests or timestamp - self.requests[request] >= self.limit:
            self.requests[request] = timestamp
            return True

        else:
            return False


class TicTacToe:
    # TicTacToe class contains rows, cols, diagonal,
    # and anti_diagonal to create a board.
    # Constructor is used to create board of size n * n.
    def __init__(self, n):
        self.rows = [0] * (n)
        self.cols = [0] * (n)
        self.diagonal = 0
        self.anti_diagonal = 0

    # move function will allow the players to play the game
    # by placing their mark at the row and col of their choice.
    def move(self, row, col, player):
        current_player = -1
        if player == 1:
            current_player = 1
        
        n = len(self.rows)

        self.rows[row] += current_player
        self.cols[col] += current_player

        if row == col:
            self.diagonal += current_player

        if col == (n - row - 1):
            self.anti_diagonal += current_player

        if abs(self.rows[row]) == n or abs(self.cols[col]) == n or abs(self.diagonal) == n or abs(self.anti_diagonal) == n:
            return player
        return 0


class FreqStack:

    # Use constructor to initialize the FreqStack object
    def __init__(self):
        self.frequency = defaultdict(int)
        self.group = defaultdict(list)
        self.max_frequency = 0

    # Use push function to push the value into the FreqStack
    def push(self, value):
        freq = self.frequency[value] + 1
        self.frequency[value] = freq
        
        if freq > self.max_frequency:
            self.max_frequency = freq
        
        self.group[freq].append(value)

    def pop(self):
        value = ""

        if self.max_frequency > 0:    
            value = self.group[self.max_frequency].pop()
            self.frequency[value] -= 1

            if not self.group[self.max_frequency]:
                self.max_frequency -= 1
        else:
            return -1

        return value


def longest_palindrome(words):
    # The built-in counter method is used to count the
    # Frequencies of each word
    frequencies = Counter(words)
    count = 0
    central = False

    for word, frequency in frequencies.items():
        # If word is a palindrome
        if word[0] == word[1]:
            # If a word has even occurrences
            if frequency % 2 == 0:
                count += frequency
            # If a word has odd occurrences
            else:
                count += frequency - 1
                central = True

        # If word is not a palindrome
        # Ensuring that a word and its reverse is only considered once
        elif word[1] > word[0]:
            # Get the minimum of the occurrences of the word and its reverse
            count += 2 * min(frequency, frequencies[word[1] + word[0]])

    if central:
        count += 1

    return 2 * count


class UnionFind:
    # Constructor
    def __init__(self):
        self.parents = {}
        self.ranks = {}

    # Function to find which group a particular element belongs.
    def find(self, coordinate):
        if coordinate != self.parents[coordinate]:
            self.parents[coordinate] = self.find(self.parents[coordinate])
        return self.parents[coordinate]

    # Function to join two coordinates into a single one.
    def union(self, x, y):
        # Set the parent of each coordinate to itself
        # if not already present in the dictionary

        self.parents.setdefault(x, x)
        self.parents.setdefault(y, y)

        # Set the ranks of each coordinate to 0
        # if not already present in the dictionary
        self.ranks.setdefault(x, 0)
        self.ranks.setdefault(y, 0)

        # Compare the ranks of the two coordinates
        # to decide which should be the parent

        if self.ranks[x] > self.ranks[y]:
            self.parents[self.find(y)] = self.find(x)
        elif self.ranks[y] > self.ranks[x]:
            self.parents[self.find(x)] = self.find(y)

         # If the rankss are equal, choose one coordinate
         # as the parent and increment its ranks
        else:
            self.parents[self.find(x)] = self.find(y)
            self.ranks[y] += 1

def remove_stones(stones):

    offset = 100000
    stone = UnionFind()

    for x, y in stones:
        stone.union(x, (y + offset))

    groups = set()
    for i in stone.parents:
        groups.add(stone.find(i))

    return len(stones) - len(groups)


def find_index(current_row, current_col, cols):
    return current_row * cols + (current_col + 1)

# checks whether the water cells to be connected are within the bounds of the matrix as per given dimensions
def within_bounds(row, col, rows, cols):
    if not (0 <= col < cols): return False
    if not (0 <= row < rows): return False
    return True

def last_day_to_cross(rows: int, cols: int, water_cells):

    day = 0
    matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    left_node, right_node = 0, rows * cols + 1
    water_directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    water_cells = [(r - 1, c - 1) for r, c in water_cells]
    uf = UnionFind(rows * cols + 2)

    for row, col in water_cells:
        matrix[row][col] = 1

        for dr, dc in water_directions:
            if within_bounds(row + dr, col + dc, rows, cols) and matrix[row + dr][col + dc] == 1:
                uf.union(find_index(row, col, cols), find_index((row + dr), (col + dc), cols))
        if col == 0:
            uf.union(find_index(row, col, cols), left_node)
        if col == cols - 1:
            uf.union(find_index(row, col, cols), right_node)

        if uf.find(left_node) == uf.find(right_node):
            break
        day += 1
    return day


def accounts_merge(accounts):
    # initialize a constructor that will create the parents array with unique IDs
    uf = UnionFind(len(accounts))

    # create a map for mapping emails to their parent IDs
    email_mapping = {}
    for i, account in enumerate(accounts):
        emails = account[1:]
        for email in emails:

            # if the email already exists in the map, take union
            if email in email_mapping:

                # before we take the union, make sure both the accounts have the same name
                if account[0] != accounts[email_mapping[email]][0]:
                    return
                uf.union(email_mapping[email], i)

            # add email with its ID to the map
            email_mapping[email] = i

    # create a map to store the merged accounts
    merged_accounts = defaultdict(list)
    for email, ids in email_mapping.items():
        merged_accounts[uf.find(ids)].append(email)

    # sort the merged accounts
    final_merged =[]
    for parent, emails in merged_accounts.items():
        final_merged.append([accounts[parent][0]]+sorted(emails))
    return final_merged
