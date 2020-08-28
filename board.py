#  x | x | x
# ---|---|---
#  x | x | x
# ---|---|---
#  x | x | x


class Board:
    def __init__(self, playerSymbols=None, numPlayers=2, boardSize=3):
        self.numPlayers = numPlayers
        self.playerSymbols = playerSymbols
        self.boardSize = boardSize
        self.board = [[None, None, None] for i in range(self.boardSize)]
        self.remainingCells = set(range(1, self.boardSize * self.boardSize + 1))
        self.mappings = self.generateMappings()

        if self.numPlayers == 2 and self.playerSymbols is None:
            self.playerSymbols = ["x", "o"]

    def makeMove(self, icon, loc):
        """
        used to make a move and update the board accordingly

        :param icon: the symbol to place on the board ie, x, o
        :param loc: the cell assiated to the tic tac toe board
        :return boolean: True if the move was successful, False if not
        """
        attempting_move = True

        if loc in self.remainingCells:
            self.board[x][y] = icon
            return True

        else:
            print("Invalid Move")
            return False

    def generateMappings(self):
        """
        Used to generate a dict of each locs relate to which row/col.
        Should only be called when the board is generated
        :return: dict object

        """

        mappings = {}
        i = 1
        for x in range(self.boardSize):
            for y in range(self.boardSize):
                mappings[i] = (x, y)

        return mappings

    def __str__(self):
        pass

#  x | x | x
# ---|---|---
#  x | x | x
# ---|---|---
#  x | x | x
