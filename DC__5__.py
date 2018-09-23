"""
September 22, 2018

This problem was asked by <Jane Street>.

cons(a, b) constructs a <pair>, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of 'cons':

    def cons(a, b):
        def pair(f):
            return f(a, b)
        return pair

Implement 'car' and 'cdr'.
"""


def cons(a, b):

    def pair(f):
        return f(a, b)

    return pair


# TODOS: it's all about functional programming !

def car(f):

    def first(a, b):
        return a

    return f(first)



def cdr(f):

    def last(a, b):
        return b

    return f(last)


""" My first aproach (Wrong !!!)
    
    def f(a, b):
        return (a, b)

    def cons(a, b):
        def pair(f):
            return f(a, b)
        return pair(f)



    def car(cons):
        return cons[0]


    def cdr(cons):
        return cons[1]
"""


"""
    ========================================================================
    =============================== TESTING ================================
    ========================================================================
"""

print("\n'''=====================<Test 1 - begin>===================='''")

sample_1_ = cons(3, 4)

print("\nsample_1_ =", sample_1_, "\n")


car_ris = car(cons(3, 4))
cdr_ris = cdr(cons(3, 4))

print("car_ris = <", car_ris, ">\ncdr_ris = <", cdr_ris, ">\n")


print("'''=====================<Test 1 - end>======================'''\n")
