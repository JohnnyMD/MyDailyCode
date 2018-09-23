"""
September 21, 2018

This problem was asked by <Stripe>.

Given an array of integers, find the first missing positive integer in -linear time- and -constant space-. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
"""

def find_the_lowest_missing_N(A):
    # Test for a valid input
    len_A = A.__len__()
    if (len_A <= 0):
        return 1

    # filter the array <A> from NON positive numbers (shift the positive num. in the first part of the array) 
    len_pos_A = 0
    for i in range(len_A):
        if (A[i] > 0):
            A[len_pos_A] = A[i]
            len_pos_A += 1

    #print("\nDEBUG: pos_A     =", A)
    #print("DEBUG: len_pos_A =", len_pos_A, "\n")

    # We know that <A> can fit a sequence of at most <len_pos_A> positive numbers. So, to find the lowest missing one, we a going to MARK (switch the sign) the index numbers of that sequence, that actually exists in the original array.
    # Ex:
    #   A = [ 1, 3, 5, 7,  -1, -3]  len_pos_A = 4 (after partitioning)
    #   A = [-1, 3,-5, 7,  -1, -3] --> the first index with an positive number 
    #                                  is <i=1>, so The searched number is <i+1 = 2>

    for i in range(len_pos_A):
        current_num = abs(A[i])
        if (current_num <= len_pos_A):
            # We found a number of the sequence --> mark it index
            # ( <abs()> used because the duplicates can exists in <A>)
            A[current_num - 1] = abs(A[current_num - 1]) * (-1)
    
    #print("\nDEBUG: pos_A     =", A)
    #print("DEBUG: len_pos_A =", len_pos_A, "\n")

    # At this point we have the marked array. So, we are going to searche our number in our sequence range
    ris = None
    for i in range(len_pos_A):
        if (A[i] > 0):
            ris = i + 1
            break

    # If no positive number in the sequence range, then the sequence is complete and we have to return <len_pos_A + 1> 
    if (ris == None):
        ris = len_pos_A + 1

    return ris

    # T = O(3N) = O(N)  -  linear time complexity;
    # We operate on the input array, so the space used is constant; 


"""
    ========================================================================
    =============================== TESTING ================================
    ========================================================================
"""

print("\n'''=====================<Test 1 - begin>===================='''")

A = [7, -3, -5, 1, -9, 2]      # 4

print("\nA =", A, "\n")

ris = find_the_lowest_missing_N(A)

print("find_the_lowest_missing_N = <", ris, ">\n")

print("'''=====================<Test 1 - end>======================'''\n")



print("\n'''=====================<Test 2 - begin>===================='''")

A = [7, 7, 7, -3, -5, 1, 1, 1, -9, 2]      # 4

print("\nA =", A, "\n")

ris = find_the_lowest_missing_N(A)

print("find_the_lowest_missing_N = <", ris, ">\n")

print("'''=====================<Test 2 - end>======================'''\n")



print("\n'''=====================<Test 3 - begin>===================='''")

A = [5]      # 4

print("\nA =", A, "\n")

ris = find_the_lowest_missing_N(A)

print("find_the_lowest_missing_N = <", ris, ">\n")

print("'''=====================<Test 3 - end>======================'''\n")



print("\n'''=====================<Test 4 - begin>===================='''")

A = []      # 4

print("\nA =", A, "\n")

ris = find_the_lowest_missing_N(A)

print("find_the_lowest_missing_N = <", ris, ">\n")

print("'''=====================<Test 4 - end>======================'''\n")



print("\n'''=====================<Test 5 - begin>===================='''")

A = [-1, 0]      # 4

print("\nA =", A, "\n")

ris = find_the_lowest_missing_N(A)

print("find_the_lowest_missing_N = <", ris, ">\n")

print("'''=====================<Test 5 - end>======================'''\n")
