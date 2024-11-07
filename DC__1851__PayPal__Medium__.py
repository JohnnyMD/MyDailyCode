'''
    --- --- ---  --- --- ---  --- --- --- ---  --- --- ---  --- --- ---
    [2024-11-02] Challenge #1851 - [Medium] - asked by PayPal
    --- --- ---  --- --- ---  --- --- --- ---  --- --- ---  --- --- ---

    Given a string and a number of lines k, print the string in zigzag form. In zigzag, characters are printed out diagonally from top left to bottom right until reaching the kth line, then back up to top right, and so on.

    For example, given the sentence "thisisazigzag" and k = 4, you should print:

    t     a     g           0|0                     0|6                     0|12
     h   s z   a                1|1             1|5     1|7             1|11
      i i   i z                     2|2     2|4             2|8     2|10
       s     g                          3|3                     3|9

'''

def zigzag_print(s: str, k: int) -> None:
    '''Prints the s word in zigzag over k lines.'''
    print(f"\ns = {s}, k = {k}")
    print(f"{'-'*32} SOL")
        
    if s is None or len(s) == 0 or k == 0:
        print(f"{'-'*32} SOL\n\n")
        return

    len_s = len(s)
    if k == 1:
        print(s)
        print(f"{'-'*32} SOL\n\n")
        return

    # Create a matrix: k rows & len(s) cols:
    m = create_empty_matrix(k, len_s)

    # Fill the letters in the right spots:
    direction = -1
    row = 0
    for i in range(len_s):
        # Revert the row filling direction when getting to the first of last row:
        if row == 0 or row == k - 1:
            direction *= -1
            if direction == 1:
                row = 0
            else:
                row = k-1
                       
        m[row][i] = s[i]
        row += direction

    print(matrix_to_string(m))

    print(f"{'-'*32} SOL\n\n")


def create_empty_matrix(rows, cols):
    '''create_empty_matrix with the given dimensions'''
    m = []
    for i in range(rows):
        m.append([])
        for j in range(cols):
            m[i].append(" ")
    return m

def matrix_to_string(m) -> str:
    '''Return the string representing the m matrix and stripping the trailing spaces in each row.'''
    res = ''
    for row in m:
        for item in row:
            res += item
        res = res.strip()
        res += "\n"
    return res[:len(res)-1].strip()
              


if __name__ == '__main__':
    print("\n'''=====================< START TESTS >===================='''")

    print("\n'''=====================<   Test 01   >===================='''")
    zigzag_print(None, 2)
    
    print("\n'''=====================<   Test 02   >===================='''")
    zigzag_print('thisisazigzag', 4)
    
    print("\n'''=====================<   Test 03   >===================='''")
    zigzag_print('thisisazigzag', 3)
    
    print("\n'''=====================<   Test 04   >===================='''")
    zigzag_print('thisisazigzag', 2)
    
    print("\n'''=====================<   Test 05   >===================='''")
    zigzag_print('thisisazigzag', 1)
    
    print("\n'''=====================<   Test 06   >===================='''")
    zigzag_print('', 1)
    
    print("\n'''=====================<   Test 07   >===================='''")
    zigzag_print('thisisazigzag', 10)
    
    print("\n'''=====================<   Test 08   >===================='''")
    zigzag_print('thisisazigzagzig', 5)
    
    print("\n'''=====================<  END TESTS  >===================='''")
