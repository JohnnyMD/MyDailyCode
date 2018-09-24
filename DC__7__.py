"""
September 24, 2018

This problem was asked by <Facebook>.

Given the mapping  a=1, b=2, c=3, ... , z=26,  and an encoded message,
count the number of ways it can be decoded.

For example, the message, '111' would give <3>, since it could be decoded
as: 'aaa', 'ak' or 'ka'.

You can assume that the messages are decodable. For example, '0001' isn't allowed !
"""

def counter_helper(M):
    len_M_ = M.__len__()

    # if void message
    if (len_M_ == 0):
        return 1

    ris = 0

    # at least one symbol in the message <M>
    if (len_M_ > 0):
        ris += counter_helper(M[1:])    # recorsivly cal the function on 
                                        # all <M> but the first char

    # at least two symbols in the message <M>
    tmp = ""
    if (len_M_ > 1 and ( 0 < int(tmp + M[0] + M[1]) <= 26 )):
        ris += counter_helper(M[2:])    # recorsivly cal the function on
                                        # all <M> but the first two char

    return ris

def count_decoding_ways(M):
    """
    Given an encoded message, count the number of ways it can be decoded.
    (Given the mapping function: a=1, b=2, c=3, ... , z=26)

    Arguments:
        M {String} -- encoded message
    """
    
    len_M_ = M.__len__()
    if (len_M_ <= 1):
        return 1                # Void or one symbol message

    # invalid message
    if (M[0] == '0'):
        return None

    return counter_helper(M)

"""
    ========================================================================
    =============================== TESTING ================================
    ========================================================================
"""


print("\n'''=====================<Test 0 - begin>===================='''")

M = '0001'
print("\nM = \'", M, "\'\n")

ris = count_decoding_ways(M)
print("count_decoding_ways(M) = <", ris, ">\n")

print("'''=====================<Test 0 - end>======================'''\n")




print("\n'''=====================<Test 1 - begin>===================='''")

M = '11111'
print("\nM = \'", M, "\'\n")

ris = count_decoding_ways(M)
print("count_decoding_ways(M) = <", ris, ">\n")

print("'''=====================<Test 1 - end>======================'''\n")



print("\n'''=====================<Test 2 - begin>===================='''")

M = '1234'
print("\nM = \'", M, "\'\n")

ris = count_decoding_ways(M)
print("count_decoding_ways(M) = <", ris, ">\n")

print("'''=====================<Test 2 - end>======================'''\n")



print("\n'''=====================<Test 3 - begin>===================='''")

M = '4321'
print("\nM = \'", M, "\'\n")

ris = count_decoding_ways(M)
print("count_decoding_ways(M) = <", ris, ">\n")

print("'''=====================<Test 3 - end>======================'''\n")
