#  x | x | x
# ---|---|---
#  x | x | x
# ---|---|---
#  x | x | x

"""
Checklist
finished init function
finsihed makeMove function
finished cell location to array position function

min board size 3, board size must be odd
"""
from constants import modes
from logic import Logic

class Board(Logic):
    def __init__(self, playerSymbols=None, boardSize=3, mode=modes["linear"]):
        self.numPlayers = 2
        self.playerSymbols = playerSymbols
        self.boardSize = boardSize
        self.mode = mode
        self.empty_square_symbol = " "

        self.board = [[None] * self.boardSize for _ in range(self.boardSize)]
        self.board_str = self.create_base_board()

        self.remainingCells = set(range(1, self.boardSize * self.boardSize + 1))


        # preforming checks on player symbols
        if self.playerSymbols is None:
            self.playerSymbols = ["x", "o"]

        elif len(set(self.playerSymbols)) <= 2:
            self.playerSymbols = list(set(self.playerSymbols))
            if "x" in self.playerSymbols:
                self.playerSymbols.append("o")
            else:
                self.playerSymbols.append("x")



    def makeMove(self, icon, loc):
        """
        Used to make a move and update the board accordingly. If the cell is
        already claimed then false is returned else true

        :param icon: the symbol to place on the board ie, x, o
        :param loc: the cell associated to the tic tac toe board
        :return boolean:
        """

        if loc in self.remainingCells:
            x, y = self.get_array_position(loc)
            self.board[x][y] = icon
            return True

        else:
            return False

    def get_array_position(self, loc):
        """
        Given the cell number of a board, the associated row and column indices are returned
        :param loc: the cell number
        :return tuple:
        """
        return (loc - 1) // self.boardSize, (loc - 1) % self.boardSize

    def create_base_board(self):
        """
        creates a list of strings that we can use .format on later.
        each string corresponds to a row
        :return list:
        """

        board = []
        for _ in range(self.boardSize):
            layer_base = ""
            for i in range(self.boardSize - 1):
                layer_base += " {" + str(i) + "} │"
            layer_base += " {" + str(self.boardSize - 1) + "} "



            board.append(layer_base)
            board.append("───┼" (* self.boardSize - 1) + "───")

        return board

    def display_board(self):
        if self.mode == modes["linear"]:
            for row in range(self.boardSize):
                print(self.board_str[row*2].format(*[self.empty_square_symbol if x is None else x for x in self.board[row]]))


        elif self.mode == modes["quadratic"]:
            pass


        pass

#  x | x | x
# ---|---|---
#  x | x | x
# ---|---|---
#  x | x | x
