"""
    Monday, September 17, 2018

    There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

    For example, if N is 4, then there are 5 unique ways:

    1, 1, 1, 1
    2, 1, 1
    1, 2, 1
    1, 1, 2
    2, 2
    
    What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X ? 
    For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.

"""

def get_num_paths_recursive(N, sorted_X, current_path_sum):
    """Recursevelly compute the number off different possible ways to climb the staircase with N steps
    
    Arguments:
        N {natural number}                      -- [number of steps to climb] [N >= 0]
        sorted_X {sorted array of positive integers (N*) }    -- [you could climb any number from a set of positive integers X, no '0' and no duplicates here]
        current_path_sum {integer} -- [the current number of steps allready climbed] [initially 0]
    """

    if (current_path_sum == N):
        return 1
    
    if (current_path_sum > N):
        return 0

    else:
        local_ris_merge = 0
        for x in sorted_X:
            local_ris_merge += get_num_paths_recursive(N, sorted_X, current_path_sum + x)
        
        return local_ris_merge


def number_of_ways_to_climb_the_staircase(N, X):
    """
    Arguments:
        N {natural number}                      -- [number of steps to climb] [N >= 0]
        X {array of positive integers (N*) }    -- [you could climb any number from a set of positive integers X]
    """
    
    # Test for a valid input
    if (N <= 0):
        return 0

    # Create a sorted local copy of X (without '0' and duplicates)
    sorted_X = list(set(X))
    sorted_X.sort()
    if (sorted_X[0] == 0):
        sorted_X.pop(0)

    print("DEBUG: sorted_X =", sorted_X)

    if (sorted_X.__len__() <= 0):
        return 0

    return get_num_paths_recursive(N, sorted_X, 0)


"""
    ========================================================================
    =============================== TESTING ================================
    ========================================================================
"""

print("\n'''=====================<Test 1 - begin>===================='''")

N = 4
X = [2, 1, 0, 2, 1, 0, 3]

ris = number_of_ways_to_climb_the_staircase(N, X)

print("\nN =", N, "(steps)")
print("X =", X, "\n")
print("number_of_ways_to_climb_the_staircase = <", ris, "> (ways)\n")

print("'''=====================<Test 1 - end>======================'''\n")


print("\n'''=====================<Test 2 - begin>===================='''")

N = 7
X = [3, 4, 2, 5, 9]

ris = number_of_ways_to_climb_the_staircase(N, X)

print("\nN =", N, "(steps)")
print("X =", X, "\n")
print("number_of_ways_to_climb_the_staircase = <", ris, "> (ways)\n")

print("'''=====================<Test 2 - end>======================'''\n")


print("\n'''=====================<Test 3 - begin>===================='''")

N = 0
X = [3, 4, 2, 5]

ris = number_of_ways_to_climb_the_staircase(N, X)

print("\nN =", N, "(steps)")
print("X =", X, "\n")
print("number_of_ways_to_climb_the_staircase = <", ris, "> (ways)\n")

print("'''=====================<Test 3 - end>======================'''\n")


print("\n'''=====================<Test 4 - begin>===================='''")

N = 1
X = [0]

ris = number_of_ways_to_climb_the_staircase(N, X)

print("\nN =", N, "(steps)")
print("X =", X, "\n")
print("number_of_ways_to_climb_the_staircase = <", ris, "> (ways)\n")

print("'''=====================<Test 4 - end>======================'''\n")
