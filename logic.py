# from board import Board


class Logic():
    def __init__(self):
        pass

    def checkRowWinCase(self, icon, loc):
        """
        Checks if a player has won on the horizontal axis of the game
        if a winner was chosen, then returns True else False
        :param icon: The icon associated to a player
        :param loc: The cell number of the board where the last move was placed
        :return boolean:
        """

        x, _ = self.get_array_position(loc)
        for cell in self.board[x]:
            if icon != cell:
                return False

        return True

    def checkColumnWinCase(self, icon, loc):
        """
        Checks if a player has won on the vertical axis of the game
        if a winner was chosen, then returns True else False
        :param icon: The icon associated to a player
        :param loc: The cell number of the board where the last move was placed
        :return boolean:
        """

        _, y = self.get_array_position(loc)

        for r in range(self.boardSize):
            if icon != self.board[r][y]:
                return False

        return True

    def checkTopLeftBottomRightDiagonalCase(self, icon, loc):
        """
        Determines if there is a winning case on the top left to bottom right
        diagonal of the board
        :param icon: The icon associated to a player
        :param loc: The cell number of the board where the last move was placed
        :return boolean:
        """
        x, y = self.get_array_position(loc)

        # making sure the icon is on the diagonal first
        if x == y:
            for i in range(self.boardSize):
                if self.board[x][y] != icon:
                    return False

            return True

        else:
            return False

    def checkTopRightBottomLeftDiagonalCase(self, icon, loc):
        """
        Determines if there is a winning case on the top right to bottom left
        diagonal of the board
        :param icon: The icon associated to a player
        :param loc: The cell number of the board where the last move was placed
        :return boolean:
        """
        x, y = self.get_array_position(loc)

        # making sure the icon is on the diagonal first
        if x + y == self.boardSize:
            for i in range(self.boardSize):
                if self.board[i][self.boardSize - i] != icon:
                    return False

            return True

        else:
            return False

    def checkFullBoard(self):
        return len(self.remainingCells) == 0
