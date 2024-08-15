class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # O(1) solution (since always a 9x9 board)

        # check if rows have duplicates

        for row in range(9):
            rownums = set()
            for col in range(9):
                cell = board[row][col]
                if cell in rownums:
                    return False
                if cell == '.':
                    continue
                else:
                    rownums.add(cell)
        
        # check if cols have duplicates

        for col in range(9):
            colnums = set()
            for row in range(9):
                cell = board[row][col]
                if cell in colnums:
                    return False
                if cell == '.':
                    continue
                else:
                    colnums.add(cell)
        
        # check if 3x3 sub-boxes have duplicates

        hashset = {(0,0): set(), (0,1): set(), (0,2): set(),
                   (1,0): set(), (1,1): set(), (1,2): set(),
                   (2,0): set(), (2,1): set(), (2,2): set()
                   }

        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell == '.':
                    continue
                if cell in hashset[(row // 3, col // 3)]:
                    return False    
                hashset[(row // 3, col // 3)].add(cell)

        return True