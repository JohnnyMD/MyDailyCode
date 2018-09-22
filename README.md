# MyDailyCoding
My solutions for Daily Coding problems (https://www.dailycodingproblem.com/)

DC__0__.py

    (17.09.2018)

    This problem was asked by <Amazon>:
    
      There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.

      For example, if N is 4, then there are 5 unique ways:
        1, 1, 1, 1
        2, 1, 1
        1, 2, 1
        1, 1, 2
        2, 2
      What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? 
      For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to take in X.
        

DC__1__.py
    
    (18.09.2018)
    
    This problem was recently asked by <Google>.

      Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
      For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
      Bonus: Can you do this in one pass? (Done !)


DC__2__.py
    
    (19.09.2018)
    
    This problem was asked by <Uber>.

      Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
      For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
      Follow-up: what if you can't use division? (Done !)


DC__3__.py
    
    (20.09.2018)

    This problem was asked by <Google>.

      Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

      For example, given the following Node class:

      class Node:
          def __init__(self, val, left=None, right=None):
              self.val = val
              self.left = left
              self.right = right

      The following test should pass:

      node = Node('root', Node('left', Node('left.left')), Node('right'))
      assert deserialize(serialize(node)).left.left.val == 'left.left'


DC__4__.py
    
    (21.09.2018)

    This problem was asked by <Stripe>.

      Given an array of integers, find the first missing positive integer in linear time and constant space. 
      In other words, find the lowest positive integer that does not exist in the array. 
      The array can contain duplicates and negative numbers as well.

      For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

      You can modify the input array in-place.
