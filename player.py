from board import Board


class Player(Board):

    def __init__(self, name, icon):
        self.name = name
        self.icon = icon

    def __str__(self):
        return self.icon
