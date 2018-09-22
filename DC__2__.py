"""
September 19, 2018

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def smart_array(X):
    # Test for a valid input
    if (X.__len__() <= 0):
        return []
    
    # No numbers arround the single number in X
    if (X.__len__() == 1):
        return [0]
    
    
    ris = []

    # 1st PASS - consider the numbers on the left side the i-th number
    bag = 1
    for x in X:
        ris.append(bag)
        bag *= x
    #print("DEBUG: ris_1st_pass =", ris, "\n")


    # 2nd PASS - consider the numbers on the right side of the i-th number (iterating in reverse order)
    bag = 1
    for i in range(-1, -1*(len(X)+1), -1):
        ris[i] *= bag
        bag *= X[i]
    #print("DEBUG: ris_2nd_pass =", ris, "\n")

    return ris


"""
    ========================================================================
    =============================== TESTING ================================
    ========================================================================
"""

print("\n'''=====================<Test 1 - begin>===================='''")
X = [1, 2, 3, 4]

ris = smart_array(X)

print("X =", X, "\n")
print("smart_array = <", ris, "> \n")
print("'''=====================<Test 1 - end>======================'''\n")


print("\n'''=====================<Test 2 - begin>===================='''")
X = []

ris = smart_array(X)

print("X =", X, "\n")
print("smart_array = <", ris, "> \n")
print("'''=====================<Test 2 - end>======================'''\n")


print("\n'''=====================<Test 3 - begin>===================='''")
X = [0]

ris = smart_array(X)

print("X =", X, "\n")
print("smart_array = <", ris, "> \n")
print("'''=====================<Test 3 - end>======================'''\n")


print("\n'''=====================<Test 4 - begin>===================='''")
X = [0, 1, 2, 3, 4]

ris = smart_array(X)

print("X =", X, "\n")
print("smart_array = <", ris, "> \n")
print("'''=====================<Test 4 - end>======================'''\n")


print("\n'''=====================<Test 5 - begin>===================='''")
X = [0, 1, 2, 3, 4, 0]

ris = smart_array(X)

print("X =", X, "\n")
print("smart_array = <", ris, "> \n")
print("'''=====================<Test 5 - end>======================'''\n")


print("\n'''=====================<Test 6 - begin>===================='''")
X = [1, 2, 0, 3, 4]

ris = smart_array(X)

print("X =", X, "\n")
print("smart_array = <", ris, "> \n")
print("'''=====================<Test 6 - end>======================'''\n")


print("\n'''=====================<Test 7 - begin>===================='''")
X = [1, 2, 3, 4, 1, 2, 3, 4]

ris = smart_array(X)

print("X =", X, "\n")
print("smart_array = <", ris, "> \n")
print("'''=====================<Test 7 - end>======================'''\n")


print("\n'''=====================<Test 8 - begin>===================='''")
X = [2, 2, 2, 0, 2, 2, 2]

ris = smart_array(X)

print("X =", X, "\n")
print("smart_array = <", ris, "> \n")
print("'''=====================<Test 8 - end>======================'''\n")
