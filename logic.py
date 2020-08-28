from board import Board


class Logic(Board):
    def __init__(self):
        self.winner = None
        pass

    def checkHorizontalWinCase(self):
        """
        Checks if a player has won on the horizontal axis of the game
        if a winner was chosen, then
        :return boolean: if there is a winner returns a True, otherwise false
        """
        for row in self.board:
            if row.count(row[0]) == self.boardSize:
                self.winner = row[0]
                return True

        return False

    def checkVerticalWinCase(self):
        """
        Checks if a player has won on the vertical axis of the game
        if a winner was chosen, then
        :return boolean: if there is a winner returns a True, otherwise false
        """
        for row in range(len(self.board)):
            start =
            for col in range(len(self.board[row])):



            if self.board[row].count(self.board[row][0]) == self.boardSize:
                return True

        return False

    def checkFullBoard(self):
        return len(self.remainingCells) == 0
