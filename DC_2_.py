"""
This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


def two_num_sum_k(X, k):
    """
    Arguments:
        X {array of integers}    -- [integer numbers] [at least two: |X| >= 2]
        k {integer}              -- [number of steps to climb] [N >= 0]
    """

    # Test for a valid input
    if (X.__len__() <= 0):
        return False

    print("DEBUG: X =", X)
    
    # store the allready encountered numbers when passing over X
    cache_table = {}

    for x in X:
        # if I previously encountered the num. that summed with  x  gives  k, I return True 
        if (str(k-x) in cache_table):
            return True
        else:
            cache_table[str(x)] = True

    return  False


"""
    ========================================================================
    =============================== TESTING ================================
    ========================================================================
"""

print("\n'''=====================<Test 1 - begin>===================='''")

k = 4
X = [2, 1, 0, 2, 1, 0, 3]

ris = two_num_sum_k(X, k)

print("\nk =", k)
print("X =", X, "\n")
print("number_of_ways_to_climb_the_staircase = <", ris, "> \n")

print("'''=====================<Test 1 - end>======================'''\n")


print("\n'''=====================<Test 2 - begin>===================='''")

k = 4
X = [2, 1]

ris = two_num_sum_k(X, k)

print("\nk =", k)
print("X =", X, "\n")
print("number_of_ways_to_climb_the_staircase = <", ris, "> \n")

print("'''=====================<Test 2 - end>======================'''\n")


print("\n'''=====================<Test 3 - begin>===================='''")

k = 4
X = []

ris = two_num_sum_k(X, k)

print("\nk =", k)
print("X =", X, "\n")
print("number_of_ways_to_climb_the_staircase = <", ris, "> \n")

print("'''=====================<Test 3 - end>======================'''\n")


print("\n'''=====================<Test 4 - begin>===================='''")

k = 0
X = [0 ,0]

ris = two_num_sum_k(X, k)

print("\nk =", k)
print("X =", X, "\n")
print("number_of_ways_to_climb_the_staircase = <", ris, "> \n")

print("'''=====================<Test 4 - end>======================'''\n")
