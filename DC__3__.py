"""
This problem was asked by <Google>.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val   = val
        self.left  = left
        self.right = right

# A function to do inorder tree traversal


def printInorder(root):

    if root:

        # First recur on left child
        printInorder(root.left)

        # then print the data of node
        print(root.val),

        # now recur on right child
        printInorder(root.right)


#Z A function to do postorder tree traversal
def printPostorder(root):

    if root:

        # First recur on left child
        printPostorder(root.left)

        # the recur on right child
        printPostorder(root.right)

        # now print the data of node
        print(root.val),


# A function to do postorder tree traversal
def printPreorder(root):

    if root:

        # First print the data of node
        print(root.val)

        # Then recur on left child
        printPreorder(root.left)

        # Finally recur on right child
        printPreorder(root.right)



def serialize_helper(root):
    if root:
        global ris 
        ris += root.val
        serialize_helper(root.left) 
        serialize_helper(root.right)

def deserialize(s):
    pass


"""
    ========================================================================
    =============================== TESTING ================================
    ========================================================================
"""

print("\n'''=====================<Test 1 - begin>===================='''")

ris = ""

node = Node('root', Node('left', Node('left.left')), Node('right'))

print(ris)

#assert deserialize(serialize(node, "")).left.left.val == 'left.left'

print("'''=====================<Test 1 - end>======================'''\n")
