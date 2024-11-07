'''
    --- --- ---  --- --- ---  --- --- --- ---  --- --- ---  --- --- ---
    [2023-03-22] Challenge #1356 - [Easy] - asked by Morgan Stanley
    --- --- ---  --- --- ---  --- --- --- ---  --- --- ---  --- --- ---
    
    In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".

    Given a binary tree, write an algorithm to print the nodes in boustrophedon order.

    For example, given the following tree:
    
               1
           /       \
          2         3
         / \       / \
        4   5     6   7
    
    You should return [1, 3, 2, 4, 5, 6, 7].
'''

def boustrophedon_traversal():
    '''Print the binary tree in boustrophedon order.'''
    
    pass

class TreeNode:
    '''Binary Tree Node class.'''
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def pretty_print_tree(root):
    '''Prints the binary tree in a pretty way.'''
    if not root:
        return

    def get_height(node):
        if not node:
            return 0
        return max(get_height(node.left), get_height(node.right)) + 1

    def print_level(nodes, level, max_level):
        if not any(nodes):
            return
        floor = max_level - level
        edge_lines = 2 ** max(floor - 1, 0)
        first_spaces = 2 ** floor - 1
        between_spaces = 2 ** (floor + 1) - 1

        print(' ' * first_spaces, end='')
        new_nodes = []
        for node in nodes:
            if node:
                print(node.value, end='')
                new_nodes.append(node.left)
                new_nodes.append(node.right)
            else:
                new_nodes.append(None)
                new_nodes.append(None)
                print(' ', end='')
            print(' ' * between_spaces, end='')
        print()
        for i in range(1, edge_lines + 1):
            for j in range(len(nodes)):
                print(' ' * (first_spaces - i), end='')
                if nodes[j] is None:
                    print(' ' * (edge_lines + edge_lines + i + 1), end='')
                    continue
                if nodes[j].left:
                    print('/', end='')
                else:
                    print(' ', end='')
                print(' ' * (i + i - 1), end='')
                if nodes[j].right:
                    print('\\', end='')
                else:
                    print(' ', end='')
                print(' ' * (edge_lines + edge_lines - i), end='')
            print()
        print_level(new_nodes, level + 1, max_level)

    height = get_height(root)
    print_level([root], 1, height)


if __name__ == '__main__':
    print("\n'''=====================< START TESTS >===================='''")

    print("\n'''=====================<   Test 01   >===================='''")
    test_binary_tree = TreeNode(1)
    test_binary_tree.left = TreeNode(2)
    test_binary_tree.right = TreeNode(3)
    test_binary_tree.left.left = TreeNode(4)
    test_binary_tree.left.right = TreeNode(5)
    test_binary_tree.right.left = TreeNode(6)
    test_binary_tree.right.right = TreeNode(7)
    pretty_print_tree(test_binary_tree)
    print(f"boustrophedon_traversal() = {boustrophedon_traversal()}")
    
    
    print("\n'''=====================<  END TESTS  >===================='''")
